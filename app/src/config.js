import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const appDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const repoRoot = path.resolve(appDir, '..');
export const config = JSON.parse(fs.readFileSync(path.join(appDir, 'config.json'), 'utf8'));

/** Today's date as YYYY-MM-DD in the configured timezone. */
export function today(tz = config.timezone, now = new Date()) {
  return new Intl.DateTimeFormat('en-CA', { timeZone: tz, year: 'numeric', month: '2-digit', day: '2-digit' }).format(now);
}
