# HUB_AUDIT_NOTES

**Repo:** `pluviometrics-hub` (deploys to pluviometrics.com.au via Cloudflare Pages, branch `main`).
**Audit branch:** `audit/assessment-hardening-hub`.
**Status:** Report only. No code changed.

---

## Findings — short version

The hub is the smallest and cleanest of the three repos. The assessment's main complaint about the hub is **commercial positioning / copy** — not technical. Technical findings are minor.

| Concern | Status |
|---|---|
| Path leaks (tracked) | **None.** Verified across all 10 tracked files. |
| Inline JS bloat | **None.** 4,889-char `index.html`, 1.3 KB total inline JS in 2 small blocks (theme flash + nav IIFE). |
| Hosting | **Cloudflare Pages, always-on.** No Render dependency. No external API dependency. |
| External data fetches | **None.** Hub is fully static. |
| LICENSE / NOTICE | **Missing** — same as the other two repos. |
| Heavy assets | One: `Assets/Logos/pluviometrics-main.png` at 1.96 MB. Easy ~80 % size reduction with a re-export at 720p–1080p, no design impact. |
| CSP | Present (`index.html:7`). Need to verify it allows everything the hub uses; spot-check looks fine since hub loads no external resources beyond the logos it serves. |

---

## Tracked file inventory

```
.gitignore         ─ standard
.nojekyll          ─ Cloudflare Pages marker
CNAME              ─ pluviometrics.com.au
index.html         ─ 4,889 chars (4 KB)
styles.css         ─ small
Assets/Logos/pluviometrics-main.png   ─ 1.96 MB    ← only heavy file
Assets/Logos/PLUVIOMETRICS.png        ─ 376 KB
Assets/Logos/STORMGAUGE.png           ─ 555 KB
Assets/Logos/ATMOS.png                ─ 723 KB
```

Total deploy: ~3.6 MB, dominated by logos.

---

## Recommended next fixes (NOT applied)

1. **Re-export `Assets/Logos/pluviometrics-main.png`** at typical web resolution. Same image, smaller file. No design or branding change. Risk: zero. Project rule "do not modify branding / replace existing Pluviometrics assets" is preserved — this is a re-encode at lower file size, not a recreation or replacement.
2. **Add `LICENSE`** (author choice).
3. **Add `THIRD_PARTY_NOTICES.md`** — minimal, since hub uses no JS libraries.
4. **Add `DATA_PROVENANCE.md`** — n/a, hub ships no data; can be a one-liner saying so.
5. **Hub commercial-positioning rewrite** — out of scope for an audit pass; the prompt's Task 7 belongs in a separate Plan-mode design session because it's copy + UX, not code.

## What this report does NOT do

- Does not modify the hub.
- Does not re-export the logo.
- Does not rewrite any copy.
