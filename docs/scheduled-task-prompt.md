# Auto-Task — GELÖST & LIVE (Update 20.07.2026)

**Läuft jetzt.** In **Cowork mode** ist der frühere Blocker weg: die Umgebung hat gleichzeitig
Repo-Zugriff (smartvelo-orchestrator gemountet) UND die Microsoft-365-Connector. Damit ist der
vollständige Check-in als Scheduled Task möglich.

- Task-ID: `morning-briefing` · Schedule: **Mo–Fr 07:30 CEST** (System-Jitter ~+8 Min.)
- Ablauf: echte Zeit holen → Repo lesen → Kalender/Mail/Sent/Teams scannen → Diff →
  `STATUS.md`/`people`/`topics`/`journal` patchen + committen → Briefing mit Confirmations.
- Grenze: Repo-Schreiben auto; Außenwirkung (To-Do schließen/anlegen, Mail, Teams, Termine)
  nur als Vorschlag, Anwendung erst nach Philipps Go.
- Bei zugeklapptem Laptop um 07:30: Lauf holt beim nächsten App-Öffnen nach.
- Verwaltung: Sidebar „Scheduled". Tipp: einmal „Run now" für Connector-Freigaben.

---

## Historie: verworfen (Stand 09.07.2026)

Komplett aufgegeben, kein Scheduled Task, keine Claude-Code-Routine. Grund: der gewünschte
Check-in (Repo-Kontext aus people/topics mit Live-Kalender/Mail/Todos/Teams verbinden, Todos
mit Begründung schließen vorschlagen) braucht Repo-Zugriff UND interaktiven MCP-Login
gleichzeitig — das gibt es nur in einer selbst geöffneten Claude-Code-Session.

Getestet und beide verworfen:
- **Claude-Code-Routine/Trigger** (08.–09.07.2026): headless/Cron hat keinen Zugriff auf
  Microsoft 365 (interaktiv-authentifizierter Anthropic-Connector) — strukturelle
  Einschränkung, kein Einstellungsproblem. Zusätzlich hatte der frische Container auch kein
  Repo (kein .git, kein origin) — zweites, unabhängiges Blocker-Problem.
- **Scheduled Task in der Claude-App**: hat zwar Connector-Zugriff, aber keinen
  Repo-Zugriff (claude.ai-Chats haben kein Git/Dateisystem) → könnte nur ein oberflächliches
  Live-Briefing ohne Dossier-Kontext liefern, nicht den eigentlich gewünschten Abgleich.

→ Check-in läuft ausschließlich manuell hier in Claude Code: Session öffnen, "check-in" sagen.
