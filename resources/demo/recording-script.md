# Demo Recording Script

60–90 seconds. Word for word. Time each section as marked.

**Setup before recording:**
- Terminal open, font size large enough to read at 1080p
- `demo/terminal-output.md` queued for copy-paste
- No other windows visible
- No intro — start mid-screen, begin speaking on first keystroke

---

## [0:00 – 0:10] Opening

**Say:**
> "This is Zero Trust Intelligence — a verification layer between AI and execution.
> I'm going to show you two proposals. One gets blocked. One gets through."

**Show:** Empty terminal. Nothing running.

---

## [0:10 – 0:25] Scene 1 — Unsafe Proposal

**Say:**
> "An AI agent generates an infrastructure change. Terraform plan.
> It looks reasonable. It hits the ZTI layer."

**Show:** Paste and run Scene 1 terminal block through the classification step.

**Say:**
> "ZTI classifies it — infrastructure-change. Moves to validation."

**Show:** Validation output appearing line by line.

**Say:**
> "Region: eu-central-1. Not in the approved set."

**Pause 1 second.**

**Show:** `CONSTRAINT_VIOLATION` line and rejection artifact sealed.

**Say:**
> "Blocked. Rejection artifact sealed. The execution system received nothing."

---

## [0:25 – 0:45] Scene 2 — Compliant Proposal

**Say:**
> "Second proposal. Same task. This time the agent stays within policy."

**Show:** Paste and run Scene 2 terminal block through classification and validation.

**Say:**
> "Same classification. Validation runs."

**Show:** Constraint checks appearing, each with a checkmark.

**Say:**
> "All six constraints pass."

**Show:** Explanation artifact generated. Decision artifact sealed with hash.

**Say:**
> "Explanation artifact. Decision sealed. Forwarded to the execution system."

**Show:** Execution system receives verified artifact line.

---

## [0:45 – 1:00] Audit

**Say:**
> "Now — audit. Any point after execution."

**Show:** Paste and run audit block.

**Say:**
> "What was proposed. What policy it passed. Who approved it. Which hash executed.
> Chain intact. No reconstruction required."

---

## [1:00 – 1:10] Closing

**Say:**
> "AI generated the proposal. ZTI verified it. Only the verified decision executed.
> The protocol is at bitscon/zerotrustintelligence."

**Show:** Terminal with the final audit output still visible. Fade or cut.

---

## Production Notes

- Do not explain what ZTI is during the demo. The actions explain it.
- Do not say "this is really cool" or editorialize.
- The pause after the rejection line is intentional — let it land.
- If recording in one take, practice the Scene 1 → Scene 2 transition until it's clean.
- Total target: 75 seconds. Under 90 is acceptable. Over 90, cut the audit section to one line.
