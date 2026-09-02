# eSIM-Portierung guide mailer

One German guide mail per colleague from support@smart-velo.com with their Telekom eSIM
letter PDF attached, deferred to 09:00 Europe/Berlin exactly 7 days before their HIGH ->
Telekom port date. Wording is owner-approved (template.html).

Run order:
  python3 esim_guide_mailer.py --dry-run        # plan + PDF check (exit 1 if any missing)
  python3 esim_guide_mailer.py --create-drafts  # create drafts + readback verify
  python3 esim_guide_mailer.py --list           # 12 drafts, 1 attachment, deferred UTC
Phase B (actual send, --send --yes-really) runs only on owner go. Never before.
Cancel: `--delete --yes-really`, or delete the draft in Outlook (support@ Drafts). Dedupe
is the exact subject queried live from the mailbox, so re-running --create-drafts is safe;
--only <mail> restricts to single recipients. PDFs live in ~/Downloads/esims-split and
never enter this repo. Secret via env GRAPH_CLIENT_SECRET or 1Password, never logged.
