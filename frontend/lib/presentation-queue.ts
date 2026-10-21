// Frontend Presentation Queue (§8.5, §24)
// Buffers raw backend SSE events and delivers them to the visual theatre at human-comprehensible pacing.

import { ScholarXEvent } from "./types";

export interface QueuedEvent {
  event: ScholarXEvent;
  visualDelayMs: number;
  description: string;
}

export class PresentationQueue {
  private queue: QueuedEvent[] = [];
  private isProcessing: boolean = false;
  private timer: NodeJS.Timeout | null = null;
  private onDispatch: ((event: ScholarXEvent) => void) | null = null;
  private speedMultiplier: number = 1.0;

  constructor(onDispatch?: (event: ScholarXEvent) => void) {
    if (onDispatch) this.onDispatch = onDispatch;
  }

  public setDispatchHandler(handler: (event: ScholarXEvent) => void) {
    this.onDispatch = handler;
  }

  public setSpeed(multiplier: number) {
    this.speedMultiplier = Math.max(0.5, Math.min(5.0, multiplier));
  }

  public enqueue(event: ScholarXEvent) {
    const delay = this.calculatePacing(event);
    this.queue.push({
      event,
      visualDelayMs: delay,
      description: event.event_type,
    });

    if (!this.isProcessing) {
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
  }

  public getQueueLength(): number {
    return this.queue.length;
  }

  private calculatePacing(event: ScholarXEvent): number {
    const type = event.event_type;

    // Command travel (§8.5: 700 to 1200ms)
    if (type.includes("COMMAND") || type.includes("DISPATCH") || type.includes("INITIATED")) {
      return 950;
    }
    // Acknowledgement (§8.5: 500 to 800ms)
    if (type.includes("ACK") || type.includes("SPAWNED")) {
      return 650;
    }
    // Report assembly & Return (§8.5: 1200 to 2200ms)
    if (type.includes("REPORT") || type.includes("SYNTHESIS")) {
      return 1500;
    }
    // Verification confrontation & Skeptic challenge (§14)
    if (type.includes("SKEPTIC") || type.includes("VERIF")) {
      return 1300;
    }
    // Candidate emergence & flow (§12)
    if (type.includes("CANDIDATE") || type.includes("ELIGIBILITY") || type.includes("COST")) {
      return 900;
    }
    // Ranking movements (§16)
    if (type.includes("RANKING") || type.includes("SCORE")) {
      return 1100;
    }
    // Default steady pacing
    return 600;
  }

  private processNext() {
    if (this.queue.length === 0) {
      this.isProcessing = false;
      return;
    }

    this.isProcessing = true;
    const item = this.queue.shift()!;
    const pacedDuration = item.visualDelayMs / this.speedMultiplier;

    if (this.onDispatch) {
      this.onDispatch(item.event);
    }

    this.timer = setTimeout(() => {
      this.processNext();
    }, pacedDuration);
  }
}

export const globalPresentationQueue = new PresentationQueue();
