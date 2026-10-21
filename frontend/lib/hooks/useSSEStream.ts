"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import { ScholarXEvent, EventSeverity } from "@/lib/types";

export type SSEConnectionState =
  | "DISCONNECTED"
  | "CONNECTING"
  | "CONNECTED"
  | "RECONNECTING"
  | "ERROR"
  | "ENDED";

export interface SSEStreamOptions {
  sessionId: string;
  enabled?: boolean;
  profile?: any;
  onEvent?: (event: ScholarXEvent) => void;
  onError?: (error: any) => void;
  onStateChange?: (state: SSEConnectionState) => void;
  maxRetries?: number;
  initialBackoffMs?: number;
  maxBackoffMs?: number;
}

export interface UseSSEStreamResult {
  connectionState: SSEConnectionState;
  lastEvent: ScholarXEvent | null;
  eventCount: number;
  error: string | null;
  reconnect: () => void;
  disconnect: () => void;
}

// Bounded deduplication ring cache size (§15)
const MAX_SEEN_EVENT_IDS = 1000;

export function useSSEStream({
  sessionId,
  enabled = true,
  profile,
  onEvent,
  onError,
  onStateChange,
  maxRetries = 5,
  initialBackoffMs = 500,
  maxBackoffMs = 8000,
}: SSEStreamOptions): UseSSEStreamResult {
  const [connectionState, setConnectionState] = useState<SSEConnectionState>("DISCONNECTED");
  const [lastEvent, setLastEvent] = useState<ScholarXEvent | null>(null);
  const [eventCount, setEventCount] = useState<number>(0);
  const [error, setError] = useState<string | null>(null);

  const eventSourceRef = useRef<EventSource | null>(null);
  const reconnectTimerRef = useRef<NodeJS.Timeout | null>(null);
  const retryCountRef = useRef<number>(0);
  const seenEventIdsRef = useRef<Set<string>>(new Set());
  const seenEventOrderRef = useRef<string[]>([]);
  const isManuallyDisconnectedRef = useRef<boolean>(false);
  const lastEventTimestampRef = useRef<number>(0);

  // Stable callback references
  const onEventRef = useRef(onEvent);
  onEventRef.current = onEvent;
  const onErrorRef = useRef(onError);
  onErrorRef.current = onError;
  const onStateChangeRef = useRef(onStateChange);
  onStateChangeRef.current = onStateChange;

  const updateState = useCallback((newState: SSEConnectionState) => {
    setConnectionState(newState);
    onStateChangeRef.current?.(newState);
  }, []);

  // Validation function (§17)
  const validateEvent = useCallback(
    (raw: any): ScholarXEvent | null => {
      if (!raw || typeof raw !== "object") return null;
      if (!raw.event_id || typeof raw.event_id !== "string") return null;
      if (!raw.session_id || raw.session_id !== sessionId) return null;
      if (!raw.event_type || typeof raw.event_type !== "string") return null;

      return {
        event_id: raw.event_id,
        session_id: raw.session_id,
        event_type: raw.event_type,
        agent_id: raw.agent_id || "orchestrator",
        agent_display_name: raw.agent_display_name || "ScholarX Agent",
        component_type: raw.component_type || "AGENT",
        phase: raw.phase || "ORCHESTRATION",
        timestamp: raw.timestamp || new Date().toISOString(),
        payload: raw.payload && typeof raw.payload === "object" ? raw.payload : {},
        severity: (raw.severity as EventSeverity) || "INFO",
        step_number: raw.step_number,
        total_steps: raw.total_steps,
        related_scholarship_id: raw.related_scholarship_id || raw.payload?.scholarship_id || null,
      };
    },
    [sessionId]
  );

  // Event handler with deduplication and idempotency (§14, §15, §16)
  const handleRawEvent = useCallback(
    (rawString: string) => {
      try {
        const parsed = JSON.parse(rawString);
        const event = validateEvent(parsed);
        if (!event) return;

        // Deduplication check (§15)
        if (seenEventIdsRef.current.has(event.event_id)) {
          return; // Ignore duplicate event silently
        }

        // Add to bounded deduplication cache
        seenEventIdsRef.current.add(event.event_id);
        seenEventOrderRef.current.push(event.event_id);
        if (seenEventOrderRef.current.length > MAX_SEEN_EVENT_IDS) {
          const evicted = seenEventOrderRef.current.shift();
          if (evicted) seenEventIdsRef.current.delete(evicted);
        }

        // Out-of-order check (§16)
        const eventTime = new Date(event.timestamp).getTime();
        if (eventTime) {
          lastEventTimestampRef.current = Math.max(lastEventTimestampRef.current, eventTime);
        }

        setLastEvent(event);
        setEventCount((prev) => prev + 1);

        // Terminal check (§64)
        if (event.event_type === "MISSION_COMPLETE" || event.event_type === "PIPELINE_ERROR") {
          updateState("ENDED");
        }

        // Dispatch to subscriber
        onEventRef.current?.(event);
      } catch (err) {
        console.warn("Malformed SSE frame payload:", err);
      }
    },
    [updateState, validateEvent]
  );

  const cleanupConnection = useCallback(() => {
    if (eventSourceRef.current) {
      eventSourceRef.current.close();
      eventSourceRef.current = null;
    }
    if (reconnectTimerRef.current) {
      clearTimeout(reconnectTimerRef.current);
      reconnectTimerRef.current = null;
    }
  }, []);

  const connect = useCallback(() => {
    if (!sessionId || !enabled) return;
    cleanupConnection();
    isManuallyDisconnectedRef.current = false;

    updateState(retryCountRef.current > 0 ? "RECONNECTING" : "CONNECTING");
    setError(null);

    // Endpoint format supporting path-based session identifier with profile context
    let url = `/api/stream/${encodeURIComponent(sessionId)}`;
    const targetProf = profile || (typeof window !== "undefined" ? (() => {
      try {
        const raw = localStorage.getItem(`scholarx_profile_${sessionId}`) || localStorage.getItem("scholarx_last_profile");
        return raw ? JSON.parse(raw) : null;
      } catch { return null; }
    })() : null);

    if (targetProf) {
      const deg = targetProf.preferences?.target_degree_level || targetProf.academic?.degree_level;
      const fld = targetProf.preferences?.target_fields?.[0] || targetProf.academic?.field_of_study;
      const nm = targetProf.personal?.name;
      const gpa = targetProf.academic?.percentage || targetProf.academic?.gpa_percentage;
      const rawRegs =
        targetProf.preferences?.preferred_regions ||
        targetProf.preferences?.preferredRegions ||
        targetProf.personal?.target_regions ||
        targetProf.personal?.targetRegions;
      const params = new URLSearchParams();
      if (deg) params.set("degree", deg);
      if (fld) params.set("field", fld);
      if (nm) params.set("name", nm);
      if (gpa) params.set("gpa", String(gpa));
      if (Array.isArray(rawRegs) && rawRegs.length > 0) {
        params.set("regions", rawRegs.join(","));
      }
      const qs = params.toString();
      if (qs) url += `?${qs}`;
    }

    const es = new EventSource(url);
    eventSourceRef.current = es;

    es.onopen = () => {
      retryCountRef.current = 0;
      updateState("CONNECTED");
    };

    // Standard onmessage listener for message frames
    es.onmessage = (e) => {
      if (e.data && e.data.trim().length > 0) {
        handleRawEvent(e.data);
      }
    };

    // Dedicated scholarx event listener (§10)
    es.addEventListener("scholarx", (e: MessageEvent) => {
      if (e.data && e.data.trim().length > 0) {
        handleRawEvent(e.data);
      }
    });

    // Listeners for all specific AgentEventType named frames emitted by backend
    const EVENT_TYPES = [
      "MISSION_INITIATED",
      "INPUT_NORMALIZED",
      "FLEET_DISPATCHED",
      "DIRECTIVE_DISPATCHED",
      "SCOUT_DEPLOYED",
      "SEARCH_QUERY_EXECUTED",
      "PAGE_SCRAPED",
      "SOURCE_FOUND",
      "CANDIDATE_EXTRACTED",
      "SCOUT_PROGRESS",
      "SCOUT_COMPLETE",
      "DISCOVERY_AGGREGATION_COMPLETE",
      "ELIGIBILITY_CHECK_STARTED",
      "DIMENSION_EVALUATED",
      "CRITICAL_BARRIER_DETECTED",
      "ELIGIBILITY_COMPLETE",
      "COST_ANALYSIS_STARTED",
      "PKR_BREAKDOWN_CALCULATED",
      "COST_ANALYSIS_COMPLETE",
      "DEADLINE_EVALUATED",
      "DEADLINE_COMPLETE",
      "DOCUMENT_CHECK_STARTED",
      "DOCUMENT_VERIFIED",
      "DOCUMENT_CHECK_COMPLETE",
      "SKEPTIC_CHALLENGE_RAISED",
      "SKEPTIC_DEBATE_CLASH",
      "SKEPTIC_COMPLETE",
      "SYNTHESIS_STARTED",
      "SYNTHESIS_COMPLETE",
      "FLEET_PAUSED",
      "DATABASE_RETRIEVAL_COMPLETE",
      "SUBJECTS_EVALUATED",
      "INELIGIBILITY_DETECTED",
      "RANKING_CALCULATED",
      "ROADMAP_GENERATED",
      "DOSSIER_COMPILED",
      "MISSION_COMPLETE",
      "PIPELINE_ERROR",
      "SESSION_CREATED",
      "SESSION_LOADED",
      "SESSION_SAVED",
      "CACHE_HIT",
      "CACHE_MISS",
    ];

    EVENT_TYPES.forEach((evtType) => {
      es.addEventListener(evtType, (e: MessageEvent) => {
        if (e.data && e.data.trim().length > 0) {
          handleRawEvent(e.data);
        }
      });
    });

    es.onerror = (e) => {
      if (isManuallyDisconnectedRef.current) return;

      cleanupConnection();

      if (retryCountRef.current < maxRetries) {
        const backoff = Math.min(
          initialBackoffMs * Math.pow(2, retryCountRef.current),
          maxBackoffMs
        );
        retryCountRef.current += 1;
        updateState("RECONNECTING");

        reconnectTimerRef.current = setTimeout(() => {
          connect();
        }, backoff);
      } else {
        const errMsg = "Max connection retries exceeded. Backend unavailable.";
        setError(errMsg);
        updateState("ERROR");
        onErrorRef.current?.(e);
      }
    };
  }, [
    sessionId,
    enabled,
    cleanupConnection,
    updateState,
    handleRawEvent,
    maxRetries,
    initialBackoffMs,
    maxBackoffMs,
    profile,
  ]);

  const disconnect = useCallback(() => {
    isManuallyDisconnectedRef.current = true;
    cleanupConnection();
    updateState("DISCONNECTED");
  }, [cleanupConnection, updateState]);

  const reconnect = useCallback(() => {
    retryCountRef.current = 0;
    connect();
  }, [connect]);

  // Lifecycle effect
  useEffect(() => {
    if (enabled && sessionId) {
      seenEventIdsRef.current.clear();
      seenEventOrderRef.current = [];
      setEventCount(0);
      setLastEvent(null);
      retryCountRef.current = 0;
      connect();
    } else {
      disconnect();
    }

    return () => {
      cleanupConnection();
    };
  }, [sessionId, enabled, connect, disconnect, cleanupConnection]);

  return {
    connectionState,
    lastEvent,
    eventCount,
    error,
    reconnect,
    disconnect,
  };
}
