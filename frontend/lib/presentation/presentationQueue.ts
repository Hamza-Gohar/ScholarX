// Enhanced Presentation Queue (§20, §21, §22, §58, §59)
// Paces real-time events for human comprehension, performs burst coalescing, and manages dynamic backpressure.

import { MasterPresentationEvent, PresentationQueueContract } from "./types";

export type PresentationDispatchHandler = (event: MasterPresentationEvent, isCoalesced: boolean) => void;

interface QueuedItem {
  event: MasterPresentationEvent;
  enqueuedAt: number;
}

export class MasterPresentationQueue implements PresentationQueueContract {
  private queue: QueuedItem[] = [];
  private isProcessing: boolean = false;
  private isPaused: boolean = false;
  private timer: NodeJS.Timeout | null = null;
  private onDispatch: PresentationDispatchHandler | null = null;
  private baseSpeedMultiplier: number = 1.0;
  
  // Burst tracking for coalescing (§22)
  private recentCoalesceCounts: Map<string, number> = new Map();
  private lastCoalesceReset: number = Date.now();

  constructor(onDispatch?: PresentationDispatchHandler) {
    if (onDispatch) this.onDispatch = onDispatch;
  }

  public setDispatchHandler(handler: PresentationDispatchHandler) {
    this.onDispatch = handler;
    this.resume();
  }

  public setSpeed(multiplier: number) {
    this.baseSpeedMultiplier = Math.max(0.5, Math.min(5.0, multiplier));
  }

  public pause() {
    this.isPaused = true;
    if (this.timer) {
      clearTimeout(this.timer);
      this.timer = null;
    }
  }

  public resume() {
    this.isPaused = false;
    if (!this.isProcessing && this.queue.length > 0) {
      this.processNext();
    }
  }

  public clear() {
    this.queue = [];
    this.isProcessing = false;
    if (this.timer) {
      clearTimeout(this.timer);
      this.timer = null;
    }
    this.recentCoalesceCounts.clear();
  }

  public getPendingCount(): number {
    return this.queue.length;
  }

  private static readonly MAX_QUEUE_DEPTH = 100;

  public enqueue(event: MasterPresentationEvent) {
    const now = Date.now();

    // Reset coalesce window every 3 seconds
    if (now - this.lastCoalesceReset > 3000) {
      this.recentCoalesceCounts.clear();
      this.lastCoalesceReset = now;
    }

    // Burst coalescing check (§22, §58, §83)
    let shouldCoalesce = false;
    if (event.coalesceKey) {
      const currentCount = this.recentCoalesceCounts.get(event.coalesceKey) || 0;
      this.recentCoalesceCounts.set(event.coalesceKey, currentCount + 1);

      // If more than 2 similar events occurred in current window, coalesce background animation
      if (currentCount >= 2 && event.importance !== "HERO") {
        shouldCoalesce = true;
      }
    }

    // Bounded Queue Enforcement (§44, §82): Never exceed MAX_QUEUE_DEPTH
    if (this.queue.length >= MasterPresentationQueue.MAX_QUEUE_DEPTH) {
      if (event.importance === "HERO") {
        // Evict the oldest non-HERO item to guarantee HERO event delivery
        const evictIdx = this.queue.findIndex((item) => item.event.importance !== "HERO");
        if (evictIdx !== -1) {
          this.queue.splice(evictIdx, 1);
        }
      } else {
        // Drop excessive low-priority burst events
        return;
      }
    }

    // If ranking calculated or mission complete, flush any pending background search queries to show direct opportunities immediately
    if (event.eventType === "MISSION_COMPLETE" || event.eventType === "RANKING_CALCULATED") {
      this.queue = this.queue.filter(
        (item) => item.event.importance === "HERO"
      );
    }

    // Preserve causal phase order: push directly to queue
    this.queue.push({ event, enqueuedAt: now });

    if (!this.isProcessing && !this.isPaused) {
      this.processNext();
    }
  }

  private processNext() {
    if (this.queue.length === 0) {
      this.isProcessing = false;
      return;
    }
    if (this.isPaused) {
      this.isProcessing = false;
      return;
    }

    this.isProcessing = true;
    const item = this.queue.shift()!;
    const event = item.event;

    // Calculate dynamic backpressure multiplier (§44, §59)
    const queueDepth = this.queue.length;
    let dynamicMultiplier = this.baseSpeedMultiplier;
    if (queueDepth > 30) {
      dynamicMultiplier = Math.min(10.0, this.baseSpeedMultiplier * 8.0);
    } else if (queueDepth > 15) {
      dynamicMultiplier = Math.min(6.0, this.baseSpeedMultiplier * 5.0);
    } else if (queueDepth > 6) {
      dynamicMultiplier = Math.min(4.0, this.baseSpeedMultiplier * 3.0);
    } else if (queueDepth > 2) {
      dynamicMultiplier = Math.min(2.5, this.baseSpeedMultiplier * 2.0);
    }

    // Check if this item is marked for coalesced compression
    const coalesceKey = event.coalesceKey;
    const isCoalesced = coalesceKey ? (this.recentCoalesceCounts.get(coalesceKey) || 0) > 2 : false;

    // Calculate pacing duration
    let delay = (event.minimumDisplayMs + event.holdAfterMs) / dynamicMultiplier;
    if (event.importance !== "HERO") {
      if (queueDepth > 10) {
        delay = Math.min(40, delay);
      } else {
        delay = Math.min(75, delay);
      }
    }

    // Dispatch event to visual theatre safely without breaking queue cycle
    if (this.onDispatch) {
      try {
        this.onDispatch(event, isCoalesced);
      } catch (err) {
        console.error("MasterPresentationQueue dispatch error on event:", event.eventType, err);
      }
    }

    this.timer = setTimeout(() => {
      this.processNext();
    }, delay);
  }
}

export const masterPresentationQueue = new MasterPresentationQueue();
