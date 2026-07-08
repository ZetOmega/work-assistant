"""
Morgen-Briefing für Philipp.
Ein API-Call an Claude mit MCP-Connector auf den SMARTVELO-Controller:
Claude zieht Kalender/To-Dos/Mails selbst, schickt das Briefing per send_mail
und liefert eine aktualisierte STATUS.md zurück, die hier ins Repo geschrieben wird.

Benötigte Secrets (GitHub → Settings → Secrets → Actions):
  ANTHROPIC_API_KEY     – Anthropic API Key
  SMARTVELO_MCP_TOKEN   – Auth-Token für ops-mcp.smart-velo.de (leer lassen, falls keins nötig)
"""
import os, re, datetime, pathlib, requests

API_KEY = os.environ["ANTHROPIC_API_KEY"]
MCP_URL = "https://ops-mcp.smart-velo.de/mcp"
MCP_TOKEN = os.environ.get("SMARTVELO_MCP_TOKEN", "").strip()

ROOT = pathlib.Path(__file__).resolve().parents[1]
status_md = (ROOT / "STATUS.md").read_text(encoding="utf-8") if (ROOT / "STATUS.md").exists() else "(leer)"
claude_md = (ROOT / "CLAUDE.md").read_text(encoding="utf-8") if (ROOT / "CLAUDE.md").exists() else ""

PROMPT = f"""Du bist Philipps Morgen-Briefing-Agent bei smartvélo (Regeln/Fixwerte siehe CLAUDE.md-Auszug unten).

Führe JETZT den Check-in aus:
1. Hole zuerst das echte Heute-Datum aus den Tool-Daten (z. B. list_calendar_events) — nichts annehmen.
2. list_calendar_events (days=2) → heutige (und morgige) Termine.
3. graph_request GET /me/todo/lists/<LISTEN-ID aus CLAUDE.md>/tasks?$top=100 → offene Aufgaben (status != completed); überfällige markieren.
4. list_recent_mail (count=15) → neue Mails seit gestern ~17:00, nur aktionsbedürftige nennen.
5. Schreibe ein knappes deutsches Morgen-Briefing (Du-Form, locker, keine Floskeln):
   ☀️ Heute (Datum) · Termine mit Uhrzeit · Top-3-Prioritäten · fällige/überfällige To-Dos ·
   Mails, die Reaktion brauchen · Blocker („wartet auf …", aus STATUS unten).
6. SENDE es via send_mail an philipp@smart-velo.com, Betreff: "☀️ Briefing <TT.MM.>". Einfaches HTML (b, br, ul, li).
7. Gib am Ende deiner Antwort eine AKTUALISIERTE STATUS.md aus, exakt zwischen den Markern <STATUS> und </STATUS>
   (gleiche Struktur wie unten; Erledigtes abhaken/verschieben, neue Punkte aus Mails/Kalender einarbeiten, Datum in der Überschrift aktualisieren).

--- CLAUDE.md (Auszug) ---
{claude_md[:6000]}

--- Aktuelle STATUS.md ---
{status_md[:6000]}
"""

server = {"type": "url", "url": MCP_URL, "name": "smartvelo"}
if MCP_TOKEN:
    server["authorization_token"] = MCP_TOKEN

resp = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "anthropic-beta": "mcp-client-2025-04-04",
        "content-type": "application/json",
    },
    json={
        "model": "claude-sonnet-4-6",
        "max_tokens": 4000,
        "messages": [{"role": "user", "content": PROMPT}],
        "mcp_servers": [server],
    },
    timeout=600,
)
resp.raise_for_status()
data = resp.json()
text = "\n".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
print(text[:3000])

m = re.search(r"<STATUS>(.*?)</STATUS>", text, re.S)
if m:
    (ROOT / "STATUS.md").write_text(m.group(1).strip() + "\n", encoding="utf-8")
    print("\n[ok] STATUS.md aktualisiert")
else:
    print("\n[warn] Keine <STATUS>-Marker gefunden — STATUS.md unverändert")

today = datetime.date.today().isoformat()
jdir = ROOT / "journal"
jdir.mkdir(exist_ok=True)
jfile = jdir / f"{today}.md"
entry = f"\n- Morgen-Briefing automatisch versendet ({datetime.datetime.now().strftime('%H:%M')} UTC)."
if jfile.exists():
    jfile.write_text(jfile.read_text(encoding="utf-8").rstrip() + entry + "\n", encoding="utf-8")
else:
    jfile.write_text(f"# {today}{entry}\n", encoding="utf-8")
print("[ok] Journal geschrieben")
