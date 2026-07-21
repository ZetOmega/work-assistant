# Flink-Uptime-System + Eskalationstool (Tooling)  · Status: aktiv — live seit 21.07

Selbstgebautes Toolset rund um Flink-Service (Claude-Session 21.07). Abgrenzung: `flink-service.md` =
SLA-Datenpaket/Rückanalyse (Vertrag/Daten); dieses File = die gebaute Software drumherum.

## Stand 21.07 16:30 (aus TODO-Sammelmail)
- **Live:** Eskalationstool voll-live · Flink-Dashboard (Metabase „Flink Uptime", 11 Cards) · Slack-Pipeline scharf.
- Referenzen: `docs/PLAN-FLINK-SLACKBOT.md`, `docs/PAPAYA-FEATURE-REQUEST.md`.

## 👤 Philipps Aktionen
Offen (als Microsoft-To-Do angelegt 21.07):
1. **Mathis: Slack-Invite freischalten** — beide `#fleet-notifications-*`-Channels: Mathis öffnet kurz „Wer darf Personen hinzufügen", Philipp tippt `/invite @smartvelo-fleet-reader`, Mathis stellt zurück. Danach autom. Backfill ab Mo 13.07 (KW29) + Live-Push. Fallbacks: Plan B (User-Token, 15 Min) / Plan C (Flink hostet App selbst).
2. **Eric: Ersatzteil-Sheet einfordern** + mit `sheetreader@smartvelo-tools.iam.gserviceaccount.com` (Betrachter) teilen → schaltet Stufe-3-Ursachenanalyse + Bestelllisten-Verknüpfung frei.
3. **KPI-Brainstorm mit Eric** terminieren (nicht Robert — Korrektur 21.07) — bis dahin Personen-Auswertungen (Mechaniker-Scores) bewusst gesperrt, nur Hub-Ebene.

Erledigt (21.07):
- ✅ Eric hat Metabase-Zugang bereits.
- ✅ Bot-Profilbild hochgeladen.
- ✅ Papaya-Feature-Request-Mail ist raus (Entwurf war `docs/PAPAYA-FEATURE-REQUEST.md`) → Antwort abwarten.

## ⏳ Wartet auf Externe / Daten
- Nach Channel-Invite: Parser-Feinschliff an echten Fleet-Messages (Hub-Erkennung aus @-Mentions; evtl. Zusatz-Scope `users:read`).
- Flink-Historie wächst täglich (Sheet-Import 10:00) — Streak-/Trend-Cards ab ~1 Woche aussagekräftig.

## 📋 Backlog (bewusst geparkt)
- Reopen-30-Tage-Regel im Eskalationstool.
- Label-Langzeitschäden / Label-Wildwuchs-Detection-Card (Papaya-API nimmt keine Label-Writes → nur Read-Auswertung).
- Odoo-Anbindung Bestelllisten (langfristig, ersetzt Ersatzteil-Sheet).

## 🤖 Automatik (läuft unbeaufsichtigt)
- Morgen (22.07) 07:00 CEST: erster voll-live Eskalations-Sweep.
- Slack-Reconciliation alle 30 Min + Events-Push laufen bereits.
