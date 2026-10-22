// Gmail access. READ ONLY: this module only calls users.messages.list and users.messages.get.
// Sending the finished draft lives in mail.js and is limited to one hard coded recipient.
import { google } from 'googleapis';

export const SCOPES = [
  'https://www.googleapis.com/auth/gmail.readonly',
  'https://www.googleapis.com/auth/gmail.send',
];

export function gmailClient(env = process.env) {
  for (const k of ['GOOGLE_CLIENT_ID', 'GOOGLE_CLIENT_SECRET', 'GOOGLE_REFRESH_TOKEN']) {
    if (!env[k]) throw new Error(`Missing ${k}. See app/README.md, step 2.`);
  }
  const auth = new google.auth.OAuth2(env.GOOGLE_CLIENT_ID, env.GOOGLE_CLIENT_SECRET);
  auth.setCredentials({ refresh_token: env.GOOGLE_REFRESH_TOKEN });
  return { gmail: google.gmail({ version: 'v1', auth }), auth };
}

const decode = (s = '') => Buffer.from(s.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf8');
const header = (msg, name) => msg.payload?.headers?.find((h) => h.name.toLowerCase() === name.toLowerCase())?.value ?? '';

function collect(part, out) {
  if (!part) return;
  if (part.mimeType === 'text/plain' && part.body?.data) out.plain.push(decode(part.body.data));
  else if (part.mimeType === 'text/html' && part.body?.data) out.html.push(decode(part.body.data));
  for (const p of part.parts ?? []) collect(p, out);
}

export function htmlToText(html) {
  return html
    .replace(/<(style|script)[\s\S]*?<\/\1>/gi, '')
    .replace(/<br\s*\/?>/gi, '\n')
    .replace(/<\/(p|div|h[1-6]|li|tr)>/gi, '\n')
    .replace(/<a [^>]*href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/gi, '$2 ($1)')
    .replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&#39;|&apos;/g, "'").replace(/&quot;/g, '"');
}

/** Remove tracking noise only. Nothing is truncated. */
export function cleanText(t) {
  return t
    .replace(/\[ https?:\/\/substack\.com\/redirect\/[^\]]*\]/g, '')
    .replace(/https?:\/\/substack\.com\/redirect\/\S+/g, '')
    .replace(/[͏​‌‍⁠﻿]/g, '')
    .replace(/^Unsubscribe .*$/gm, '')
    .replace(/[ \t]+\n/g, '\n')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

export function parseMessage(msg) {
  const out = { plain: [], html: [] };
  collect(msg.payload, out);
  const raw = out.plain.length ? out.plain.join('\n') : htmlToText(out.html.join('\n'));
  const text = cleanText(raw);
  const view = text.match(/View this post on the web at (\S+)/i);
  return {
    id: msg.id,
    threadId: msg.threadId,
    labelIds: msg.labelIds ?? [],
    from: header(msg, 'From'),
    subject: header(msg, 'Subject'),
    date: header(msg, 'Date'),
    url: view ? view[1] : null,
    text,
  };
}

const SYSTEM_NOTICE = /(is going live|is live on substack|live video with|recommended |posted new notes|added you|restacked)/i;

/** Heuristic skip list. The model also gets told to ignore anything that is not editorial. */
export function isLikelyNewsletter(m, cfg) {
  if (m.labelIds.includes('SENT')) return false;
  if (cfg.selfAddresses.some((a) => m.from.toLowerCase().includes(a))) return false;
  if (/no-reply@substack\.com/i.test(m.from) && SYSTEM_NOTICE.test(m.subject)) return false;
  if (m.text.length < cfg.minEmailChars) return false;
  return true;
}

export async function fetchNewsletters(gmail, cfg) {
  let q = cfg.gmailQuery;
  let list = await gmail.users.messages.list({ userId: 'me', q, maxResults: Math.min(cfg.maxEmails * 2, 100) });
  if (!list.data.messages?.length) {
    q = cfg.gmailQueryFallback;
    list = await gmail.users.messages.list({ userId: 'me', q, maxResults: Math.min(cfg.maxEmails * 2, 100) });
  }
  const ids = list.data.messages ?? [];
  if (!ids.length) throw new Error(`No emails matched either Gmail query. Last query: ${q}`);
  const kept = [];
  const skipped = [];
  for (const { id } of ids) {
    const res = await gmail.users.messages.get({ userId: 'me', id, format: 'full' });
    const m = parseMessage(res.data);
    if (isLikelyNewsletter(m, cfg)) kept.push(m);
    else skipped.push({ from: m.from, subject: m.subject, date: m.date });
    if (kept.length >= cfg.maxEmails) break;
  }
  return { query: q, found: ids.length, emails: kept, skipped };
}
