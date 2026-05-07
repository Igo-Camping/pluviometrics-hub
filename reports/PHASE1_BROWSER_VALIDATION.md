# PHASE1_BROWSER_VALIDATION — Hub

**Master report:** `pluvio-stormgauge:feature/phase1-safe-hardening-stormgauge:reports/PHASE1_BROWSER_VALIDATION.md`.

**Method:** Playwright + Chromium against a local HTTP server on port 8229 serving `feature/phase1-safe-hardening-hub`.

**Date:** 2026-05-07.

---

## Verdict

**13/13 PASS. Zero regressions.** Safe to merge.

## Results

| Check | Result |
|---|---|
| Page loads | PASS |
| Header logo loaded (non-zero natural width) | PASS |
| Product-card count = 4 | PASS |
| Atmos link → `atmos.pluviometrics.com.au` | PASS |
| Atmos card image loaded | PASS |
| Stormgauge link → `stormgauge.pluviometrics.com.au/?view=calculator` | PASS |
| Stormgauge card image loaded | PASS |
| Stormgrid link → `stormgrid.pluviometrics.com.au/` | PASS |
| Stormgrid card image loaded (SVG) | PASS |
| NBC link → `nbc.pluviometrics.com.au/?v=20260429-home` | PASS |
| All 5 images loaded with non-zero dimensions | PASS |
| Theme toggle works | PASS (sets `data-theme="dark"`) |
| Screenshot saved | PASS (`reports/phase1_hub.png`) |

## One non-blocking console message

```
The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.
```

**Pre-existing**, not introduced by Phase 1. CSP otherwise works correctly. Recommended Phase 2 follow-up: move CSP to a Cloudflare Pages `_headers` file (already noted in `HOSTING_HARDENING_PLAN.md`).
