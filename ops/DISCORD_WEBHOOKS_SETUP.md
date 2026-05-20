# Discord Webhooks Setup — Theseus Phase 0

Theseus Phase 0 posts to **3 Discord channels** via webhooks:

| Channel | Purpose | Cadence |
|---|---|---|
| `#theseus-briefing` | Daily morning briefing — crawler progress, cost throughput, CMS-prep weak topics | Daily 07:00 NJT |
| `#theseus-alerts` | Kill switch engagements, cost cap warnings, ethics violations (mentions `@here`) | Event-driven |
| `#b2b-leads` | SaaS funnel notifications — sommelier candidates worth B2B outreach | Weekly, quiet |

This guide walks you through creating the 3 webhook URLs and pasting them into `deploy.sh`.

---

## 1. Pick a server

Webhooks can live in **any Discord server you control**. Your own personal server is fine; a team server is fine.

**Do not** put production alerts in a public server or a casual friends server — webhook URLs sitting in channel settings are a low-grade footgun if someone else has Manage Webhooks rights.

---

## 2. Create each webhook (repeat 3 times)

Do this once per channel — `theseus-briefing`, `theseus-alerts`, `b2b-leads`.

1. **Open** Discord and navigate to your server.
2. If the channel doesn't exist, **right-click** in the channel list → **Create Channel** → choose **Text** → name it (`theseus-briefing`, `theseus-alerts`, or `b2b-leads`).
3. **Right-click** the channel → **Edit Channel** (or hover the channel name and **click** the gear icon).
4. In the channel settings left sidebar, **click Integrations**.
5. **Click Webhooks** → **New Webhook**.
6. **Name** the webhook (e.g. `Theseus Briefing`). Customize the avatar if you want — purely cosmetic.
7. **Click Copy Webhook URL**.
8. **Paste** it somewhere safe — 1Password, or a scratch text file you'll delete right after deploy.
9. **Repeat** for the remaining 2 channels.

You should end up with 3 URLs of the form:

```
https://discord.com/api/webhooks/<id>/<token>
```

---

## 3. Treat webhook URLs as secrets

Webhook URLs **are write-tokens**. Anyone holding the URL can post in that channel as the webhook, with no further auth.

**Never** put them in:
- public git repos (or any git repo without `.gitignore` for `.env`)
- issue trackers / Jira / Linear tickets
- screenshots posted online
- public chat / Slack / Discord messages

Theseus stores them in `/opt/theseus/.env` with `chmod 600` so only the service user can read.

---

## 4. Paste into deploy

On the VPS, run:

```bash
bash ops/deploy.sh
```

It will prompt for each URL in order:

```
DISCORD_WEBHOOK_BRIEFING:
DISCORD_WEBHOOK_ALERTS:
DISCORD_WEBHOOK_B2B_LEADS:
```

Pasted URLs go **directly into `.env`** and are never echoed back to the terminal. After deploy completes, wipe whatever scratch file you pasted them into in Step 2.8.

---

## 5. Verify a webhook works (optional)

After deploy, from the VPS:

```bash
source /opt/theseus/.env
curl -X POST -H "Content-Type: application/json" \
  -d '{"content":"Theseus webhook test — please ignore"}' \
  "$DISCORD_WEBHOOK_BRIEFING"
```

Expected: **HTTP 204 No Content**, and the test message appears in `#theseus-briefing`. Repeat with `$DISCORD_WEBHOOK_ALERTS` and `$DISCORD_WEBHOOK_B2B_LEADS` to confirm all 3.

---

## 6. Mobile

The Discord mobile app has the same flow with fewer clicks: long-press the channel → **Edit Channel** → **Integrations** → **Webhooks** → **New Webhook** → **Copy Webhook URL**. You can do the whole setup from your phone if needed.

Sanity check: every legitimate Discord webhook URL is on the domain `discord.com/api/webhooks/<id>/<token>`. If you see anything else, it's not Discord — discard it.

---

## 7. Permissions

The account creating the webhook needs **Manage Webhooks** permission on the channel (or server-wide). Server owners have this by default. If you're using a team server you don't own, ask the owner to either grant you Manage Webhooks on these 3 channels or create the webhooks for you.

---

<sub>Accompanies `ops/deploy.sh`. Written 2026-05-20.</sub>
