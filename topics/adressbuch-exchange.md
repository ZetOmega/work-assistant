# Adressbuch-Tool & Exchange-Aufräumen · Status: 🆕 live, ein paar offene Punkte (Stand 12.08.2026)

## Adressbuch (live)
- **https://tools.smartvelo-mobility.com/adressbuch** — Team-Kontakte (Name, Rolle, Abteilung, Standort,
  Telefon, vCard-Download) + Funktionsmailadressen mit Zuständigen.
- **Pflege ausschließlich über `portal/adressbuch.json`** im Repo `SMARTVELO/tools-portal`
  (Branch `mailadressen-page`, PR #1) → Datei bearbeiten, auf den VPS nach
  `/opt/stacks/status/tools-site/` kopieren, fertig.

## Exchange (smart-velo.com) — Aufräumen 12.08
- **admin@ + support@ sind jetzt Shared Mailboxes**, Philipp als Owner (FullAccess + SendAs). **support@ ist
  ein neues, leeres Postfach** — die alte Support-Historie liegt weiter in admin@.
- **Gelöscht:** `krank@smart-velo.de` (war Alias auf Henry), Verteiler `mobilitygmbh@` + `servicegmbh@`
  (letzterer hatte 0 Mitglieder), Tippfehler-Aliase `protoype-alert@`, `catagay@`.
- **Ergänzt:** `sales@smart-velo.de` als Alias.
- **49 Benutzerprofile** mit Rolle/Abteilung/Firma aus Personio befüllt.
- ⚠️ **Telefonnummern lassen sich über Exchange NICHT ins Verzeichnis schreiben** (Microsoft blockt das für
  Benutzerpostfächer) — Nummern stehen nur im Adressbuch, nicht im Exchange-Verzeichnis.

## Inaktiv gesetzt (ausgeblendet, im Backend erhalten)
Alexander Wessels, Christian Müller, Fiona Honervogt, Hans Härtel, Michael Jacoby, Tom Tries,
Paula Fronhoff, Katharina Hahn.

**Nummer-Übergaben:** Fionas Nummer → Jakob Volksdorf. Katharinas Nummer → Simon Schröder.

## Kontakte sortiert
`~/Downloads/kontakte-sortiert/` bei Philipp — `smartvelo.vcf` (Team) und `extern.vcf` (Steuerbüro, Anwalt,
Spedition etc.).

## Offen / wartet auf

### Funktionspostfächer ohne Zuständigen
`einkauf@` · `order@` · `retoure@` · `service@` · `tpm@` · `production@` — im Adressbuch als „–" markiert.
**`einkauf@` war Katharina, die ist raus. Wer übernimmt?** Sonst laufen dort Mails unbeaufsichtigt ein.

### Personen im Adressbuch ohne Rolle
**Cosma, Lotte Essers, Rosa** — kein Titel in Personio/Entra, Status unklar (aktiv oder Altkonto?).

### Falls während des Urlaubs was reinkommt
Adressbuch-Änderung nötig → `adressbuch.json` bearbeiten (s.o.) oder bis nach dem Urlaub sammeln.
