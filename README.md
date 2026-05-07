# Pluviometrics Hub

The landing page at **https://pluviometrics.com.au**. Lists the Pluviometrics product family with outbound links.

Static site — no JavaScript libraries, no backend, no data fetches. Served by Cloudflare Pages from `main`.

## Layout

```
.
├── index.html      Landing page
├── styles.css
├── Assets/Logos/   Brand artwork
├── docs/           Operator notes
├── CNAME           pluviometrics.com.au
└── .nojekyll       Disable Jekyll on Pages
```

## Local preview

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Documents

- `LICENSE` — proprietary, all rights reserved.
- `THIRD_PARTY_NOTICES.md` — confirms no runtime third-party libraries.
- `DATA_PROVENANCE.md` — confirms no third-party data shipped.
- `docs/OPERATIONS.md` — hosting and deployment notes.

## Linked products

| Product | Domain | Repo |
|---|---|---|
| Atmos | atmos.pluviometrics.com.au | (TBA) |
| Stormgauge | stormgauge.pluviometrics.com.au | `Pluviometrics/pluvio-stormgauge` |
| Stormgrid | stormgrid.pluviometrics.com.au | `Pluviometrics/pluvio-stormgrid` |
| NBC (legacy) | nbc.pluviometrics.com.au | `Pluviometrics/nbc` |
