// Event Source Abstraction (§35, §36, §37, §38)
// Provides a unified interface for both Live SSE execution and Demo fixture execution.

import { ScholarXEvent } from "@/lib/types";

export type ExecutionMode = "demo" | "live";

export interface EventSourceListener {
  (event: ScholarXEvent): void;
}

export interface IEventSource {
  readonly mode: ExecutionMode;
  start: () => void;
  stop: () => void;
  pause: () => void;
  resume: () => void;
  setSpeed: (multiplier: number) => void;
  addListener: (listener: EventSourceListener) => () => void;
  isActive: () => boolean;
}

export class LiveEventSource implements IEventSource {
  public readonly mode: ExecutionMode = "live";
  private listeners: Set<EventSourceListener> = new Set();
  private running: boolean = false;
  private speed: number = 1.0;

  constructor() {}

  public start() {
    this.running = true;
  }

  public stop() {
    this.running = false;
  }

  public pause() {
    this.running = false;
  }

  public resume() {
    this.running = true;
  }

  public setSpeed(multiplier: number) {
    this.speed = multiplier;
  }

  public addListener(listener: EventSourceListener): () => void {
    this.listeners.add(listener);
    return () => {
      this.listeners.delete(listener);
    };
  }

  public emit(event: ScholarXEvent) {
    if (!this.running) return;
    this.listeners.forEach((listener) => {
      try {
        listener(event);
      } catch (err) {
        console.error("Error in event source listener:", err);
      }
    });
  }

  public isActive(): boolean {
    return this.running;
  }
}
