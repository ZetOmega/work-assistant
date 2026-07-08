# Morgen-Briefing — Setup (5 Min)

1. Diese zwei Dateien ins smartvelo-memory-Repo kopieren:
   .github/workflows/morning-checkin.yml
   scripts/morning_checkin.py

2. GitHub → Repo → Settings → Secrets and variables → Actions:
   ANTHROPIC_API_KEY    = <dein Anthropic API Key (console.anthropic.com)>
   SMARTVELO_MCP_TOKEN  = <Auth-Token für ops-mcp.smart-velo.de; leer/weglassen falls keins nötig>

3. Testen: GitHub → Actions → "Morning Check-in" → "Run workflow" (manuell).
   → Mail "☀️ Briefing …" landet bei philipp@smart-velo.com, STATUS.md + journal/ werden committet.

4. Zeitplan: cron "30 5 * * 1-5" = 07:30 CEST (Sommer) / 06:30 CET (Winter, dann auf "30 6" stellen).

Zustellkanal ändern: Statt Mail kann Claude auch per post_chat_message in einen Teams-Chat posten —
dazu im Prompt (scripts/morning_checkin.py, Schritt 6) send_mail durch post_chat_message + chat_id ersetzen.

Voraussetzung: ops-mcp.smart-velo.de muss von außen (GitHub-Runner) erreichbar sein und
serverseitig ein gültiges Microsoft-Token haben. Wenn der MCP nur mit deiner Claude.ai-Session
funktioniert, sag Bescheid — dann bauen wir die Variante, die Graph direkt per Refresh-Token anspricht.
