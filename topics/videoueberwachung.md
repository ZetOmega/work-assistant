# Videoüberwachung Venloer Str. (Eingänge + Garten)  · Status: aktiv (aufgenommen 29.07.2026)

## Stand
- **Bestand: 2x Reolink TrackMix WiFi** (4K PTZ, Wi-Fi 6, Dual-Objektiv, Auto-Tracking) — an den **beiden Eingängen**.
  Dort unproblematisch: feste Blickrichtung, Zugangskontrolle, Tracking sogar sinnvoll.
- **Konrads Idee (28.07 18:01, Teams): dritte Kamera für den Garten.** Garten = **Lagerstandort für Bikes** *und*
  **Outdoor Community Area** (Mittagessen etc.), zusätzlich ein **Durchgangsbereich** im Bild.
  → **3. Kamera wird gesucht.**
- In den Arbeitsverträgen steht **nichts zu Videoüberwachung** (Philipp, 29.07).

## Bewertung (Philipp/Claude 29.07) — kein Rechtsrat
- **Trägt**: Bike-Lager mit hohem Sachwert = berechtigtes Interesse (Art. 6 Abs. 1 f DSGVO), Diebstahlschutz.
- **Trägt nicht**: Der **Pausen-/Essbereich** im selben Garten. Pausenbereiche gelten bei Aufsichtsbehörden/BAG
  praktisch als tabu — Beschäftigte müssen dort unbeobachtet sein. Das ist der Punkt, an dem die Abwägung kippt.
- **Durchgangsbereich** ist das kleinere Problem (flüchtige Erfassung, kein Pausenbereich) — **solange die
  Zweckbindung sitzt**. Wenn Aufnahmen je für Kommen/Gehen genutzt werden, ist die Anlage angreifbar.
- **Kein Ton** — Mitschneiden von Gesprächen ist § 201 StGB, kein Abwägungsthema.
- Vertragsklausel wäre wirkungslos: Grundlage ist berechtigtes Interesse + Information, nicht der Vertrag.

## Technische Auflösung: dynamische Privacy Mask
- **Statische** Maske (TrackMix) klebt an Bildkoordinaten → wandert beim PTZ-Schwenk mit und deckt den falschen
  Bereich ab. Für einen frei schwenkbaren Garten-View **unbrauchbar**.
- **Dynamische** Maske hängt an der Szene und bleibt beim Schwenken/Zoomen auf dem Bereich. Laut Reolink-Support
  nur bei **RLC-823S1, RLC-823S1W, RLC-823S2** — und **nur via Reolink App/Web-UI**, NICHT über NVR/Desktop-Client
  (dort bleibt sie statisch).
- **Reolink „Privacy Mode"** (Aufzeichnung + Live-Bild zusammen aus, planbar) ist laut Support der **E1-Serie
  (Indoor)** vorbehalten → **für Outdoor-PTZ keine Option**. Erste Annahme dazu war falsch.
- **Zeitfenster-Idee (nur außerhalb Arbeitszeit aufzeichnen)**: guter Hebel, aber Live-Ansicht muss mit
  abgeschaltet sein, und „Arbeitszeit" ist bei Außendienst/Spätdienst kein Block → Fenster großzügig legen.
  Mit dynamischer Maske ist das nur noch Zusatzabsicherung statt einziger Schutz.

## Modellentscheidung: RLC-823S1W (entschieden 29.07, Philipp)
- **RLC-823S1W** — 4K, 360°/90°, Wi-Fi 6 Dual-Band, 5x Zoom, **dynamische Privacy Mask**. Abgekündigt,
  nur Restbestände → **jetzt kaufen, solange lieferbar**. Bei einer Einzelkamera vertretbares Risiko
  (Ersatzteile gibt es bei Consumer-Kameras ohnehin nicht, im Defektfall wird komplett getauscht).
- **Dritte TrackMix verworfen**: kann nur die statische Maske, die beim PTZ-Schwenk mitwandert und den
  falschen Bereich abdeckt. Philipp 29.07: **auf Firmware-Versprechen wird nicht gewartet** („wir kaufen
  keine Versprechen") → Reolink-Ticket entfällt, Entscheidung auf Basis des heute verfügbaren Funktionsumfangs.
- **RLC-823S2** (16x Zoom) verworfen: **PoE only**. WLAN am Standort ist laut Philipp „1a, direkt neben AP".
- **Hofmaß korrigiert (Philipp 29.07): Hof ist eher ~50 m lang**, nicht 10–20 m. Philipp bleibt bei der W.
  → **Bedingung: Kamera nah am Bike-Lager montieren.** Dann ist die Distanz zum Schutzobjekt klein und 5x reicht.
  4K/5x auf 50 m liefert **Detektion** („da bewegt sich was"), aber **keine verwertbare Identifikation**
  (Gesicht/Kennzeichen). Falls die Kamera doch als Rundumblick für den ganzen Hof gedacht ist,
  **Entscheidung neu aufmachen** → dann 823S2 + PoE.
- Funktionaler Unterschied 823S1W ↔ 823S2 ist **allein der Zoom** (5x vs. 16x); 4K, PTZ-Bereich, dynamische
  Maske, Auto-Tracking, Erkennung, Spotlight, Sirene, 512 GB microSD, IP66 sind identisch.

## Anforderungen beim Einrichten (Checkliste)
- [ ] Dynamische Maske über **App/Web-UI** setzen, für **beide Objektive** (Weitwinkel + Tele) prüfen
- [ ] **Auto-Tracking + Auto-Zoom AUS** — sonst schwenkt die Kamera Beschäftigten nach (eingriffsintensivste Variante)
- [ ] Maske in einer **echten Aufzeichnung** gegenprüfen, nicht nur im Live-Bild
- [ ] **Kein Ton** / Mikrofon deaktivieren
- [ ] Hinweisschilder vor dem erfassten Bereich (Art. 13) + Beschäftigteninformation
- [ ] **Zweckbindung schriftlich**: nur Einbruch/Diebstahl, ausdrücklich KEINE Anwesenheits-, Arbeitszeit-
      oder Verhaltenskontrolle
- [ ] Löschfrist automatisch, 48–72 h; Ereignisclips per Bewegungstrigger statt Dauerlauf
- [ ] Zugriffskonzept: max. 2 benannte Personen, PTZ-Rechte begrenzt, Zugriffe protokolliert
- [ ] Eintrag ins Verarbeitungsverzeichnis; **DSFA** für den Beschäftigtenbereich ratsam
- [ ] **Betriebsrat?** Falls vorhanden: Mitbestimmung nach § 87 Abs. 1 Nr. 6 BetrVG **zwingend** — die
      *Eignung* zur Überwachung genügt, unabhängig von Zeitfenster und Maske
- [ ] Von eurem Datenschutzbeauftragten abzeichnen lassen (DSFA + BetrVG)

## Alternative, die zuerst geprüft werden sollte
Gegen Bike-Diebstahl: **IoT-Tracker/Ortung (läuft schon über Papaya)** + abschließbare Bikeboxen +
Bewegungslicht. Oft wirksamer als eine Kamera und komplett unproblematisch. Kamera als Ergänzung, nicht
als erste Maßnahme.

## Offen / wartet auf
- **RLC-823S1W bestellen** (Restbestände, Verfügbarkeit prüfen) — **Go von Konrad nötig, einzige Option** (180-€-Variante ist mit dem DSGVO-Nachtrag vom Tisch)
- **Produktlink an Celine schicken** (Konrad 29.07 08:22 „link kannst du celine schicken" — bezieht sich auf diese Kamera) — hängt am Go
- 12-V-Netzteil/Steckdose am Kamerastandort im Garten sicherstellen (WLAN ist da, Strom braucht sie trotzdem)
- Betriebsrat-Frage klären

## Verlauf Konrad-Abstimmung (29.07)
- 07:55 Philipp: **„180 € ca"** (Preis auf Konrads Frage vom 28.07 18:01).
- 08:01 Konrad: „Reicht eine für den Garten ja oder" → 08:02 Philipp: ja, PTZ rotiert, Blindspot nur bei starrer
  Montage; je nach Montagepunkt ggf. **Kabelverlängerungen** von Reolink nötig.
- 08:08 Konrad: **„Ja lass uns das machen bei dem Preis, das ist gut dann haben wir den Garten auch."**
  → Go, **bezogen auf 180 €**.
- 08:40 Philipp: DSGVO-Nachtrag — Kamera darf **nicht auf Pausenbereich/Terrasse** zeigen; Alternative ist die
  **teurere Kamera für 250 €** (mehr Funktionen, kann den Pausenbereich ausblenden und den Rest anlassen).
- **→ Konrad hat auf die 250 € nicht geantwortet. Go für die RLC-823S1W fehlt, Bestellung hängt (Stand 30.07).**
