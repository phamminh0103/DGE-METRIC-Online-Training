\
# Day 1 Setup Guide — VS Code, GitHub, AI Coding Assistant, MATLAB

**Do this before Online Day 1 (Wednesday 22 July).** Day 1 opens with a short setup check-in against this exact list (see `detailed-agenda.md`, Session 1, Block 1) — small gaps get fixed together in the first break, but please don't start from zero that morning.

No prior experience with any of these tools is required. Full hands-on Git/GitHub Desktop and VS Code instruction — from scratch — happens on Day 2 morning. This guide only gets the tools installed and open.

---

## 1. Install VS Code

- Download and install VS Code for your OS from `code.visualstudio.com`.
- Open it once and confirm it launches.

## 2. Set up GitHub

- Create a free account at `github.com` if you don't already have one.
- Installing GitHub Desktop (`desktop.github.com`) now is a bonus but not required — Day 2 morning walks through installing and using it from scratch.

## 3. Enable an AI coding assistant in VS Code

Pick **one** — any is fine for this course:

**Option A — GitHub Copilot**
1. In VS Code, open the Extensions view (`Ctrl+Shift+X` / `Cmd+Shift+X`).
2. Search for "GitHub Copilot" and install it.
3. Sign in with your GitHub account when prompted. You'll need an active Copilot subscription, trial, or org-provided seat.

**Option B — Claude Code**
1. Install Node.js if you don't already have it.
2. Open VS Code's integrated terminal (`` Ctrl+` ``) and run:
   ```
   npm install -g @anthropic-ai/claude-code
   ```
3. In a project folder, type `claude` in the terminal and follow the sign-in prompt.
4. If your organization provides a dedicated "Claude Code" VS Code extension, you can install that instead of the CLI.

**Option C — another AI coding assistant**
- Any LLM coding assistant you're already comfortable with (e.g., Codeium, Cursor, Tabnine) works fine. The course doesn't require a specific one.

## 4. Confirm MATLAB is installed and working

This should already be in place from the on-site training (Training Days 1–2). Before Day 1:
- Open MATLAB directly (not through VS Code) and confirm it starts.
- Run a simple command in the Command Window, e.g. `disp('ok')`, to confirm it's licensed and working.
- If MATLAB isn't installed or your license has expired, flag it to the course contact **before** Day 1 — MATLAB is a licensed install the course team cannot set up remotely for you.
- Dynare also needs to be installed and on the MATLAB path. If you need a refresher, see the on-site installation slides: `../../Installation/DGE_CRED_Training_Installation_Dynare.pdf`.

## 5. Optional: add MATLAB file support to VS Code

Some participants prefer editing MATLAB (`.m`) and Dynare (`.mod`) files inside VS Code rather than MATLAB's own editor.

1. In VS Code's Extensions view, search "MATLAB" (published by MathWorks) and install it.
2. This adds syntax highlighting and linting for `.m` files inside VS Code.

This step is optional. MATLAB's own editor works fine too, and Day 2 morning doesn't assume you've done this.

---

## Self-check before Day 1

- [ ] VS Code installed and opens
- [ ] GitHub account created
- [ ] One AI coding assistant enabled in VS Code (Copilot, Claude Code, or another)
- [ ] MATLAB opens and runs a command
- [ ] Dynare installed and on the MATLAB path

If anything is unchecked, that's exactly what Day 1's opening check-in is for — don't let it stop you from joining.
