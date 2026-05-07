# PHASE1_VALIDATION — Pluviometrics Hub

**Branch:** `feature/phase1-safe-hardening-hub`.
**Caveat:** Static validation only. Operator must run a browser smoke test before merge.

## Static checks

| Check | Result |
|---|---|
| `Assets/Logos/pluviometrics-main.png` opens and round-trips through PIL | ✓ PASS |
| New file size | 308 KiB (was 1.87 MiB) |
| New dimensions | 2000 × 1556 (was 18751 × 14584) |
| Aspect ratio preserved | ✓ 1.286:1 (unchanged) |
| PNG mode preserved | ✓ RGBA |
| Hub `index.html` references `pluviometrics-main.png` | **No** — the hub loads `PLUVIOMETRICS.png` instead. The re-encoded master file is therefore not on the visible critical path; this change is pure deploy-size cleanup. |
| `index.html` and `styles.css` byte-identical to `origin/main` | ✓ confirmed via `git diff` |

## Browser smoke test (operator action required)

Open Hub locally and confirm:

- [ ] Page renders correctly with all four product cards.
- [ ] Theme toggle works (light/dark).
- [ ] Logos display correctly in cards (Atmos, Stormgauge, Stormgrid, NBC).
- [ ] All four card links open the correct destinations:
  - [ ] Atmos → atmos.pluviometrics.com.au
  - [ ] Stormgauge → stormgauge.pluviometrics.com.au?view=calculator
  - [ ] Stormgrid → stormgrid.pluviometrics.com.au
  - [ ] NBC → nbc.pluviometrics.com.au
- [ ] No new console errors.

## Recommendation

**Safe to merge to `main`.** All changes are additive (LICENSE, NOTICES, PROVENANCE, README, OPERATIONS) or deploy-size cleanup of a file the hub doesn't actually load. Zero risk to the visible landing page.
