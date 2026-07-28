# KI für Arbeitsverträge (Anfrage Celine)  · Status: beantwortet 28.07.2026

## Anfrage
Celine, Teams 24.07 11:28: „welche KI ist am besten geeignet für Arbeitsverträge etc.?" —
auf Rückfrage: **DSGVO UND Qualität** („am liebsten beides").

## Antwort/Empfehlung (Philipp, 28.07 — Rev. 2)
**Copilot ist raus** (Philipp: Qualität zu schlecht). Zweistufig:

1. **Arbeitspferd = Claude Team** (haben wir schon im Haus, klar beste Qualität bei langen Vertragstexten).
   Rechtliche Basis: Anthropic stellt einen **DPA nach Art. 28 DSGVO** (= AVV) für Team/Enterprise/API,
   in die Commercial Terms integriert; Drittlandtransfer über **SCCs**.
   **Wichtige Einschränkung:** **kein EU-only-Processing im Standard** — echtes EU-Residency gäbe es nur über
   AWS Bedrock / Google Vertex in EU-Regionen. Zero Data Retention gilt für API/Claude Code, **nicht** fürs
   normale Team-Chat-Interface.
   → **Arbeitsregel daraus:** Vertragsarbeit mit **Platzhaltern** ([Name], [Gehalt], [Geburtsdatum]);
   echte Personendaten erst lokal in Word einsetzen. Damit ist der DSGVO-Punkt praktisch entschärft.

2. **Wenn HR echte Personendaten in die KI geben will** (Bestandsverträge prüfen o. Ä.) →
   **Mistral Le Chat Pro/Team** als HR-Werkzeug: Server in Paris, **AVV ohne SCC-/Drittlandthematik**,
   kein Training auf Pro/Business-Daten. Qualität für Vorlagenarbeit ausreichend, günstig.

3. **Klauselprüfung (ob es hält)** ist kein KI-Thema: einmalig **Mustervorlage anwaltlich** prüfen lassen,
   danach KI nur zum Befüllen/Vergleichen. Spezial-Tools (z. B. Beck-Noxtua, in DE gehostet) sind für ~41 MA
   überdimensioniert und teuer.

## Flankierend nötig
- AVV + Eintrag im Verzeichnis von Verarbeitungstätigkeiten; kurze KI-Nutzungsrichtlinie fürs Team.
- Beschäftigtendaten: § 26 BDSG. Falls ein Betriebsrat existiert *(bei smartvélo unbestätigt)*: Mitbestimmung § 87 BetrVG.
- **AI Act:** Vertragserstellung selbst ist **kein** Hochrisiko. Aber **ab 02.08.2026** greifen die Hochrisiko-Pflichten
  für HR-KI nach Anhang III Nr. 4 — **Bewerber-Screening, Leistungsbewertung, Beförderungs-/Kündigungsentscheidungen**.
  → Direkt relevant für das To-Do **„Recruiting via odoo"**: vor Aktivierung eines KI-Screenings prüfen.
- Kein Rechtsrat: Endfassung von Arbeitsverträgen gehört zur Fachanwalt-Arbeitsrecht-Prüfung (RDG).
