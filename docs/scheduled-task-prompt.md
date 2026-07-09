# Routine: Morgen-Check-in (werktags 08:00, an CC-Session gebunden)

Aktive Variante: Claude-Code-Routine `smartvelo-morning-checkin` (trig_01LZsSxPj2C99pYG7ScepbYk),
feuert in die persistente Session mit verbundenen MCPs (frische Sessions haben keine MCP-Auth!).

Prüfumfang — ALLES, keine Ausschnitte:
1. Echte Zeit zuerst (outlook_find_available_time, nowDateTime maßgeblich).
2. Kalender 7 Tage.
3. ALLE offenen To-Dos (Standardliste, $top=100, überfällige markieren).
4. ALLE Mails: Inbox seit gestern ~17 Uhr + Sent-Abgleich.
5. ALLE Teams-Chats mit neuen Nachrichten (1:1 UND Gruppen/Meetings), nicht nur Konrad.
6. Output: ☀️ Heute · Termine · Top-3 · To-Dos · Mail-/Chat-Aktionen · Blocker.
7. Repo pflegen: STATUS.md · people/ · topics/ · journal/ · commit + push.

Read-only nach außen: keine Mails/Nachrichten senden, keine Termine ändern.
To-Do-Änderungen nur nach Bestätigung.
