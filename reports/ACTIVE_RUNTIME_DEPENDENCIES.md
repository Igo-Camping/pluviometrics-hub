# ACTIVE_RUNTIME_DEPENDENCIES — Pluviometrics Hub

**Audit branch:** `audit/dead-file-audit-hub`.

The protected surface for any future cleanup. **8 of the 10 tracked files are ACTIVE.**

---

| File | Reached from | Notes |
|---|---|---|
| `index.html` | Cloudflare Pages root | The landing page |
| `styles.css` | `<link rel="stylesheet">` in index.html | |
| `Assets/Logos/PLUVIOMETRICS.png` | `<img src="Assets/Logos/PLUVIOMETRICS.png">` in index.html (header + NBC card) | Visible logo |
| `Assets/Logos/ATMOS.png` | `<img>` in Atmos product card | Visible logo |
| `Assets/Logos/STORMGAUGE.png` | `<img>` in Stormgauge product card | Visible logo |
| `Assets/Logos/STORMGRID.svg` | `<img>` in Stormgrid product card | Visible logo |
| `CNAME` | Cloudflare Pages | Custom-domain pinning |
| `.nojekyll` | Cloudflare Pages | Disables Jekyll |

The hub does not load any JavaScript libraries from CDN (per `THIRD_PARTY_NOTICES.md`); it has only inline IIFE for theme toggle + nav. No `src/`, no module graph.

## NOT ACTIVE in this list

- `Superseeded/stormgauge-direct-calculator-link-before-fix/index.html` → `SAFE_DELETE_CANDIDATES.md`
- `assets/logos/pluviometrics-main.png` → `NEEDS_CONFIRMATION_CANDIDATES.md`
