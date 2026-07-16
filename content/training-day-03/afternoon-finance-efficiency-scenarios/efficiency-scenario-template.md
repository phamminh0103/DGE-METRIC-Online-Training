\
# Energy-Efficiency Scenario Metadata Template

**New 2026-07-13**, replacing the old `pathway-template.md` (DER and LNG-to-Hydrogen pathways are out of scope for this iteration — see [`../../../design/decision-log.md`](../../../design/decision-log.md)). Per `../../../CLAUDE.md` "Scenario design rules," this scenario must be documented with this metadata block before it is run tomorrow morning. Copy this block into [`../../../scenarios/energy-efficiency/efficiency-scenario-log.md`](../../../scenarios/energy-efficiency/efficiency-scenario-log.md).

```text
Scenario label: efficiency-dsm-baseline
Policy mechanism: <one sentence — efficiency gains + DSM, and the channels they act through>
Exact file edits: <workbook/sheet/cell or config, or "n/a — definition only">
Exact variables changed: <e.g. sector-specific energy input coefficients, DSM load-shifting parameter>
Affected sectors: <manufacturing / services-commercial / households>
Time path: <how savings ramp in, through what year>
Start year: <year>
End year: <year, or "ongoing">
Transition profile: <immediate / phased / ramped, with detail>
Expected effects: <one paragraph — mechanism, direction, AND the rebound effect>
Key output indicators: <e.g. energy intensity, final energy demand, GDP, investment, energy prices>
Caveats: <data/calibration/assumption limitations>
Person or group responsible: <name/group>
Date created or revised: <YYYY-MM-DD>
```

## Worked example

```text
Scenario label: efficiency-dsm-baseline
Policy mechanism: Prioritized efficiency gains in industry and transport plus demand-side management that flattens peak loads and slows total electricity demand growth
Exact file edits: [SME REVIEW NEEDED: confirm exact ExcelFiles/ cell or config path used to set sector-specific efficiency coefficients for this cohort's repository copy]
Exact variables changed: sector-specific energy input coefficients (manufacturing, services/commercial, households); DSM load-shifting parameter
Affected sectors: manufacturing, services/commercial, households
Time path: efficiency gains ramp in linearly to reach 2030 savings targets: ≈7.4% manufacturing, ≈5.1% services/commercial, ≈11.6% households
Start year: [SME REVIEW NEEDED: confirm model start year for this cohort's baseline]
End year: 2030 target, ongoing thereafter (no reversal specified in source)
Transition profile: phased/ramped to reach the 2030 savings potential
Expected effects: lower energy intensity of production and reduced peak electricity demand should lower fossil-fuel and electricity imports and system costs; quantified investment need ≈USD 361 million/year (≈0.076% of 2024 GDP); a documented rebound effect means higher efficiency raises productivity and GDP, and the resulting extra economic activity partly offsets the direct energy savings — net savings are smaller than the gross efficiency gain
Key output indicators: energy intensity, final energy demand, GDP, investment, energy prices/expenditure, fossil-fuel and electricity imports
Caveats: rebound effect is documented but not separately quantified in the source — treat net savings as smaller than the gross 7.4%/5.1%/11.6% figures; DSM load-shifting effect on required generation capacity is qualitative only in the source
Person or group responsible: <fill in group name>
Date created or revised: 2026-07-13
```

Do not remove or leave blank any field. If a value is not known or not in the source documents, write `[SME REVIEW NEEDED: ...]` rather than inventing it.
