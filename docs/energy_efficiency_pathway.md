# Energy Efficiency Pathway (Day 1 Afternoon)

This page is the training quick-start for the energy-efficiency pathway used in the Day 1 afternoon online session.

## Policy framing

Question: how much macroeconomic benefit can be unlocked by stronger demand-side efficiency, and how much of that effect is attributable to storage-enabled system integration (BESS)?

Core scenario pairs:
- `EE_PDP8` vs `EE_PDP8_NoBESS`
- `EE_Directive10` vs `EE_Directive10_NoBESS`
- `EE_PDP8_PV_BESS` vs `EE_PDP8_PV_BESS_NoBESS`

Pairwise differences isolate BESS contribution.

## Where assumptions live

Primary source workbook:
- `ExcelFiles/PDP8/Vietnam_EnergyExpert_ScenarioInputs - Adjust_2505.xlsx`

Fallback source workbook:
- `ExcelFiles/Vietnam_EnergyExpert_ScenarioInputs.xlsx`

Scenario writer script:
- `scripts/maintenance/CreateEEScenariosFromExpertInputs.m`

Model scenario workbook (written by the script):
- `ExcelFiles/ModelScenarios5Sectorsand1Regions.xlsx`

Technical design details:
- `docs/ee_scenario_design.md`
- `docs/ee_pv_coupling.md`

Policy interpretation and figures:
- `docs/use_cases_ee.md`

## Main mapping logic (expert inputs to model shocks)

- Industry and services EE saving percentages map into productivity shocks.
- EE and RTS investment costs map into accumulation channels for additional capital stock.
- PV integration gain and BESS investments map into dedicated efficiency and capital channels.
- In NoBESS sheets, BESS-specific channels revert to baseline while EE channels are preserved.

## Day 1 afternoon workflow

1. Inspect expert assumptions in the source workbook.
2. Regenerate EE scenario sheets with `CreateEEScenariosFromExpertInputs.m`.
3. Validate that full and NoBESS sheets were written correctly.
4. Confirm scenario group selection in `RunSimulations.m`.
5. Run scenarios and prepare Day 2 interpretation outputs.

## Suggested checks before Day 2 run-and-interpret block

- Verify year alignment between expert input years and baseline years.
- Confirm terminal-year behavior for extrapolated paths.
- Confirm NoBESS sheets only reset BESS channels (not EE productivity channels).

## Related references

- `docs/scenarios_overview.md`
- `docs/ee_scenario_design.md`
- `docs/running.md`
