import path from "path";
import fs from "fs";

/**
 * Resolves paths to the SQLite databases across local dev, Next.js root, and Vercel serverless lambdas.
 */
export function getDatabasePath(dbName: "scholarships_database.db" | "scholarx_sessions.db"): string {
  const cwd = process.cwd();

  const candidatePaths = [
    // 1. Inside frontend/data (bundled with Next.js)
    path.join(cwd, "data", dbName),
    path.join(cwd, "frontend", "data", dbName),
    // 2. Direct in frontend root
    path.join(cwd, dbName),
    // 3. Parent data directory (when running from frontend/)
    path.join(cwd, "..", "data", dbName),
    path.join(cwd, "..", dbName),
    // 4. Absolute fallback based on __dirname if available
    path.resolve(__dirname, "..", "..", "data", dbName),
  ];

  for (const candidate of candidatePaths) {
    if (fs.existsSync(candidate)) {
      return candidate;
    }
  }

  // Fallback to local data folder
  return path.join(cwd, "data", dbName);
}

/**
 * Returns a writable path for sessions database (using /tmp on serverless when needed).
 */
export function getWritableSessionsDbPath(): string {
  const primary = getDatabasePath("scholarx_sessions.db");
  if (fs.existsSync(primary)) {
    try {
      fs.accessSync(primary, fs.constants.W_OK);
      return primary;
    } catch {
      // Read-only filesystem (e.g. Vercel deployment) -> copy to /tmp for mutation
      const tmpPath = path.join("/tmp", "scholarx_sessions.db");
      if (!fs.existsSync(tmpPath)) {
        try {
          fs.copyFileSync(primary, tmpPath);
        } catch {
          return primary;
        }
      }
      return tmpPath;
    }
  }

  return primary;
}
