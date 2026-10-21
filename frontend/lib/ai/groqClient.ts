import fs from "fs";
import path from "path";

export interface GroqChatMessage {
  role: "system" | "user" | "assistant";
  content: string;
}

export interface GroqChatOptions {
  messages: GroqChatMessage[];
  model?: string;
  temperature?: number;
  max_tokens?: number;
  json_mode?: boolean;
}

export interface GroqChatResponse {
  content: string;
  model: string;
  keyIndex: number;
}

class GroqRoundRobinPool {
  private keys: string[] = [];
  private keyIndex: number = 0;
  private cooldowns: Map<number, number> = new Map();
  private initialized: boolean = false;

  private initializeKeys(): void {
    if (this.initialized && this.keys.length > 0) return;

    const gatheredKeys: string[] = [];

    // 1. Read from process.env
    for (let i = 1; i <= 20; i++) {
      const val = process.env[`GROQ_API_KEY_${i}`];
      if (val && val.trim() && !val.startsWith("your_")) {
        gatheredKeys.push(val.trim());
      }
    }
    if (process.env.GROQ_API_KEY && !gatheredKeys.includes(process.env.GROQ_API_KEY.trim())) {
      gatheredKeys.push(process.env.GROQ_API_KEY.trim());
    }

    // 2. Fallback to reading root or local .env if running in Node environment
    if (gatheredKeys.length === 0) {
      const candidatePaths = [
        path.join(process.cwd(), ".env.local"),
        path.join(process.cwd(), ".env"),
        path.join(process.cwd(), "..", ".env"),
      ];

      for (const p of candidatePaths) {
        try {
          if (fs.existsSync(p)) {
            const content = fs.readFileSync(p, "utf-8");
            const matches = content.match(/GROQ_API_KEY_\d+=[^\r\n]+/g) || [];
            for (const m of matches) {
              const [, val] = m.split("=");
              if (val && val.trim() && !val.startsWith("your_") && !gatheredKeys.includes(val.trim())) {
                gatheredKeys.push(val.trim());
              }
            }
          }
        } catch {
          // ignore file read error
        }
      }
    }

    this.keys = gatheredKeys;
    this.initialized = true;
  }

  public getKeyCount(): number {
    this.initializeKeys();
    return this.keys.length;
  }

  public getNextKey(): { key: string; index: number } | null {
    this.initializeKeys();
    if (this.keys.length === 0) return null;

    const now = Date.now();
    const totalKeys = this.keys.length;

    // Try finding an available key not currently in cooldown
    for (let attempts = 0; attempts < totalKeys; attempts++) {
      const idx = this.keyIndex % totalKeys;
      this.keyIndex = (this.keyIndex + 1) % totalKeys;

      const cooldownUntil = this.cooldowns.get(idx) || 0;
      if (now >= cooldownUntil) {
        return { key: this.keys[idx], index: idx };
      }
    }

    // If all keys are in cooldown, pick the next one anyway (soft fallback)
    const fallbackIdx = this.keyIndex % totalKeys;
    this.keyIndex = (this.keyIndex + 1) % totalKeys;
    return { key: this.keys[fallbackIdx], index: fallbackIdx };
  }

  public markCooldown(index: number, durationMs: number = 30000): void {
    this.cooldowns.set(index, Date.now() + durationMs);
  }

  public async chatCompletion(options: GroqChatOptions): Promise<GroqChatResponse> {
    this.initializeKeys();
    const totalKeys = this.keys.length;
    if (totalKeys === 0) {
      throw new Error("[GroqPool] No GROQ_API_KEY available in environment.");
    }

    const model = options.model || process.env.GROQ_MODEL || "qwen/qwen3.8-27b";
    const temperature = options.temperature ?? 0.0;
    const max_tokens = options.max_tokens ?? 500;

    let lastError: Error | null = null;
    const maxAttempts = Math.min(totalKeys, 5);

    for (let attempt = 0; attempt < maxAttempts; attempt++) {
      const keyInfo = this.getNextKey();
      if (!keyInfo) break;

      try {
        const payload: Record<string, any> = {
          model,
          messages: options.messages,
          temperature,
          max_tokens,
        };

        if (options.json_mode) {
          payload.response_format = { type: "json_object" };
        }

        const res = await fetch("https://api.groq.com/openai/v1/chat/completions", {
          method: "POST",
          headers: {
            Authorization: `Bearer ${keyInfo.key}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
          signal: AbortSignal.timeout(10000),
        });

        if (res.ok) {
          const data = await res.json();
          const content = data.choices?.[0]?.message?.content || "";
          return {
            content,
            model,
            keyIndex: keyInfo.index,
          };
        }

        // Handle 429 Too Many Requests or 5xx server errors by rotating
        if (res.status === 429) {
          this.markCooldown(keyInfo.index, 45000); // 45s cooldown on rate limit
        } else if (res.status >= 500) {
          this.markCooldown(keyInfo.index, 15000);
        }

        const errorText = await res.text().catch(() => "");
        lastError = new Error(`Groq HTTP ${res.status}: ${errorText.slice(0, 200)}`);
      } catch (err: any) {
        this.markCooldown(keyInfo.index, 10000);
        lastError = err;
      }
    }

    throw lastError || new Error("[GroqPool] All attempted Groq keys failed.");
  }
}

export const groqPool = new GroqRoundRobinPool();
