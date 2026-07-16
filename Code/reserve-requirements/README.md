# Reserve-requirements break-even toy model

Illustrative MC = MB (marginal-cost = marginal-benefit) break-even calculator used in the Day 2 PM and Day 3 AM reserve-requirements sessions. This is a standalone toy model, not DGE-METRIC output — see the session materials for how the numbers are used.

## Run it

```bash
pip install openpyxl tabulate
python compute_reserve_breakeven.py
```

Reads `Data for DCE-METRIC.xlsx` and regenerates `reserve_breakeven_table.md` and `reserve_breakeven_table.csv`. To change the GDP figure or crisis probability, edit Section 1 of `compute_reserve_breakeven.py`.

## Files

- `compute_reserve_breakeven.py` — main script, depends on `ces_gdp_loss.py`
- `ces_gdp_loss.py` — CES production-chain GDP-loss helper
- `Data for DCE-METRIC.xlsx` — raw reserve-carrier cost data
- `reserve_breakeven_table.md` / `.csv` — generated break-even ranking used directly in the exercises
