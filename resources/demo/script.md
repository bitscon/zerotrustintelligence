# ZTI Demo Script

## Scenario: AI-Generated Infrastructure Change

An AI agent operating inside a CI/CD pipeline proposes a Terraform infrastructure change.
This demo walks through two outcomes: a proposal that fails verification and one that passes.

The full terminal simulation is in `terminal-output.md`.

---

## Setup

**What is being demonstrated:**

The ZTI verification layer intercepting an AI-generated proposal at the execution boundary —
before any change reaches infrastructure.

**What this is not:**

- A demo of AI capability
- A demo of ZTI improving AI output quality
- A demonstration that ZTI makes AI correct

**What this is:**

A demonstration that only a proposal satisfying the declared execution contract
is allowed to cross from generation into execution.

---

## Cast

| Actor | Role |
|---|---|
| AI Agent | Generates a Terraform change proposal |
| ZTI Verification Layer | Classifies, validates, seals, or rejects |
| Execution System | Only receives verified decision artifacts |

---

## Scene 1 — Unsafe Proposal (Blocked)

### Narration

> An AI agent has generated a Terraform plan recommending a change to production infrastructure.
> The plan proposes deploying resources in a region outside the organization's declared policy,
> without the required approval entry in the lineage record.

> The proposal reaches the ZTI verification layer.

> ZTI classifies the proposal against the Pattern Registry.
> The proposal matches the `infrastructure-change` decision class.

> ZTI moves to validation. It checks the declared constraints:
> - Approved regions: `us-east-1`, `us-west-2`
> - Proposed region: `eu-central-1`

> The proposed region is outside the allowed set.

> ZTI does not degrade gracefully. The pathway to execution is closed.
> The proposal is logged with a sealed rejection artifact.
> The AI is not stopped. The execution boundary held.

### What the audience sees

Terminal output showing:
- AI proposal received
- ZTI classification (matched class: infrastructure-change)
- ZTI validation: FAIL — region constraint violation
- Rejection artifact sealed with decision hash
- Execution system: no artifact received

---

## Scene 2 — Compliant Proposal (Verified and Allowed)

### Narration

> A second proposal is generated. This time the AI agent has produced a plan
> within the approved region, referencing approved modules, within the declared
> blast-radius limit, with the required approval entry recorded.

> The proposal reaches the ZTI verification layer.

> ZTI classifies it. Pattern match: `infrastructure-change`.

> ZTI validates all declared constraints. Each check passes.

> ZTI generates an explanation artifact — an explicit record of which signals matched
> and which policy conditions were satisfied.

> ZTI seals the decision artifact with a cryptographic hash and records
> the approval lineage.

> The sealed artifact crosses the execution boundary.
> The execution system receives exactly this artifact — not the raw AI output.
> Not the Terraform plan text. The verified decision artifact.

> Auditors can now reconstruct: what was proposed, what policy passed, who approved it,
> and which artifact hash reached execution. The record is tamper-evident.

> ZTI did not evaluate whether the infrastructure change was a good idea.
> It evaluated whether the proposal satisfied the declared contract for execution.

### What the audience sees

Terminal output showing:
- AI proposal received
- ZTI classification (matched class: infrastructure-change)
- ZTI validation: PASS — all constraints satisfied
- Explanation artifact generated
- Decision artifact sealed (decision hash shown)
- Execution system: verified artifact received
- Lineage record: sealed, auditable

---

## Closing Line

> AI generated the proposal.
> ZTI verified it.
> Only the verified decision executed.

---

## Key Points to Land

1. ZTI intercepted at the boundary — not inside the AI, not inside the execution system.
2. The execution system never saw the raw AI output. It saw a sealed artifact.
3. The rejection in Scene 1 was deterministic — not probabilistic, not heuristic.
4. The approval in Scene 2 is reproducible. The same inputs will produce the same result.
5. The audit trail exists before any incident occurs — not assembled after the fact.
