# DEAD_FILE_AUDIT — Pluviometrics Hub

**Branch:** `audit/dead-file-audit-hub` (off `main`).
**Method:** Same reference tracer as Stormgauge / Stormgrid. Strict basename + relative-path literal matching.
**Date:** 2026-05-07.

**Audit only — no files deleted, moved, or edited.**

---

## Headline

| Property | Value |
|---|---|
| Total tracked files | 10 |
| Strict-unreferenced | 5 |
| Genuinely dead (high-confidence SAFE_DELETE) | **1** (`Superseeded/stormgauge-direct-calculator-link-before-fix/index.html`) |
| Operator decision required | **1** (`assets/logos/pluviometrics-main.png` — Phase 1 carryover) |
| ACTIVE / config / entry-point | 8 |

The hub is the smallest of the three repos and is largely clean.

| Tracked file | Tracer status | Classification |
|---|---|---|
| `index.html` | unref (entry point) | ACTIVE |
| `styles.css` | strong refs from index.html | ACTIVE |
| `CNAME` | unref (Cloudflare Pages config) | ACTIVE |
| `.nojekyll` | unref (Cloudflare Pages config) | ACTIVE |
| `Assets/Logos/ATMOS.png` | strong refs from index.html | ACTIVE |
| `Assets/Logos/PLUVIOMETRICS.png` | strong refs from index.html | ACTIVE |
| `Assets/Logos/STORMGAUGE.png` | strong refs from index.html | ACTIVE |
| `Assets/Logos/STORMGRID.svg` | strong refs from index.html | ACTIVE |
| `assets/logos/pluviometrics-main.png` | unref | NEEDS_CONFIRMATION (master logo, Phase 1 finding) |
| `Superseeded/stormgauge-direct-calculator-link-before-fix/index.html` | unref | **SAFE_DELETE** |

## Cross-cutting issues

**Case-duplicate directories** — `Assets/` and `assets/` exist as separate paths in Git but are the same directory on Windows. Same issue as Stormgauge. Out of scope for this audit (it's a move, not a delete) but flagged for a future consolidation pass.

## Sibling reports (this branch)

- `reports/SAFE_DELETE_CANDIDATES.md` — 1 candidate.
- `reports/NEEDS_CONFIRMATION_CANDIDATES.md` — 1 candidate.
- `reports/ACTIVE_RUNTIME_DEPENDENCIES.md` — 8 ACTIVE files.
- `reports/HISTORICAL_REFERENCE_FILES.md` — empty.
