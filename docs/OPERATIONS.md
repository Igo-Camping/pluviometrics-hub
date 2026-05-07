# Pluviometrics Hub — Operations

## Hosting

- **Platform:** Cloudflare Pages.
- **Custom domain:** pluviometrics.com.au
- **Deploy branch:** `main`.
- Static landing page only — `index.html`, `styles.css`, `Assets/Logos/`. No JavaScript libraries. No backend.

## Branch model

| Branch | Purpose |
|---|---|
| `main` | Production. What pluviometrics.com.au serves. |
| `feature/*` | Work-in-progress; merge to `main` to deploy. |
| `audit/*` | Read-only audit reports — never merged. |

## What the hub does

The hub provides four product cards linking to:

| Product | Domain |
|---|---|
| Atmos | https://atmos.pluviometrics.com.au |
| Stormgauge | https://stormgauge.pluviometrics.com.au |
| Stormgrid | https://stormgrid.pluviometrics.com.au |
| NBC (legacy) | https://nbc.pluviometrics.com.au |

That's the full surface. All linked products are independent products under the Pluviometrics brand and are governed by their own LICENSE / THIRD_PARTY_NOTICES / DATA_PROVENANCE files in their respective repos.

## Local preview

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Deployment procedure

1. Merge feature work to `main` via PR.
2. Verify https://pluviometrics.com.au/ within ~2 min.

## Backup and recovery

- Source code: GitHub (`Pluviometrics/pluviometrics-hub`).
- Cloudflare Pages config: managed via Cloudflare dashboard; `CNAME` and `.nojekyll` files pin the deploy.

## Asset notes

- `Assets/Logos/pluviometrics-main.png` is a master/archive logo file. The hub itself loads `Assets/Logos/PLUVIOMETRICS.png` (compact version). The master file is kept in the repo for any external Pluviometrics property that links to it.

## Key references

- `LICENSE` — copyright.
- `THIRD_PARTY_NOTICES.md` — confirms the hub uses no runtime third-party libraries.
- `DATA_PROVENANCE.md` — confirms the hub ships no third-party data.
