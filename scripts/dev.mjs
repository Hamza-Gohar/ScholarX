#!/usr/bin/env node

/**
 * ScholarX — Unified Development Orchestrator
 * Automatically manages both FastAPI backend (port 8000) and Next.js frontend (port 3000).
 * Ensures zero-configuration startup whether invoked from repo root or frontend directory.
 */

import { spawn, execSync } from "node:child_process";
import http from "node:http";
import path from "node:path";
import fs from "node:fs";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Resolve repository root directory
let repoRoot = path.resolve(__dirname, "..");
if (!fs.existsSync(path.join(repoRoot, "backend")) && fs.existsSync(path.join(process.cwd(), "backend"))) {
  repoRoot = process.cwd();
}

const frontendDir = path.join(repoRoot, "frontend");

// Terminal colors
const CYAN = "\x1b[36m";
const GREEN = "\x1b[32m";
const YELLOW = "\x1b[33m";
const RED = "\x1b[31m";
const BOLD = "\x1b[1m";
const RESET = "\x1b[0m";

function log(prefix, color, message) {
  const time = new Date().toLocaleTimeString();
  console.log(`${color}${BOLD}[${prefix} ${time}]${RESET} ${message}`);
}

function freePortIfOccupied(port) {
  try {
    execSync(`fuser -k ${port}/tcp 2>/dev/null || true`);
  } catch {
    try {
      const pids = execSync(`lsof -ti :${port} 2>/dev/null`, { encoding: "utf-8" }).trim();
      if (pids) {
        for (const pid of pids.split("\n")) {
          if (pid.trim()) {
            try { process.kill(Number(pid.trim()), "SIGKILL"); } catch {}
          }
        }
      }
    } catch {}
  }
}

function checkBackendHealth(timeoutMs = 1000) {
  return new Promise((resolve) => {
    const req = http.get("http://127.0.0.1:8000/api/health", { timeout: timeoutMs }, (res) => {
      resolve(res.statusCode === 200);
    });
    req.on("error", () => resolve(false));
    req.on("timeout", () => {
      req.destroy();
      resolve(false);
    });
  });
}

function findPythonBinary() {
  const candidatePaths = [
    path.join(repoRoot, ".venv", "bin", "python"),
    path.join(repoRoot, "venv", "bin", "python"),
    path.join(repoRoot, ".venv", "Scripts", "python.exe"),
    path.join(repoRoot, "venv", "Scripts", "python.exe"),
  ];

  for (const p of candidatePaths) {
    if (fs.existsSync(p)) {
      return p;
    }
  }

  return "python3";
}

let backendProcess = null;
let frontendProcess = null;
let isShuttingDown = false;

function shutdown() {
  if (isShuttingDown) return;
  isShuttingDown = true;
  log("ScholarX", YELLOW, "Shutting down all ScholarX services...");

  if (frontendProcess && !frontendProcess.killed) {
    try {
      frontendProcess.kill("SIGTERM");
    } catch {}
  }

  if (backendProcess && !backendProcess.killed) {
    try {
      backendProcess.kill("SIGTERM");
      setTimeout(() => {
        if (backendProcess && !backendProcess.killed) {
          try {
            backendProcess.kill("SIGKILL");
          } catch {}
        }
      }, 1500);
    } catch {}
  }

  setTimeout(() => process.exit(0), 1000);
}

process.on("SIGINT", shutdown);
process.on("SIGTERM", shutdown);
process.on("exit", shutdown);

async function main() {
  console.log("\n" + "═".repeat(60));
  console.log(`  ${BOLD}ScholarX Unified Mission Control — Launching Environment${RESET}`);
  console.log("═".repeat(60) + "\n");

  log("ScholarX", CYAN, `Repository root: ${repoRoot}`);

  // Step 1: Check if backend is already running
  const alreadyRunning = await checkBackendHealth(800);
  if (alreadyRunning) {
    log("Backend", GREEN, "FastAPI backend is already ACTIVE and healthy on http://127.0.0.1:8000");
  } else {
    // If port 8000 has a zombie process that isn't healthy, clear it
    freePortIfOccupied(8000);

    const pythonBin = findPythonBinary();
    log("Backend", CYAN, `Starting FastAPI backend with ${pythonBin} on port 8000...`);

    const backendEnv = {
      ...process.env,
      PYTHONPATH: "backend",
      PYTHONUNBUFFERED: "1",
    };

    backendProcess = spawn(
      pythonBin,
      ["-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"],
      {
        cwd: repoRoot,
        env: backendEnv,
        stdio: ["ignore", "pipe", "pipe"],
      }
    );

    backendProcess.stdout.on("data", (chunk) => {
      const lines = chunk.toString().split("\n");
      for (const line of lines) {
        if (line.trim()) {
          console.log(`${CYAN}[Backend]${RESET} ${line}`);
        }
      }
    });

    backendProcess.stderr.on("data", (chunk) => {
      const lines = chunk.toString().split("\n");
      for (const line of lines) {
        if (line.trim()) {
          console.error(`${CYAN}[Backend err]${RESET} ${line}`);
        }
      }
    });

    backendProcess.on("close", (code) => {
      if (!isShuttingDown) {
        log("Backend", RED, `Backend process terminated with code ${code}`);
      }
    });

    // Wait for backend to report healthy
    log("Backend", YELLOW, "Waiting for backend health check...");
    let healthy = false;
    const maxRetries = 40; // 40 * 250ms = 10s
    for (let i = 0; i < maxRetries; i++) {
      await new Promise((r) => setTimeout(r, 250));
      healthy = await checkBackendHealth(500);
      if (healthy) break;
    }

    if (!healthy) {
      log("Backend", RED, "⚠️  Backend did not report ready within 10 seconds. Starting frontend anyway with offline fallback.");
    } else {
      log("Backend", GREEN, "✅ FastAPI backend is HEALTHY and listening on http://127.0.0.1:8000");
    }
  }

  // Step 2: Ensure port 3000 is available for Next.js
  freePortIfOccupied(3000);

  // Step 3: Start Next.js frontend
  log("Frontend", GREEN, "Starting Next.js development server on port 3000...");

  frontendProcess = spawn("npx", ["next", "dev", "-p", "3000"], {
    cwd: frontendDir,
    env: process.env,
    stdio: ["inherit", "pipe", "pipe"],
  });

  frontendProcess.stdout.on("data", (chunk) => {
    const lines = chunk.toString().split("\n");
    for (const line of lines) {
      if (line.trim()) {
        console.log(`${GREEN}[Frontend]${RESET} ${line}`);
      }
    }
  });

  frontendProcess.stderr.on("data", (chunk) => {
    const lines = chunk.toString().split("\n");
    for (const line of lines) {
      if (line.trim()) {
        console.error(`${GREEN}[Frontend err]${RESET} ${line}`);
      }
    }
  });

  frontendProcess.on("close", (code) => {
    if (!isShuttingDown) {
      log("Frontend", YELLOW, `Frontend server closed with code ${code}`);
      shutdown();
    }
  });
}

main().catch((err) => {
  log("ScholarX", RED, `Fatal startup error: ${err.message}`);
  shutdown();
});
