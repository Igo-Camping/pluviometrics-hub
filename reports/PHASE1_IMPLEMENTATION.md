# PHASE1_IMPLEMENTATION — Pluviometrics Hub

**Branch:** `feature/phase1-safe-hardening-hub` (off `main`).
**Scope:** Hub-specific Phase 1 changes. Cross-repo summary lives in `pluvio-stormgauge:feature/phase1-safe-hardening-stormgauge:reports/PHASE1_IMPLEMENTATION.md`.

---

## Files changed

| File | Change |
|---|---|
| `Assets/Logos/pluviometrics-main.png` | Re-encoded — same image, smaller file. 18,751 × 14,584 (300 DPI master) → 2,000 × 1,556 web resolution. PNG mode RGBA preserved. **1.87 MiB → 308 KiB (84% smaller).** Visual fidelity maintained at any reasonable display size. The hub's `index.html` does not reference this file (it loads `PLUVIOMETRICS.png` instead) — the master is kept in case external Pluviometrics properties link to it. |
| `LICENSE` | New — proprietary, all rights reserved. |
| `THIRD_PARTY_NOTICES.md` | New — confirms hub uses no third-party JS or fonts at runtime. |
| `DATA_PROVENANCE.md` | New — confirms hub ships no third-party data. |
| `README.md` | New — high-level overview, link to OPERATIONS. |
| `docs/OPERATIONS.md` | New — Cloudflare Pages topology, branch model, hub-as-pure-landing-page note. |

## What was deliberately not touched

- `index.html` — unchanged.
- `styles.css` — unchanged.
- All other logos in `Assets/Logos/` (PLUVIOMETRICS.png, ATMOS.png, STORMGAUGE.png, STORMGRID.svg) — unchanged. They're larger than ideal for their display dimensions but were not in the audited target list. Flagged as a follow-up.
- Brand artwork, layout, copy — unchanged.

## Validation

See `reports/PHASE1_VALIDATION.md`.
