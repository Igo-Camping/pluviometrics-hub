# SAFE_DELETE_CANDIDATES — Pluviometrics Hub

**Audit branch:** `audit/dead-file-audit-hub`.

---

## SAFE_DELETE — high confidence (1 file)

### `Superseeded/stormgauge-direct-calculator-link-before-fix/index.html`

| Property | Value |
|---|---|
| Path | `Superseeded/stormgauge-direct-calculator-link-before-fix/index.html` |
| Reason | Historical UI snapshot. Not routed to from the live `index.html`. Ships to Cloudflare Pages but is not linked from any nav. |
| Evidence | Tracer: 0 references from any other tracked file. The directory name (`Superseeded`) explicitly signals the operator's prior intent to retain as an archive copy. |
| Risk level | **None.** Recovery via `git checkout <pre-cleanup-commit> -- ...` if needed. |
| Suggested commit group | `commit-1: drop Superseeded/ directory` |

This is the only high-confidence SAFE_DELETE in the hub.

---

## What is NOT in this report

`assets/logos/pluviometrics-main.png` is a Phase 1 carryover — the unreferenced master logo. It's listed in `NEEDS_CONFIRMATION_CANDIDATES.md` because the operator may want to keep it for external Pluviometrics properties that link directly to that file. Phase 1 already re-encoded it from 1.87 MiB to 308 KiB to mitigate the deploy-size concern.
