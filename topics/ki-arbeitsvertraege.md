# KI für Arbeitsverträge (Anfrage Celine)  · Status: beantwortet 28.07.2026

## Anfrage
Celine, Teams 24.07 11:28: „welche KI ist am besten geeignet für Arbeitsverträge etc.?" —
auf Rückfrage: **DSGVO UND Qualität** („am liebsten beides").

## Antwort/Empfehlung (Philipp, 28.07)
**Zweistufig, weil „eine KI für Arbeitsverträge" die falsche Frage ist:**

1. **Verträge aus eigener, anwaltlich geprüfter Vorlage befüllen/anpassen/glätten**
   → **Microsoft 365 Copilot im eigenen Tenant**. Daten bleiben in der EU Data Boundary, kein Modelltraining
   auf Kundendaten, AVV über die Microsoft Online Services Terms. Braucht Copilot-Lizenzen.
   Fallback ohne Copilot-Lizenz: **Claude Team/Enterprise** (kein Training auf Business-Daten, AVV verfügbar;
   US-Anbieter → SCC/DPF-Grundlage dokumentieren).
2. **Juristische Prüfung von Klauseln** (AGB-Kontrolle §§ 305 ff. BGB, Nachweisgesetz-Pflichtangaben,
   Befristung TzBfG, Verfall-/Wettbewerbsklauseln) → dafür ist kein Allzweck-Chatbot gut genug.
   Passendes Werkzeug wäre **Beck-Noxtua** (in Deutschland gehostet auf IONOS/Open Telekom Cloud,
   BSI C5 / ISO 27001 / ISO 42001, Word-Add-in) — auf Juristen ausgelegt, lizenzkostenintensiv.
   **Pragmatischer für ~41 MA:** einmalig eine Mustervorlage anwaltlich prüfen lassen, danach KI nur
   zum Befüllen/Vergleichen einsetzen.

**Hartes Nein:** private/kostenlose Consumer-Accounts mit echten Personendaten (Name, Gehalt, Geburtsdatum).
Wenn es schnell gehen muss: Platzhalter verwenden ([Name], [Gehalt]) und erst lokal einsetzen.

## Flankierend nötig
- AVV + Eintrag im Verzeichnis von Verarbeitungstätigkeiten; kurze KI-Nutzungsrichtlinie fürs Team.
- Beschäftigtendaten: § 26 BDSG. Falls ein Betriebsrat existiert *(bei smartvélo unbestätigt)*: Mitbestimmung § 87 BetrVG.
- **AI Act:** Vertragserstellung selbst ist **kein** Hochrisiko. Aber **ab 02.08.2026** greifen die Hochrisiko-Pflichten
  für HR-KI nach Anhang III Nr. 4 — **Bewerber-Screening, Leistungsbewertung, Beförderungs-/Kündigungsentscheidungen**.
  → Direkt relevant für das To-Do **„Recruiting via odoo"**: vor Aktivierung eines KI-Screenings prüfen.
- Kein Rechtsrat: Endfassung von Arbeitsverträgen gehört zur Fachanwalt-Arbeitsrecht-Prüfung (RDG).
