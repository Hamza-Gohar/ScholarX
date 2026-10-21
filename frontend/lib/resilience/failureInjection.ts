// Development-Only Failure Injection Framework (§17)
// Strictly for automated testing, rehearsal, and regression verification.
// NEVER exposed in Judge Mode or to judges.

export type FailureTarget =
  | "TAVILY_FAIL"
  | "FIRECRAWL_FAIL"
  | "JINA_FAIL"
  | "GEMINI_FAIL"
  | "GROQ_FAIL"
  | "REDIS_DISCONNECT"
  | "SSE_DISCONNECT"
  | "SCOUT_FAIL"
  | "SPECIALIST_FAIL"
  | "RANKING_FAIL"
  | "PDF_FAIL"
  | "WEB_ARTIFACT_FAIL"
  | "BURST_STORM"
  | "SLOW_TOOL";

export interface ActiveSimulatedFaults {
  [target: string]: boolean;
}

class FailureInjectionManager {
  private activeFaults: ActiveSimulatedFaults = {};
  private burstCallback?: () => void;

  public injectFault(target: FailureTarget): void {
    this.activeFaults[target] = true;
    console.info(`[Dev Failure Injection] Simulated fault activated: ${target}`);
  }

  public clearFault(target: FailureTarget): void {
    delete this.activeFaults[target];
    console.info(`[Dev Failure Injection] Simulated fault cleared: ${target}`);
  }

  public clearAllFaults(): void {
    this.activeFaults = {};
    console.info("[Dev Failure Injection] All simulated faults reset.");
  }

  public isFaultActive(target: FailureTarget): boolean {
    return Boolean(this.activeFaults[target]);
  }

  public listActiveFaults(): FailureTarget[] {
    return Object.keys(this.activeFaults) as FailureTarget[];
  }

  public registerBurstCallback(cb: () => void) {
    this.burstCallback = cb;
  }

  public triggerBurstStorm(eventCount: number = 100) {
    console.info(`[Dev Failure Injection] Triggering burst storm: ${eventCount} events`);
    this.burstCallback?.();
  }
}

export const devFailureInjector = new FailureInjectionManager();
