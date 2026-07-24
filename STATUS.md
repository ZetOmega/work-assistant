# STATUS — Stand Fr 24.07.2026, 08:46 Uhr CEST (alle Zeiten CEST)

## 🔥 Heute (Fr 24.07)
- **10:00–11:30 — Jobvalley.** Eric heute früh (05:30) via Teams: noch **keine finale Bestätigung von Calvin**, und Eric hat um 10 selbst „Ops Checkout" mit Konrad → **Eric ist NICHT dabei**. Vor Termin klären, ob er überhaupt stattfindet.
- **Papaya x SMARTVÉLO Weekly (11:30) — Philipp sieht keinen Sinn**, 30 Min verschwendet. Er beantwortet Ariannas Mail direkt schriftlich (Accept-Header + Beispiel-Requests) statt Meeting.

## ✅ Seit letztem Lauf geklärt / vorangekommen (seit Do 23.07 08:22)
- **greendevice/Pascal war 23.07 vor Ort** — „get to know" gelaufen. Pascal (Mail 23.07 14:24): **nächster Termin 06.08 11:00**, Mobilfunk läuft parallel. Celine bestätigt („passt prima"). → `topics/mobilfunk.md`.
- **Papaya-Engineering geantwortet** (Arianna, 23.07 18:27): (1) **Labels-Update per API aktuell nicht möglich** — Limitierung, Use-Case ans Team weitergegeben. (2) **Keine dokumentierten Rate-Limits** — Server ächzt evtl. an Volumen/Muster; Arianna bittet um Endpoints + Request-Rate + Beispiel-Requests. (3) **404 auf /comments** liegt vermutlich am fehlenden Header **`Accept: application/json`** (Pflicht für alle Requests) — bittet um Beispiel-Request. → Ball bei Philipp: Header prüfen + Beispiele liefern. To-Do „Papaya-API nachverfolgen".
- **Konrad-1:1 verschoben**: neuer Termin **Mo 27.07 13:15–13:30 CEST** (Teams, neue Einladung 23.07 akzeptiert) — nicht mehr 08:45.
- **Neuer Philipp x Eric**: **Mo 27.07 15:00–15:30 CEST** (Teams, akzeptiert 23.07).

## ⏳ Weiter offen (kein Fortschritt / weiter blockiert)
- **Claude-Abo BLOCKIERT (seit 21.07, 3 Tage)** — Teams mit Celine 23.07: Zahlung nun über **Konrads Karte** versucht, geht ebenfalls nicht („weißt du warum Konrads Karte nicht geht?"). Passkey + Sign-in-Links 23.07 → Philipp arbeitet aktiv daran, aber **kein funktionierender Bezahlweg**.
- **Terminkonflikt Mo 27.07 (Entscheidung):** Eric bleibt 15:00–15:30. OBS/Odoo 14:00–15:30 im Kalender ✅ — Philipp hofft auf kurzen Odoo-Termin (1 h reicht, endet ~15:00). Falls OBS überzieht → Überlappung mit Eric.
- **Impressum-/Website-Fehlerliste** (seit 22.07) — kein neuer Fortschritt; konsolidierte Liste an Lukas/Marketing weiter offen. → `topics/website.md`.
- **Hanisch — Telefon/Zugang NetCologne-Glasfaser** — nur Umfrage-Reminder von NetCologne (23.07), kein Zugang. To-Do offen (seit 22.07). → `topics/netcologne-netzwerk.md`.
- **Slack-Bot-Invite (Mathis)** — kein Fortschritt (nur Slack-Onboarding-Promo).
- **Papaya-IoT-Sync (Robert)** — erst nach SUPLY-Bereinigung + Flink-Abgleich; Nachfassen nach Urlaub (To-Do 31.08).

## 🆕/laufend
- **Hiring GEKLÄRT (24.07):** Konrad-Abstimmung erfolgt — Stelle wird auf den **KI-Engineer** zugeschnitten (greendevice übernimmt Geräteverwaltung/Support, daher kein Sysadmin-Fokus mehr). Profil „KI- & Automatisierungs-Engineer" gilt. → `topics/hiring.md`.
- **greendevice-Mobilfunk:** on-site erledigt, nächster Termin 06.08 11:00. → `topics/mobilfunk.md`.
- **To-Do „Lukas bom abhängigkeitsbuilder" (geklärt):** Lukas will langfristig einen **Bike-Konfigurator** bauen (komplex). Philipp baut ihm ein **Abhängigkeits-/Kompatibilitäts-Tool** (BOM): z. B. „Teil X gewählt → inkompatibel mit X, Y, Z, braucht aber A, B, C".
- **Cagatay Walk-in-Kaufinteressenten** — Kontakt weitergegeben, sie melden sich.
- **Azure Copilot-Agent-Access bis 01.08.2026 prüfen** · **MS Entra Passkeys/SMS-Voice-Abschaltung 01.02.2027** — informativ, IT. → `it-security.md`.
- Philipp: **Mitte August 2 Wochen Urlaub**.

## 🟡 Ich (Philipp) — Microsoft To-Do (10 offen; KEINE überfällig)
- [ ] Kompatibilitäts-/Abhängigkeits-Tool für Lukas' Bike-Konfigurator bauen (Titel + Notiz präzisiert 24.07)
- [ ] Jokubas anrufen — fällig **30.07**. Hängt an Website-/Impressum-Fixes.
- [ ] Papaya-API: Feature-Request — Antwort nachverfolgen (**Arianna hat geantwortet → jetzt Beispiele + Accept-Header liefern**)
- [ ] KPI-Brainstorm mit Eric terminieren — evtl. = Philipp x Eric Mo 27.07 15:00 (aber Konflikt OBS)
- [ ] Hanisch: Telefon/Zugang Glasfaserausbau NetCologne
- [ ] Slack-Bot in fleet-notifications einladen (via Mathis) — wird vorher verbessert
- [ ] Showroom-Bike-Steckbrief erstellen — sidelined
- [ ] Robert nach Urlaub nachfassen (Papaya-IoT-Sync) — fällig 31.08
- [ ] SharePoint-Restrukturierung: Ideen sammeln — fällig 30.08
- [ ] Wissensdatenbank/Video-Anleitung für Service — fällig 29.11

## 🔵 Extern / wartet auf andere
- [ ] Arianna/Papaya → jetzt Ball bei Philipp (Beispiel-Requests + Accept-Header); RW-API-Key weiter offen
- [ ] Claude-Abo: funktionierender Bezahlweg — beide Karten + Konrads Karte abgelehnt
- [ ] Mathis → Slack-Channel-Freigabe für Bot-Invite (nach Bot-Verbesserung)
- [ ] Eric → SUPLY-Bereinigung + Flink-Abgleich (Voraussetzung für Papaya-Sync-Skript)

## 📅 Nächste Termine (alle CEST, aus Kalender 24.07 08:46)
- Fr 24.07 · 10:00–11:30 Jobvalley (Eric raus, Calvin-Bestätigung offen) · 11:30–12:00 Papaya x SMARTVÉLO Weekly (Teams)
- Mo 27.07 · 12:30–12:45 Weekly x Büro Köln (Venloer Str. 515) · 13:15–13:30 Konrad x Philipp (Teams) · **14:00–15:30 OBS/Odoo-Verhandlung (Carina Schuch, Teams) — im Kalender ✅** · 15:00–15:30 Philipp x Eric (Teams) ⚠️ **überschneidet OBS**

## ✅ Zuletzt erledigt
- OBS-Termin in Kalender eingetragen (24.07) · Hiring mit Konrad geklärt → KI-Engineer (24.07) ·
  Eric-Hubs-Dashboard-Cleanup durch (bestätigt 24.07) · greendevice on-site „get to know" (23.07) ·
  OBS/Odoo-Termin-Uhrzeit bestätigt (23.07) · FordPro-Zugang läuft (22.07) · Metabase-Zugang an Eric (21.07)

## ⚠️ Blinde Flecken
- Jobvalley-Termin 10:00: findet er statt? (Calvin-Bestätigung offen, Eric raus).
- Terminkonflikt Mo 27.07: Eric bleibt; hängt daran, ob OBS in 1 h (bis ~15:00) durch ist.
- Impressum-Fehlerliste: Status/Umfang weiter unklar — konsolidierte Liste raus an Lukas/Marketing?
- Ergebnis 1:1 Konrad (Mo 20.07) weiter nicht belegt (Call).
