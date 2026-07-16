\
# Scenario Metadata Template

Per `../../../CLAUDE.md` "Scenario design rules," every scenario introduced in this training must be documented with this metadata block before it is run. Copy this block into [`../../../scenarios/finance/scenario-log.md`](../../../scenarios/finance/scenario-log.md) (or the relevant scenario log) once per scenario.

```text
Scenario label: <lowercase-kebab-case, e.g. finance-pdp8-concessional>
Policy mechanism: <one sentence — what lever changes>
Exact file edits: <workbook/sheet/cell or config, or "n/a — recap/prep only">
Exact variables changed: <e.g. public financing rate 8% -> 5%>
Time path: <how the shock is phased in>
Start year: <year>
End year: <year, or "ongoing">
Transition profile: <immediate / phased / ramped, with detail>
Expected effects: <one paragraph — mechanism and direction>
Key output indicators: <e.g. GDP, investment, emission-tax revenue, renewable capital>
Caveats: <data/calibration/assumption limitations>
Person or group responsible: <name/group>
Date created or revised: <YYYY-MM-DD>
```

## Worked example (finance matrix, PDP8-Concessional)

```text
Scenario label: finance-pdp8-concessional
Policy mechanism: Concessional public financing for renewable investment
Exact file edits: [SME REVIEW NEEDED: confirm exact ExcelFiles/ModFiles cell or config path used to set the public financing rate for this cohort's repository copy]
Exact variables changed: public investment financing rate, 8% -> 5% (-3pp), PDP8 emissions pathway held fixed
Time path: applied from scenario start year, held constant thereafter (per financing_pathway.md, "concessional shock" is a level change, not a ramp)
Start year: [SME REVIEW NEEDED: confirm model start year for this cohort's baseline]
End year: ongoing (no reversal specified in source)
Transition profile: immediate step change in financing rate at start year
Expected effects: lower cost of public capital for renewable investment should bring forward renewable capital accumulation relative to PDP8-Base, with a small positive effect on near-term investment and GDP
Key output indicators: public financing rate, renewable capital stock, GDP, investment, emission-tax revenue (if applicable), renewable generation
Caveats: compare only against PDP8-Base (same emissions pathway); do not cross-compare against NZ-Base
Person or group responsible: <fill in group name>
Date created or revised: 2026-07-13
```

Do not remove or leave blank any field. If a value is not known or not in the source documents, write `[SME REVIEW NEEDED: ...]` rather than inventing it.
