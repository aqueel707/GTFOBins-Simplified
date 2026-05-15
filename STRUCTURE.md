# GTFOBins-Simplified — Directory Layout

```
GTFOBins-Simplified/
│
├── _binaries/                  # One YAML file per binary (data only)
│   ├── curl.yaml
│   ├── python.yaml
│   └── ...
│
├── _layouts/
│   ├── default.html            # Shell: <head>, nav, footer
│   └── binary.html             # Per-binary detail page
│
├── _includes/
│   ├── capability-badge.html   # Reusable capability tag partial
│   └── meta-block.html         # Collapsible metadata partial
│
├── _plugins/
│   └── capability_filter.rb    # Jekyll plugin: filter by capability
│
├── assets/
│   ├── css/
│   │   └── main.css            # Single stylesheet — no frameworks
│   └── js/
│       └── app.js              # Filter, search, expand/collapse
│
├── pages/
│   ├── index.html              # Master binary list with live filter
│   └── 404.html
│
├── schema/
│   ├── binary.schema.json      # JSON Schema for validation
│   └── binary.template.yaml    # Blank template for new entries
│
├── scripts/
│   └── migrate.py              # Migration helper: old GTFOBins → new format
│
├── .github/
│   └── CONTRIBUTING.md
│
├── _config.yml
└── README.md
```

## Files REMOVED from upstream GTFOBins
| Removed path | Reason |
|---|---|
| `_functions/` | Not needed in simplified model |
| `_posts/` | No blog content |
| `Gemfile.lock` (tracked) | Track only `Gemfile` |
| `_data/functions.yml` | Replaced by inline YAML fields |
| `assets/images/` | Icon set replaced with CSS badges |
| `_includes/gtfo.html` | Replaced by `capability-badge.html` |
| `_sass/` entire directory | Single `main.css` replaces all partials |
| `_pages/contribute.md` | Merged into `CONTRIBUTING.md` |
