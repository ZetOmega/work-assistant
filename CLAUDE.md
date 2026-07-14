# CLAUDE.md — smartvelo-memory

Persistentes Gedächtnis + Ops-Panel für **Philipp Klei** (IT/KI-Lead, smartvélo mobility GmbH, Köln).
Claude Code liest/aktualisiert diese Dateien, statt langen Chat-Kontext zu halten.

## Grundregeln
- Deutsch, knapp. Philipp schreibt kurz/direktiv → ausführen, nicht erklären. Bei Korrektur: anerkennen, weitermachen.
- **Source of Truth = dieses Repo.** Nach jeder Session betroffene Dateien patchen + committen
  (`checkin: YYYY-MM-DD` bzw. `update: <person|thema>`).
- **Keine Passwörter/Secrets im Klartext** — nur Verweis „im Passwortmanager“.
- Aktionen mit Außenwirkung (Mail senden, Teams posten, Termine ändern) **nur nach explizitem Go**.
- Nur Fakten festhalten; Vermutungen als solche markieren (`(unbestätigt)`).

## Fixwerte
- Domain: `vorname@smart-velo.com` · Zeitzone: Europe/Berlin
- Philipp: philipp@smart-velo.com · 0151 53409285
- Firma: smartvélo mobility GmbH · Venloer Str. 515 (+509), 50825 Köln · ~41 MA
- To-Do-Standardliste (Graph-ID):
  `AQMkADRjZWJmNzY5LTg4AGNhLTRlZmEtOGEyYS0yN2EwYzcwZmU1MTkALgAAA6R08GlsPYdLv4WCEQ32ZoMBAAZslv-uyBJMk_m5ZC2bXikAAAIBEgAAAA==`
- MCP-Server: `Microsoft-Controller-SMARTVELO` (https://ops-mcp.smart-velo.de/mcp) + `Microsoft 365` (https://microsoft365.mcp.claude.com/mcp)

## Graph-Gotchas (hart erarbeitet — nicht neu ausprobieren)
- **To-Do-Task PATCH direkt → 500** (Auto-`If-Match`). Immer `POST /$batch`,
  Sub-Requests mit `headers: {"Content-Type": "application/json"}`, **ohne** If-Match. Max. 20 Sub-Requests.
  429/Timeout → einfach wiederholen (idempotent).
- Outlook-Kategorien **seriell** anlegen (parallel → 409).
- Neue Mail-Entwürfe: `POST /me/messages` (kein Copy-Endpoint).
- Signatur-Bilder lassen sich per API nicht zuverlässig einbetten → manuell.
- Planner-PATCH braucht exakten ETag (dedizierte update/delete-Tools nutzen, falls vorhanden).
- **Zeiten sauber halten (UTC vs. CEST — hier schon vermischt worden)**: `list_calendar_events`/`graph_request`
  liefern Kalenderzeiten ohne „Z"-Suffix, sind aber **UTC** — immer **+2h für CEST** (Sommerzeit) umrechnen,
  bevor sie an Philipp oder ins Repo gehen. Mail-Timestamps (`received`/`sentDateTime`) haben ein explizites
  „Z" (UTC) und brauchen dieselbe Umrechnung. `outlook_find_available_time`s `nowDateTime` ist ebenfalls UTC
  mit „Z". Bei Zweifel: eine bekannte Alltagszeit im Kontext gegenprüfen (z. B. „Techniker kommt zwischen 8
  und 12 Uhr" vs. Rohwert) statt zu raten. Immer die Zeitzone dazuschreiben (z. B. „14:15 CEST"), nie nackte
  Uhrzeiten ohne Zone in STATUS.md/people/topics stehen lassen.

## Skill: check-in
Trigger: „check-in“, „new day“, „was steht an“, „take all in“.

1. **ZUERST echte Zeit holen**: `outlook_find_available_time` → `nowDateTime` ist autoritativ.
   Philipp nennt das Datum öfter falsch (mehrfach passiert) — alle relativen Angaben daran ankern.
2. Kalender nächste 7 Tage.
3. Offene To-Dos (`GET .../tasks?$top=100`, status != completed).
4. Inbox letzte ~5 Tage (aktionsbedürftig/unbeantwortet) · Sent letzte ~2 Tage (Erledigtes abgleichen) ·
   wichtige Teams-Chats, v. a. 1:1 Konrad.
5. Output an Philipp: korrigiertes Heute · Tages-/Wochenplan · geflaggte Mail-/Chat-Aktionen ·
   Vorschlag To-Do-Updates (erst nach Bestätigung anwenden, via $batch).
6. Danach Repo pflegen: `STATUS.md` regenerieren · betroffene `people/*.md` + `topics/*.md` patchen ·
   `journal/YYYY-MM-DD.md` schreiben · committen.

## Struktur
- `people/` — ein Dossier pro Person (Template siehe unten)
- `topics/` — ein File pro laufendem Thema
- `STATUS.md` — das Panel; wird bei jedem Check-in **komplett neu generiert**
- `journal/` — ein Kurzlog pro Tag (3–8 Zeilen)

### Person-Template
```
# Name
Rolle: · E-Mail: · Tel: · Status: aktiv|ausgeschieden|extern
## Kurzprofil
## Aktuelle Themen
## Letzte Aktionen   (immer mit Datum, neueste oben)
## Offen / wartet auf
## Notizen
```
