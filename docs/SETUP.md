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

## 3. Morgen-Briefing — verworfen (Stand 09.07.2026)
Kein Auto-Task mehr. Grund: die Art Check-in, die gebraucht wird (Repo-Kontext aus
people/topics mit Live-Kalender/Mail/Todos/Teams verbinden, Todos mit Begründung
schließen vorschlagen), braucht gleichzeitig Repo-Schreibzugriff UND den interaktiven
MCP-Login — das gibt es nur in einer Claude-Code-Session, die man selbst öffnet.
Automatisierte Trigger/Scheduled Tasks haben entweder kein Repo (App-Task) oder keinen
MCP-Zugriff (Cron/Routine, da Microsoft 365 interaktiv-authentifiziert ist — siehe
docs/scheduled-task-prompt.md für die Details der beiden gescheiterten Versuche).
→ Check-in läuft ausschließlich manuell: Claude Code öffnen, "check-in" tippen.

## 4. Arbeitsteilung
- Claude Code     = einziger Weg für den vollen Check-in (Repo + Live-MCP zusammen)
- Claude.ai-Chat  = Adhoc-Arbeit mit MCP (Mails, PDFs, Recherche), ohne Repo-Bezug

## 5. optional/api-briefing/
GitHub-Action-Variante des Briefings über die Anthropic API (kostet API-Guthaben) —
ungetestet, unbenutzt. Gleiche MCP-Einschränkung würde hier nicht greifen (eigener
Graph-Zugriff per Refresh-Token statt Connector), aber nicht aufgesetzt. Ignorieren.
