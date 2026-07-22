# Four-carrier public-source assumptions (paste-ready)

This table is aligned with the toy-model rows in reserve_breakeven_table.csv and adds low/high sensitivity bands for use in DCE-METRIC input replacement.

Method:
- Central values: from reserve_breakeven_table.csv (same macro assumptions: p=0.04, GDP=430,000m USD).
- Low/high values: multiplicative sensitivity around central values.
- Oil products, crude oil, imported coal: ±25%.
- LNG: ±30% (higher project-cost variance).

Files:
- CSV: four_carrier_assumptions_public_sources.csv

Selected carriers and sources:
- Refined oil products: IEA Oil 2025; US DOE SPR context.
- Crude oil: IEA Oil 2025; US DOE SPR context.
- Imported coal: GEM coal terminals tracker; IEA Coal 2025.
- LNG: GEM LNG terminal pages + GGIT.

Note: the source links provide openly accessible benchmark context. The low/high bands are explicit sensitivity assumptions, not direct point estimates from a single source.
