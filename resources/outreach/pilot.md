# Pilot Proposal

One workflow. Two to three weeks. One verified execution boundary in place.

---

## What This Is

A scoped exploration of ZTI applied to one existing AI-driven workflow.
Not a procurement. Not a platform adoption. Not a commitment beyond the scope defined here.

The goal is to have a working execution boundary in one workflow at the end of the pilot —
and a clear picture of what extending that boundary to other workflows would require.

---

## Scope

Choose one of the following:

**Option A — Infrastructure Automation**
Target: AI-assisted Terraform or infrastructure change workflow
Boundary: ZTI verification layer between AI proposal and CI/CD apply step
Policy: Approved modules, regions, blast-radius limits, required approvals

**Option B — CI/CD Pipeline**
Target: AI-generated pipeline configuration or deployment proposals
Boundary: ZTI verification layer between AI output and pipeline execution trigger
Policy: Approved environments, deployment windows, required sign-off by role

**Option C — Agent Runtime**
Target: An AI agent that proposes or executes API actions
Boundary: ZTI verification layer wrapping the tool-call or action-dispatch path
Policy: Allowed action classes, scope constraints, required lineage entries

One option. Not all three.

---

## Timeline

**Week 1 — Understand and Define**

- Map the chosen workflow: where AI output enters, where execution begins
- Define the policy constraints that belong at the boundary:
  what is always allowed, what requires approval, what is never allowed
- Stand up ZTI in audit mode against the workflow
- Review what the classification and validation surfaces look like against real proposals

**Week 2 — Verify and Refine**

- Review audit mode output: which proposals passed, which would have failed, why
- Refine the policy definitions based on audit mode findings
- Identify edge cases and define how the boundary handles them

**Week 3 — Enforce and Document**

- Switch the boundary to enforcement mode for the target workflow
- Run the workflow through the verified execution path
- Document: what the boundary catches, what the sealed record looks like,
  what the audit reconstruction looks like

---

## What You Have at the End

- One workflow with a working ZTI execution boundary in enforcement mode
- A sealed decision record for every proposal that passed through the boundary during the pilot
- A policy definition that can be versioned and extended
- A clear answer to: "what would it take to extend this to the next workflow?"

---

## What Is Not in Scope

- Modifying the AI system or model
- Rewriting the execution system
- Building new infrastructure — ZTI runs alongside existing policy engines,
  CI/CD gates, and audit logging
- A decision about broader adoption — that comes after the pilot

---

## References

Protocol specification: github.com/bitscon/zerotrustintelligence
Reference implementation: bitscon/zerotrustintelligence (Python, MIT license)
Demo scenario: zti-adoption/demo/terminal-output.md
Architecture: zti-adoption/assets/architecture.md
