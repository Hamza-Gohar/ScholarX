#!/usr/bin/env node

/**
 * ScholarX — Unified Production Orchestrator
 * Starts both FastAPI backend (port 8000, production mode) and Next.js frontend (port 3000, production mode).
 */

import { spawn, execSync } from "node:child_process";
import http from "node:http";
import path from "node:path";
import fs from "node:fs";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let repoRoot = path.resolve(__dirname, "..");
if (!fs.existsSync(path.join(repoRoot, "backend")) && fs.existsSync(path.join(process.cwd(), "backend"))) {
  repoRoot = process.cwd();
}

const frontendDir = path.join(repoRoot, "frontend");

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
  ];
  for (const p of candidatePaths) {
    if (fs.existsSync(p)) return p;
  }
  return "python3";
}

let backendProcess = null;
let frontendProcess = null;
let isShuttingDown = false;

function shutdown() {
  if (isShuttingDown) return;
  isShuttingDown = true;
  log("ScholarX", YELLOW, "Shutting down production services...");

  if (frontendProcess && !frontendProcess.killed) {
    try { frontendProcess.kill("SIGTERM"); } catch {}
  }
  if (backendProcess && !backendProcess.killed) {
    try {
      backendProcess.kill("SIGTERM");
      setTimeout(() => {
        if (backendProcess && !backendProcess.killed) {
          try { backendProcess.kill("SIGKILL"); } catch {}
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
  console.log(`  ${BOLD}ScholarX Production Server — Dual Service Mode${RESET}`);
  console.log("═".repeat(60) + "\n");

  const alreadyRunning = await checkBackendHealth(800);
  if (alreadyRunning) {
    log("Backend", GREEN, "FastAPI backend is already ACTIVE and healthy on http://127.0.0.1:8000");
  } else {
    freePortIfOccupied(8000);
    const pythonBin = findPythonBinary();
    log("Backend", CYAN, `Starting production backend with ${pythonBin}...`);

    backendProcess = spawn(
      pythonBin,
      ["-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"],
      {
        cwd: repoRoot,
        env: { ...process.env, PYTHONPATH: "backend", PYTHONUNBUFFERED: "1" },
        stdio: ["ignore", "pipe", "pipe"],
      }
    );

    backendProcess.stdout.on("data", (c) => console.log(`${CYAN}[Backend]${RESET} ${c.toString().trim()}`));
    backendProcess.stderr.on("data", (c) => console.error(`${CYAN}[Backend err]${RESET} ${c.toString().trim()}`));

    let healthy = false;
    for (let i = 0; i < 40; i++) {
      await new Promise((r) => setTimeout(r, 250));
      healthy = await checkBackendHealth(500);
      if (healthy) break;
    }

    if (healthy) {
      log("Backend", GREEN, "✅ Backend is HEALTHY on http://127.0.0.1:8000");
    } else {
      log("Backend", RED, "⚠️  Backend did not report ready within 10s, proceeding anyway.");
    }
  }

  freePortIfOccupied(3000);
  log("Frontend", GREEN, "Starting Next.js production server on port 3000...");
  frontendProcess = spawn("npx", ["next", "start", "-p", "3000"], {
    cwd: frontendDir,
    env: process.env,
    stdio: ["inherit", "pipe", "pipe"],
  });

  frontendProcess.stdout.on("data", (c) => console.log(`${GREEN}[Frontend]${RESET} ${c.toString().trim()}`));
  frontendProcess.stderr.on("data", (c) => console.error(`${GREEN}[Frontend err]${RESET} ${c.toString().trim()}`));

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
