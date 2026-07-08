# Setup — Gesamtpaket (alles übers Claude-Abo, keine API-Kosten)

## 1. Repo aufsetzen
    cd smartvelo-memory
    git init && git add -A && git commit -m "init memory"
    gh repo create smartvelo-memory --private --source=. --push

## 2. Claude Code verbinden (läuft mit deinem Claude-Login, kein API-Key)
    claude mcp add --transport http smartvelo https://ops-mcp.smart-velo.de/mcp
    claude mcp add --transport http microsoft365 https://microsoft365.mcp.claude.com/mcp

Nutzung: im Repo `claude` starten → "check-in" tippen.
Claude liest CLAUDE.md, zieht Live-Daten (Kalender/To-Dos/Mails/Teams),
aktualisiert STATUS.md + people/ + topics/ + journal/ und committet.

Optional lokal automatisieren (weiterhin Abo):
    # crontab -e  (Mac/Linux; Windows: Taskplaner)
    30 7 * * 1-5  cd $HOME/repos/smartvelo-memory && claude -p "check-in" >> $HOME/checkin.log 2>&1
    # Vorher einmal manuell testen; Permission-Verhalten je Claude-Code-Version prüfen.

## 3. Morgen-Briefing (Push in die Claude-App)
Scheduled Task in der App anlegen (werktags ~07:30), beide Connectoren aktivieren,
Prompt aus docs/scheduled-task-prompt.md einfügen. Fertig.

## 4. Arbeitsteilung
- Scheduled Task  = tägliches Briefing (Push, nur lesen)
- Claude Code     = Gedächtnis-/Panel-Pflege im Repo (STATUS.md = dein Panel)
- Claude.ai-Chat  = Adhoc-Arbeit mit MCP (Mails, PDFs, Recherche)

## 5. optional/api-briefing/
GitHub-Action-Variante des Briefings über die Anthropic API (kostet API-Guthaben).
NUR relevant, falls du das Briefing später serverseitig ohne App/Rechner willst. Aktuell ignorieren.
