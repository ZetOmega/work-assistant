#!/usr/bin/env python3
"""eSIM porting guide mailer.

Creates one deferred draft per colleague in support@smart-velo.com Drafts:
German guide mail + their Telekom eSIM letter PDF, held until 7 days before
their port date, 09:00 Europe/Berlin. Python 3 stdlib only.

Run order: --dry-run  ->  --create-drafts  ->  --list.
Phase B (--send) only on owner go.
"""
import argparse
import base64
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEDULE_FILE = os.path.join(HERE, "schedule.json")
TEMPLATE_FILE = os.path.join(HERE, "template.html")
STATE_FILE = os.path.join(HERE, "drafts-state.json")

TENANT = os.environ.get("GRAPH_TENANT_ID", "5441b1fd-fc35-494e-bcf5-2aa118ebc72a")
CLIENT = os.environ.get("GRAPH_CLIENT_ID", "f3e5f261-a399-4537-a07c-7854c211dfca")
GRAPH = "https://graph.microsoft.com/v1.0"
SCOPE = "https://graph.microsoft.com/.default"

DEFER_PROP_ID = "SystemTime 0x3FEF"          # PidTagDeferredSendTime
DEFER_PROP_TAG = "0x3fef"                    # Graph echoes the id lowercased
SUBJECT_PREFIX = "Deine neue Telekom-eSIM"

OP_TOKEN_FILE = os.path.expanduser("~/.config/op/sa-token.ai")
OP_SECRET_REF = "op://IT/Microsoft MCP Secret/Value"


class GraphError(RuntimeError):
    pass


# ---------------------------------------------------------------- schedule --

def load_schedule():
    with open(SCHEDULE_FILE, encoding="utf-8") as fh:
        return json.load(fh)


def load_template():
    with open(TEMPLATE_FILE, encoding="utf-8") as fh:
        return fh.read()


def de_date(iso):
    """2026-09-11 -> 11.09.2026"""
    return datetime.strptime(iso, "%Y-%m-%d").strftime("%d.%m.%Y")


def send_times(sched, rec):
    """-> (local datetime Europe/Berlin, utc datetime)"""
    tz = ZoneInfo(sched["tz"])
    hh, mm = (int(x) for x in sched["send_time_local"].split(":"))
    port = datetime.strptime(rec["portdatum"], "%Y-%m-%d").date()
    day = port - timedelta(days=int(sched["days_before"]))
    local = datetime(day.year, day.month, day.day, hh, mm, tzinfo=tz)
    return local, local.astimezone(ZoneInfo("UTC"))


def utc_z(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def subject_for(sched, rec):
    return (sched["subject"]
            .replace("{nummer}", rec["nummer"])
            .replace("{portdatum}", de_date(rec["portdatum"])))


def render(tpl, rec):
    return (tpl
            .replace("{vorname}", rec["vorname"])
            .replace("{nummer}", rec["nummer"])
            .replace("{portdatum}", de_date(rec["portdatum"])))


def attachment_name(rec):
    """0151 53415127 + 2026-09-11 -> Telekom-eSIM_0151-53415127_Portierung-2026-09-11.pdf"""
    nummer = "-".join(rec["nummer"].split())
    return f"Telekom-eSIM_{nummer}_Portierung-{rec['portdatum']}.pdf"


def pdf_path(sched, rec):
    return os.path.join(sched["pdf_dir"], rec["pdf"])


def pick(sched, only):
    recs = sched["recipients"]
    if not only:
        return recs
    wanted = {m.lower() for m in only}
    out = [r for r in recs if r["mail"].lower() in wanted]
    missing = wanted - {r["mail"].lower() for r in out}
    if missing:
        raise SystemExit("unknown --only address(es): " + ", ".join(sorted(missing)))
    return out


# -------------------------------------------------------------------- auth --

def get_secret():
    env_secret = os.environ.get("GRAPH_CLIENT_SECRET")
    if env_secret:
        return env_secret.strip()
    try:
        with open(OP_TOKEN_FILE, encoding="utf-8") as fh:
            sa_token = fh.read().strip()
    except OSError as exc:
        raise GraphError(f"cannot read {OP_TOKEN_FILE}: {exc}")
    env = os.environ.copy()
    env["OP_SERVICE_ACCOUNT_TOKEN"] = sa_token
    proc = subprocess.run(["op", "read", OP_SECRET_REF],
                          env=env, capture_output=True, text=True)
    if proc.returncode != 0:
        raise GraphError("op read failed: " + proc.stderr.strip()[:300])
    secret = proc.stdout.strip()
    if not secret:
        raise GraphError("op read returned an empty secret")
    return secret


def get_token():
    data = urllib.parse.urlencode({
        "client_id": CLIENT,
        "client_secret": get_secret(),
        "scope": SCOPE,
        "grant_type": "client_credentials",
    }).encode()
    req = urllib.request.Request(
        f"https://login.microsoftonline.com/{TENANT}/oauth2/v2.0/token",
        data=data, method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))["access_token"]
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:300]
        raise GraphError(f"token endpoint HTTP {exc.code}: {body}")
    except urllib.error.URLError as exc:
        raise GraphError(f"token endpoint unreachable: {exc.reason}")


# ------------------------------------------------------------------- graph --

def graph_req(token, method, path, body=None):
    url = path if path.startswith("http") else GRAPH + path
    payload = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {"Authorization": "Bearer " + token}
    if payload is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=payload, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            raw = resp.read()
            return json.loads(raw.decode("utf-8")) if raw else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:300]
        raise GraphError(f"{method} {url.split('?')[0]} -> HTTP {exc.code}: {detail}")
    except urllib.error.URLError as exc:
        raise GraphError(f"{method} {url.split('?')[0]} -> unreachable: {exc.reason}")


def qs(params):
    return urllib.parse.urlencode(params, quote_via=urllib.parse.quote, safe="")


def deferred_of(message):
    for prop in message.get("singleValueExtendedProperties") or []:
        if str(prop.get("id", "")).lower().endswith(DEFER_PROP_TAG):
            return prop.get("value")
    return None


def list_guide_drafts(sender, token):
    """All Drafts whose subject starts with SUBJECT_PREFIX, with deferred prop."""
    path = f"/users/{urllib.parse.quote(sender)}/mailFolders/drafts/messages?" + qs({
        "$filter": f"startswith(subject,'{SUBJECT_PREFIX}')",
        "$top": "100",
        "$select": "id,subject,toRecipients,hasAttachments,internetMessageId,createdDateTime",
        "$expand": f"singleValueExtendedProperties($filter=id eq '{DEFER_PROP_ID}')",
    })
    out = []
    while path:
        page = graph_req(token, "GET", path)
        out.extend(page.get("value", []))
        path = page.get("@odata.nextLink")
    return out


def attachments_of(sender, token, msg_id):
    path = f"/users/{urllib.parse.quote(sender)}/messages/{msg_id}/attachments?" + qs(
        {"$select": "name,size,contentType"})
    return graph_req(token, "GET", path).get("value", [])


def read_message(sender, token, msg_id):
    """Readback: deferred property + attachment metadata (no contentBytes)."""
    path = f"/users/{urllib.parse.quote(sender)}/messages/{msg_id}?" + qs({
        "$select": "id,subject,toRecipients,internetMessageId",
        "$expand": (f"singleValueExtendedProperties($filter=id eq '{DEFER_PROP_ID}'),"
                    "attachments($select=name,size)"),
    })
    try:
        msg = graph_req(token, "GET", path)
        atts = msg.get("attachments") or []
    except GraphError:
        path = f"/users/{urllib.parse.quote(sender)}/messages/{msg_id}?" + qs({
            "$select": "id,subject,toRecipients,internetMessageId",
            "$expand": f"singleValueExtendedProperties($filter=id eq '{DEFER_PROP_ID}')",
        })
        msg = graph_req(token, "GET", path)
        atts = attachments_of(sender, token, msg_id)
    return msg, atts


def same_instant(a, b):
    def parse(value):
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    try:
        return parse(a) == parse(b)
    except (TypeError, ValueError):
        return False


def to_address(msg):
    recips = msg.get("toRecipients") or []
    return recips[0].get("emailAddress", {}).get("address", "?") if recips else "?"


# ------------------------------------------------------------------- state --

def load_state():
    if not os.path.exists(STATE_FILE):
        return []
    try:
        with open(STATE_FILE, encoding="utf-8") as fh:
            data = json.load(fh)
        return data if isinstance(data, list) else []
    except (OSError, ValueError):
        return []


def upsert_state(entry):
    rows = [r for r in load_state() if r.get("mail") != entry["mail"]]
    rows.append(entry)
    rows.sort(key=lambda r: (r.get("deferred_utc", ""), r.get("mail", "")))
    with open(STATE_FILE, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


# --------------------------------------------------------------- commands --

def cmd_dry_run(sched):
    tpl_ok = os.path.exists(TEMPLATE_FILE)
    head = (f"{'NAME':<28}{'MAIL':<30}{'NUMMER':<15}{'PORT':<12}"
            f"{'SEND (Berlin)':<20}{'SEND (UTC)':<23}{'WD':<5}PDF")
    print(head)
    print("-" * len(head))
    missing = []
    for rec in sched["recipients"]:
        local, utc = send_times(sched, rec)
        path = pdf_path(sched, rec)
        found = os.path.isfile(path)
        if not found:
            missing.append(rec["pdf"])
        print(f"{rec['name']:<28}{rec['mail']:<30}{rec['nummer']:<15}{rec['portdatum']:<12}"
              f"{local.strftime('%Y-%m-%d %H:%M'):<20}{utc_z(utc):<23}"
              f"{local.strftime('%a'):<5}{'yes' if found else 'NO'}")
        print(f"    att:  {attachment_name(rec)}")
        print(f"    subj: {subject_for(sched, rec)}")
    print("-" * len(head))
    print(f"recipients: {len(sched['recipients'])}  pdfs missing: {len(missing)}  "
          f"template: {'ok' if tpl_ok else 'MISSING'}")
    if missing:
        for name in missing:
            print("MISSING PDF: " + name, file=sys.stderr)
        return 1
    return 0 if tpl_ok else 1


def cmd_render(sched, mail):
    rec = next((r for r in sched["recipients"] if r["mail"].lower() == mail.lower()), None)
    if rec is None:
        print("no such recipient: " + mail, file=sys.stderr)
        return 1
    sys.stdout.write(render(load_template(), rec))
    return 0


def cmd_create(sched, only):
    sender = sched["sender"]
    recs = pick(sched, only)
    tpl = load_template()

    for rec in recs:
        if not os.path.isfile(pdf_path(sched, rec)):
            print(f"ABORT: pdf missing for {rec['mail']}: {rec['pdf']}", file=sys.stderr)
            return 1

    token = get_token()
    existing = {m.get("subject"): m for m in list_guide_drafts(sender, token)}
    failures, created, skipped = [], 0, 0

    for rec in recs:
        subject = subject_for(sched, rec)
        if subject in existing:
            print(f"SKIP   {rec['mail']:<30} draft already in Drafts "
                  f"(id {existing[subject]['id'][:16]}…)")
            skipped += 1
            continue
        try:
            local, utc = send_times(sched, rec)
            expected = utc_z(utc)
            with open(pdf_path(sched, rec), "rb") as fh:
                content = base64.b64encode(fh.read()).decode()
            att_name = attachment_name(rec)
            msg = {
                "subject": subject,
                "body": {"contentType": "HTML", "content": render(tpl, rec)},
                "toRecipients": [{"emailAddress": {"address": rec["mail"]}}],
                "attachments": [{
                    "@odata.type": "#microsoft.graph.fileAttachment",
                    "name": att_name,
                    "contentType": "application/pdf",
                    "contentBytes": content,
                }],
                "singleValueExtendedProperties": [
                    {"id": DEFER_PROP_ID, "value": expected}],
            }
            draft = graph_req(token, "POST",
                              f"/users/{urllib.parse.quote(sender)}/messages", msg)
            back, atts = read_message(sender, token, draft["id"])

            got = deferred_of(back)
            if not same_instant(got, expected):
                raise GraphError(f"deferred property mismatch: got {got!r}, want {expected!r}")
            if len(atts) != 1:
                raise GraphError(f"expected 1 attachment, got {len(atts)}")
            if atts[0].get("name") != att_name:
                raise GraphError(f"attachment name mismatch: {atts[0].get('name')!r}")
            if to_address(back).lower() != rec["mail"].lower():
                raise GraphError(f"recipient mismatch: {to_address(back)!r}")

            print(f"OK     {rec['mail']:<30} defer {got}  att {atts[0]['name']} "
                  f"({atts[0].get('size', 0)} B)  id {draft['id'][:16]}…")
            upsert_state({
                "mail": rec["mail"],
                "name": rec["name"],
                "subject": subject,
                "draft_id": draft["id"],
                "internetMessageId": back.get("internetMessageId"),
                "deferred_utc": expected,
                "send_local": local.strftime("%Y-%m-%d %H:%M %Z"),
                "attachment": att_name,
                "created_at": datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%dT%H:%M:%SZ"),
            })
            created += 1
        except (GraphError, OSError, KeyError) as exc:
            print(f"FAIL   {rec['mail']:<30} {exc}", file=sys.stderr)
            failures.append(rec["mail"])

    print(f"\ncreated {created}, skipped {skipped}, failed {len(failures)}"
          f"  (state: {STATE_FILE})")
    return 1 if failures else 0


def cmd_list(sched):
    sender = sched["sender"]
    token = get_token()
    drafts = list_guide_drafts(sender, token)
    drafts.sort(key=lambda m: (deferred_of(m) or "", m.get("subject") or ""))
    head = f"{'TO':<30}{'DEFERRED (UTC)':<23}{'ATT':<5}{'ID':<20}SUBJECT"
    print(head)
    print("-" * len(head))
    failures = []
    for msg in drafts:
        try:
            atts = attachments_of(sender, token, msg["id"])
            count = str(len(atts))
        except GraphError as exc:
            count = "ERR"
            failures.append(f"{msg.get('subject')}: {exc}")
        print(f"{to_address(msg):<30}{str(deferred_of(msg)):<23}{count:<5}"
              f"{msg['id'][:18]:<20}{msg.get('subject')}")
    print("-" * len(head))
    print(f"drafts matching '{SUBJECT_PREFIX}…': {len(drafts)}")
    for line in failures:
        print("ERROR " + line, file=sys.stderr)
    return 1 if failures else 0


def cmd_delete(sched, yes_really):
    sender = sched["sender"]
    token = get_token()
    drafts = list_guide_drafts(sender, token)
    if not yes_really:
        print(f"DRY: would delete {len(drafts)} draft(s). Re-run with --yes-really.")
        for msg in drafts:
            print(f"  would delete  {to_address(msg):<30}{msg.get('subject')}")
        return 0
    failures = []
    for msg in drafts:
        try:
            graph_req(token, "DELETE",
                      f"/users/{urllib.parse.quote(sender)}/messages/{msg['id']}")
            print(f"deleted  {to_address(msg):<30}{msg.get('subject')}")
        except GraphError as exc:
            print(f"FAIL     {to_address(msg):<30}{exc}", file=sys.stderr)
            failures.append(msg["id"])
    print(f"deleted {len(drafts) - len(failures)}, failed {len(failures)}")
    return 1 if failures else 0


def cmd_send(sched, only, yes_really):
    """Phase B. Owner go required."""
    if not yes_really:
        print("REFUSED: --send needs --yes-really (Phase B, owner go only).", file=sys.stderr)
        return 1
    sender = sched["sender"]
    token = get_token()
    drafts = list_guide_drafts(sender, token)
    if only:
        wanted = {m.lower() for m in only}
        drafts = [m for m in drafts if to_address(m).lower() in wanted]
    failures = []
    for msg in drafts:
        try:
            graph_req(token, "POST",
                      f"/users/{urllib.parse.quote(sender)}/messages/{msg['id']}/send")
            print(f"sent     {to_address(msg):<30}{msg.get('subject')}")
        except GraphError as exc:
            print(f"FAIL     {to_address(msg):<30}{exc}", file=sys.stderr)
            failures.append(msg["id"])
    print(f"submitted {len(drafts) - len(failures)}, failed {len(failures)}")
    return 1 if failures else 0


# -------------------------------------------------------------------- main --

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true",
                    help="show the plan, verify PDFs (default)")
    ap.add_argument("--render", metavar="MAIL",
                    help="print rendered HTML for one recipient")
    ap.add_argument("--create-drafts", action="store_true",
                    help="create deferred drafts in the sender's Drafts folder")
    ap.add_argument("--list", action="store_true", dest="do_list",
                    help="list existing guide drafts")
    ap.add_argument("--delete", action="store_true",
                    help="delete (cancel) existing guide drafts")
    ap.add_argument("--send", action="store_true",
                    help="Phase B: send the drafts now (owner go only)")
    ap.add_argument("--only", action="append", metavar="MAIL", default=[],
                    help="restrict to this address (repeatable)")
    ap.add_argument("--yes-really", action="store_true",
                    help="required confirmation for --delete and --send")
    args = ap.parse_args(argv)

    sched = load_schedule()
    try:
        if args.render:
            return cmd_render(sched, args.render)
        if args.create_drafts:
            return cmd_create(sched, args.only)
        if args.do_list:
            return cmd_list(sched)
        if args.delete:
            return cmd_delete(sched, args.yes_really)
        if args.send:
            return cmd_send(sched, args.only, args.yes_really)
        return cmd_dry_run(sched)
    except GraphError as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
