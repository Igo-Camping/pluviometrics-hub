# NEEDS_CONFIRMATION_CANDIDATES — Pluviometrics Hub

**Audit branch:** `audit/dead-file-audit-hub`.

---

## 1 candidate — `assets/logos/pluviometrics-main.png`

| Property | Value |
|---|---|
| Tracer status | 0 references from any other tracked file |
| Phase 1 finding | Hub `index.html` does not `<img src>` this file. The hub loads `Assets/Logos/PLUVIOMETRICS.png` (376 KiB compact version) for display. |
| Phase 1 action | Re-encoded from 18,751 × 14,584 (300 DPI master, 1.87 MiB) to 2,000 × 1,556 (308 KiB) so it would weigh less on the deploy. |
| Possible reason to keep | External Pluviometrics properties may link directly to `pluviometrics-main.png` as a master logo URL. |

**Question for operator:**
> *Is `assets/logos/pluviometrics-main.png` linked from any external Pluviometrics property? If no, the file can be removed from the hub repo (Stormgauge also has its own copy, `assets/logos/pluviometrics-main.png`, that's flagged in the Stormgauge audit). If yes, keep — the Phase 1 re-encode already mitigated the deploy-size cost.*

**Why it cannot be safely classified without operator input:** external link auditing is operator knowledge that is not visible to a static reference tracer.

**Suggested commit group if approved for deletion:** `commit-1: drop unreferenced master logo` (1 file).
