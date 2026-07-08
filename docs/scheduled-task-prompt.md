# Scheduled Task: Morgen-Briefing (Claude-App, werktags ~07:30)

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
