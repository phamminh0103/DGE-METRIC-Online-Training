import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slidekit as sk

DECK = "DGE-METRIC Online Training — Online Day 1 — Wed 22 Jul 2026"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "DGE-METRIC_Online_Day1_Slides.pptx")

prs = sk.new_deck()
n = [0]
def pn():
    n[0] += 1
    return n[0]

# 1. Title
sk.title_slide(
    prs,
    "DGE-METRIC Online Training",
    "Online Day 1 — Finance & Energy-Efficiency Scenarios: Detailed Definition",
    [
        "Wednesday 22 July 2026 · Afternoon · 180 minutes",
        "GIZ Vietnam | DGE-METRIC Program | Online Module",
        "Continues numbering from the on-site training — this is Training Day 3, delivered online",
    ],
)
pn()

# 2. Agenda / block timing
sk.table_slide(
    prs, "Today's Agenda — 8 Blocks, 180 Minutes", ["Block", "Min", "What happens"],
    [
        ["1. Setup check-in", "10", "Confirm VS Code, GitHub, and an AI coding assistant are installed/enabled"],
        ["2. Welcome & where things live", "10", "Recap on-site outcomes; point to where financing and efficiency assumptions live in the repository"],
        ["3. Why financing design matters", "15", "Three reasons financing design is a first-order determinant of transition speed and cost"],
        ["4. The six-scenario finance matrix, in full", "35", "Baseline rate, concessional variant, revenue-recycling variant, mechanism by mechanism"],
        ["5. Draft finance-scenario metadata sheet", "25", "Groups document their assigned scenario in full"],
        ["— Break —", "15", ""],
        ["6. The energy-efficiency scenario, in full", "35", "Narrative, core channels, 2030 savings potential, investment need, rebound effect"],
        ["7. Draft efficiency-scenario metadata sheet", "30", "Groups document the efficiency scenario using the same rigor"],
        ["8. Wrap and preview", "5", "Confirm both metadata sheets recorded; preview tomorrow's hands-on run"],
    ],
    col_widths=[3.4, 0.8, 5.3], page_no=pn(), deck_label=DECK,
)

# 3. Setup check-in
sk.bullets_slide(
    prs, "Setup Check-In — VS Code, GitHub, AI Coding Assistant", kicker="Block 1 · 10 min · [Interactive]",
    items=[
        ("Quick poll — show of hands for each:", 0, True),
        ("VS Code installed and opens", 1, False),
        ("GitHub account exists (GitHub Desktop installed too, if you got to it)", 1, False),
        ("An AI coding assistant is enabled in VS Code — Claude Code, GitHub Copilot, or another LLM coding assistant", 1, False),
        ("Not ready yet? Pair with a neighbor who is, grab the quick-install links, and flag the facilitator", 0, False),
        ("We fix gaps in the first break, not live in front of the group — full Git/GitHub Desktop/VS Code instruction is still tomorrow morning, from scratch", 0, True),
    ], page_no=pn(), deck_label=DECK,
)

# 3b. Setup quick reference
sk.bullets_slide(
    prs, "Setup Quick Reference (Full Steps: setup-guide.md)", kicker="Block 1 · handout / reference",
    items=[
        ("VS Code: download from code.visualstudio.com, open once to confirm it launches", 0, False),
        ("GitHub: create a free account at github.com", 0, False),
        ("AI coding assistant — pick one:", 0, True),
        ("GitHub Copilot: Extensions view (Ctrl/Cmd+Shift+X) → search \"GitHub Copilot\" → install → sign in with GitHub", 1, False),
        ("Claude Code: install Node.js, then run npm install -g @anthropic-ai/claude-code, then run claude in VS Code's terminal", 1, False),
        ("Or another LLM coding assistant you're already comfortable with", 1, False),
        ("MATLAB: should already be installed from on-site training — open it directly and confirm it runs a command", 0, False),
        ("Optional: add the \"MATLAB\" extension (by MathWorks) in VS Code for .m file syntax highlighting", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

# 4. Welcome
sk.bullets_slide(
    prs, "Welcome Back", kicker="Block 2 · 10 min",
    items=[
        ("This course continues directly from your on-site training (Training Days 1–2, and Day 3 if already completed)", 0, False),
        ("Today and tomorrow go deep on two scenario families: finance and energy efficiency — fully defined today, run and interpreted tomorrow morning", 0, False),
        ("Where the assumptions live: docs/financing_pathway.md, docs/energy_efficiency_pathway.md, ExcelFiles/", 0, False),
        ("Full codebase navigation and Git/GitHub Desktop are taught tomorrow morning, right before you need them hands-on — not repeated here", 0, True),
    ], page_no=pn(), deck_label=DECK,
)

# 5. Why financing design matters
sk.bullets_slide(
    prs, "Why Financing Design Matters", kicker="Block 3 · 15 min",
    items=[
        ("Affordability of public investment — lower borrowing rates reduce the debt-service burden of transition investment", 0, False),
        ("Investment crowd-in — recycling emission-tax revenue into renewable capital can fund additional capacity without new borrowing", 0, False),
        ("Policy credibility — transparent, pre-announced financing rules improve implementation certainty for investors", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

# 6. Finance matrix in full detail
sk.table_slide(
    prs, "The Six-Scenario Finance Matrix", ["Scenario ID", "Emissions pathway", "Financing rate", "Revenue recycling"],
    [
        ["PDP8-Base", "PDP8", "8%", "No"],
        ["NZ-Base", "Net Zero", "8%", "No"],
        ["PDP8-Concessional", "PDP8", "5%", "No"],
        ["NZ-Concessional", "Net Zero", "5%", "No"],
        ["PDP8-Recycle", "PDP8", "8%", "Yes"],
        ["NZ-Recycle", "Net Zero", "8%", "Yes"],
    ],
    col_widths=[2.6, 2.2, 1.8, 1.8], kicker="Block 4 · 35 min", page_no=pn(), deck_label=DECK,
    note="Compare concessional/recycling variants against the base case with the SAME emissions pathway only.",
)

# 7. Draft finance metadata sheet
sk.bullets_slide(
    prs, "Draft Your Finance-Scenario Metadata Sheet", kicker="Block 5 · 25 min",
    items=[
        ("Your group is assigned one of the six scenarios", 0, False),
        ("Document in full: label, mechanism, exact file edits, exact variables changed, time path, start/end year, transition profile, expected effects, key output indicators, caveats, owner, date", 0, False),
        ("Also state: which base case to compare against, and the single variable that differs from it", 0, False),
        ("Record your sheet in the finance scenario log before the break", 0, True),
    ], page_no=pn(), deck_label=DECK,
)

sk.section_slide(prs, "Short break", "15 minutes", "Next: the energy-efficiency scenario, in the same depth as the finance matrix")

# 8. Energy efficiency scenario
sk.bullets_slide(
    prs, "The Energy-Efficiency & DSM Scenario, in Full Detail", kicker="Block 6 · 35 min",
    items=[
        ("Narrative: prioritized efficiency gains in industry and transport, plus demand-side management (DSM) that flattens peak loads and slows electricity demand growth", 0, False),
        ("Core channels: lower energy intensity of production; reduced peak electricity demand; slower final-energy demand growth; lower fossil-fuel and electricity imports", 0, False),
        ("2030 savings potential: ≈7.4% manufacturing, ≈5.1% services/commercial, ≈11.6% households", 0, False),
        ("Quantified investment need: ≈USD 361 million/year (≈0.076% of 2024 GDP)", 0, False),
        ("Rebound effect: higher efficiency raises productivity and GDP, and the resulting extra activity partly offsets direct energy savings", 0, True),
        ("Compared against the PDP8 baseline — front-loaded, investment-driven decarbonization", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

# 9. Draft efficiency metadata sheet
sk.bullets_slide(
    prs, "Draft Your Energy-Efficiency Scenario Metadata Sheet", kicker="Block 7 · 30 min",
    items=[
        ("Same rigor as the finance sheet: mechanism, sector-specific assumptions (with source), affected sectors, time path, expected effects — including the rebound effect — key output indicators, caveats", 0, False),
        ("Affected sectors: manufacturing, services/commercial, households", 0, False),
        ("Cite every numeric value; mark anything not in energy_efficiency_pathway.md as [SME REVIEW NEEDED]", 0, True),
        ("Record your sheet in the energy-efficiency scenario log before the session ends", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

# 10. Debrief + common errors
sk.bullets_slide(
    prs, "Debrief & Common Errors", kicker="Wrap-up",
    items=[
        ("Debrief: for your finance scenario, what's the one variable that changes vs. its base case?", 0, False),
        ("Debrief: what does the rebound effect do to the efficiency scenario's net savings?", 0, False),
        ("Watch out for: confusing \"baseline\" with \"PDP8-Base\" — PDP8-Base is baseline on both dimensions", 0, False),
        ("Watch out for: comparing across emissions pathways by mistake — same-pathway comparison only", 0, False),
        ("Watch out for: leaving the rebound effect out of the efficiency scenario's expected-effects field", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

# 11. Wrap
sk.bullets_slide(
    prs, "Today's Output & What's Next", kicker="Block 8 · 5 min",
    items=[
        ("You leave today with:", 0, True),
        ("A completed finance-scenario metadata sheet for your assigned scenario", 1, False),
        ("A completed energy-efficiency scenario metadata sheet", 1, False),
        ("Tomorrow morning: codebase navigation, Git/GitHub Desktop, baseline calibration, and running both scenarios hands-on", 0, False),
    ], page_no=pn(), deck_label=DECK,
)

prs.save(OUT)
print("Saved", OUT, "with", len(prs.slides._sldIdLst), "slides")
