# Papaya (Service-/Ticketsystem)

Status: aktiv · Anbieter-Kontakt Engineering: Arianna

## Aktuelle Themen
- **Vertragslaufzeit / mögliche Kündigung** (neu 24.07): Papaya am 01.12.2024 scharf gestellt, Vertrag über **24 Monate** → Laufzeit bis ~30.11.2026, danach automatische Verlängerung (unbestätigt, genaue Kündigungsfrist prüfen). Konrad will das kündigen prüfen. Termin „Papaya Reminder – Vertragslaufzeit" war für Do 13.08 11:00–11:30 CEST angelegt.
  **⚠️ 06.08 13:21 CEST: Termin als „Declined" ins Postfach gelandet** — Kalendersuche (01.–20.08) findet den
  Termin nicht mehr, er scheint storniert/abgelehnt. Unklar, wer/warum abgelehnt hat *(unbestätigt)* — vor dem
  13.08 klären, sonst droht die Kündigungsfrist-Prüfung ganz zu verfallen.
- **API-Integration** (Arianna/Engineering): Feature-Request labels im Ticket-Update, undokumentierte Rate-Limits (404 statt 429), Kommentar-Historie ~450 Tickets. /comments-404 lag am fehlenden Header `Accept: application/json` → funktioniert inzwischen.
- **Papaya-IoT-Sync** (Robert): Sync-Skript (Papaya = source of truth) erst nach SUPLY-Bereinigung + Flink-Abgleich mit Eric; Nachfassen nach Philipps Urlaub (To-Do 31.08).

- **Sales Bikes in Papaya abbilden** (neu 27.07): Robert 12:32 — Bestand als **„Waren-Zuteilung" pro Sales Manager**
  in Papaya; Joshua Rippelmeier, Cagatay Oguz und Jurgen de Jonge sollen **aktiv auf Philipp zugehen**, die Entscheidung
  kommt von ihnen („ihr müsst die Infos jederzeit parat haben"). Jurgen 12:56: hält die vorgeschlagene Arbeitsweise für
  **„unmöglich"**, führt selbst eine Excel-Tabelle; **Bike-IDs (vier Standorte) hoffentlich Ende dieser Woche**.

- **Lösungsrichtung Philipp (28.07):** statt Papaya-Warenzuteilung vermutlich **Excel + Microsoft Planner**
  (Sales führt die Liste, Planner für Zuordnung/Status) — noch nicht mit Sales abgestimmt *(unbestätigt)*.

## Letzte Aktionen
- 27.07 — Sales-Bikes-Diskussion (Robert/Jurgen, Mail „Sales Bikes Papaya"); Entscheidung liegt bei Sales, Philipp technisch beratend.
- 27.07 — Konrad: Papaya-Kündigung „Montag mit reinnehmen"; separater Termin 13.08 im Kalender.
- 24.07 — Robert flaggt 24-Monats-Laufzeit ab 01.12.2024 (Mail „Papaya Laufzeit").
- 24.07 07:39 — Philipp an Arianna: /comments funktioniert (Accept-Header), Rate-Limit/Labels adressiert.
- 24.07 — Papaya-Weekly abgesagt, schriftlich geklärt.

## Kündigungsfrist-Termin verschoben (Korrektur 11.08)
Der Termin „Papaya Reminder – Vertragslaufzeit" (war Do 13.08 11:00–11:30 CEST) tauchte als „Declined" auf
(06.08) und fehlte im Kalender dieser Woche — **Klärung 11.08: Robert hat den Termin selbst bewusst weit
nach hinten verschoben** (neues Datum unbestätigt). Kein verlorener/verschollener Termin, kein akuter
Handlungsbedarf vor dem 13.08.

## 🆕 Axa-Ringschloss-Bruchanalyse (14.08) — Philipps eigenes To-Do
- **Eric Frey (13.08 12:16)** und **Lukas Laarmann (14.08 08:59)** fragen unabhängig, ob sich aus Papaya-
  Tickets (ausgetauschte Schlösser) auswerten lässt, wie häufig/aus welchem Grund Axa-Ringschlösser brechen
  (km-Laufzeit, Schadensbild). Philipp an Eric (14.08 07:26): „Klingt kompliziert, ich könnte aber mal
  gucken." — **noch nicht umgesetzt, kein Wartet-auf-Dritte, sondern Philipps eigene Aufgabe.**
- **Antwort an Lukas (14.08 11:59 CEST):** eventuell im KPI/OPS-Dashboard abbildbar, kostet aber erst Zeit/
  Analyse — die Tickets müssten den Schaden einheitlich benennen, tun sie aktuell nicht.

## Digitaler Zwilling (Ersatzteile/Bauteile je Bike-ID + IoT-Historie) — nicht in Planung (14.08)
Lukas fragte danach (14.08 08:59). Philipps Antwort: nicht in Planung, würde versuchen es von Papaya bauen
zu lassen („wir zahlen ja genug"), sonst frühestens mit dem ERP. Zeitaufwand für Eigenbau aktuell nicht
zu rechtfertigen.

## Offen / wartet auf
- Sales (Rippelmeier/Cagatay/Jurgen): Entscheidung, wie Sales-Bikes abgebildet werden + Bike-IDs (Ende KW 31).
- **Arianna: Rückmeldung Feature-Request (labels, Rate-Limits) + RW-API-Key** — ist ein „wartet auf", kein
  To-Do bei Philipp (Klarstellung 11.08).
- Neuer Termin von Robert für die Kündigungsfrist-Prüfung (Datum unbestätigt, nicht mehr dringend vor 13.08).
- Robert nach Urlaub: Papaya-IoT-Sync wieder aufnehmen — **erst relevant nach Philipps Urlaub (Mitte August),
  jetzt noch nicht dringend** (Klarstellung 11.08).

## Notizen
- Vertragsdaten unbestätigt aus Roberts Mail — vor Kündigungsentscheidung Originalvertrag prüfen.
