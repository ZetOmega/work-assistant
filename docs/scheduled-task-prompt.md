# Scheduled Task: Morgen-Briefing (Claude-App, werktags ~08:00)

**Warum nicht Claude-Code-Routine/Trigger:** Getestet (08.–09.07.2026) und verworfen.
Microsoft 365 ist der first-party-Anthropic-Connector mit interaktivem Claude-Login (OAuth) —
headless/Cron-Trigger haben grundsätzlich keinen Zugriff auf interaktiv-authentifizierte
Connectoren. Zwei Fixversuche (Session-Binding, Repo-Checkout-Fallback) haben das nicht
umgangen, weil es keine Einstellung ist, sondern eine strukturelle Einschränkung.
`Microsoft-Controller-SMARTVELO` (eigener MCP-Server, eigenes Auth) wäre davon nicht betroffen,
aber ohne Microsoft 365 fehlen Kalender/Mail/Teams sowieso.

**Der funktionierende Weg:** Scheduled Task in der Claude-App selbst (nicht Claude Code) —
die App verwaltet den Connector-Login selbst und nimmt ihn in geplante Tasks mit.

Beim Anlegen des geplanten Tasks BEIDE Connectoren aktivieren
(Microsoft 365 + Microsoft-Controller-SMARTVELO).
Der Task startet ohne Chat-Kontext — dieser Prompt ist deshalb self-contained.

--- PROMPT (ab hier kopieren) ---

Morgen-Check-in smartvélo (Philipp Klei, philipp@smart-velo.com):

1. Hole ZUERST die echte Zeit: outlook_find_available_time → nowDateTime ist maßgeblich, nichts annehmen.
2. Kalender heute + morgen (list_calendar_events, days=2).
3. Offene To-Dos: graph_request GET
   /me/todo/lists/AQMkADRjZWJmNzY5LTg4AGNhLTRlZmEtOGEyYS0yN2EwYzcwZmU1MTkALgAAA6R08GlsPYdLv4WCEQ32ZoMBAAZslv-uyBJMk_m5ZC2bXikAAAIBEgAAAA==/tasks?$top=100
   → nur status ≠ completed, überfällige markieren.
4. list_recent_mail (15) → nur aktionsbedürftige Mails seit gestern ~17 Uhr.
5. Teams-1:1 mit Konrad Essers auf neue Nachrichten prüfen.

Ausgabe kurz & locker (Du-Form):
☀️ Heute (Datum) · Termine mit Uhrzeit · Top-3-Prioritäten · fällige/überfällige To-Dos ·
Mails/Chats mit Handlungsbedarf · Blocker (wer schuldet was).

Wichtig: KEINE To-Do-Änderungen, keine Mails/Nachrichten senden — nur lesen und berichten.

--- ENDE PROMPT ---

**Einschränkung ggü. Claude-Code-Check-in:** Der App-Task hat keinen Repo-Zugriff — er kann
nur das Briefing schicken, nicht STATUS.md/people/journal pflegen. Repo-Pflege bleibt beim
"check-in" hier in Claude Code (manuell anstoßen oder Philipp meldet sich nach dem Briefing).
