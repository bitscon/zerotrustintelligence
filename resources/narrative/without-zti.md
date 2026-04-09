# What Happens Without ZTI

Three scenarios. Each one is a class of incident that is happening now,
in organizations that have deployed AI-driven automation without an execution boundary.

---

## Scenario 1 — Infrastructure Drift

An AI agent is operating inside a platform engineering workflow.
Its task: respond to a capacity alert by scaling infrastructure.

The agent generates a Terraform plan. The plan looks reasonable.
It passes a linter. It passes a static policy check.
A human reviews the summary — not the full plan — and approves.

The plan executes.

Two hours later: 47 instances are running in a region the organization
does not use, against a module version that was deprecated six months ago
due to a known security configuration issue.

The capacity problem is solved. A new problem exists.

**What went wrong:**

No layer evaluated the proposal against the organization's declared execution contract
before it reached infrastructure. The linter checks syntax. The static policy check
checks a subset of rules. The human reviewed a summary, not a verifiable artifact.
The approval exists as a Slack message.

There is no sealed record of what was proposed, what was checked, who approved,
and what artifact executed. Reconstruction requires cross-referencing four systems.

**With ZTI:**

The proposal would have been classified against the infrastructure-change decision class.
The deprecated module version would have failed the admissibility check.
The non-approved region would have failed a second check.
A rejection artifact would have been sealed before the proposal reached execution.
The Slack approval would not have been the record of authorization — a cryptographic decision artifact would.

---

## Scenario 2 — Policy Bypass at Scale

A security automation system uses an AI agent to classify incoming alerts
and propose response actions — block an IP, quarantine a host, revoke a token.

The system operates at high volume. Human review exists but is
applied selectively, based on a confidence score produced by the model.

A batch of alerts arrives. The model produces high-confidence classifications
for all of them. The automation executes.

Twelve of those actions revoke tokens belonging to active service accounts
in a production system. The model confused a naming pattern.
The production system begins failing.

The incident takes four hours to diagnose because the token revocations
were scattered across hundreds of automated actions in a single window.
There is no single audit record. There is a log file.

**What went wrong:**

The model's confidence score is not a verification contract.
It is a probability estimate produced by the same stochastic system
that generated the incorrect classifications.

High confidence is not the same as policy compliance.
The automation system trusted the model's self-assessment.
There was no independent verification layer.

**With ZTI:**

Each proposed action would have been classified against a declared policy
for token revocation — including constraints on which account classes
are eligible for automated revocation and what approval is required
before execution in production scope.

The service account name pattern would have triggered a constraint check.
The required approval would have been absent.
The proposals would have been rejected in enforcement mode,
or flagged without blocking in audit mode.

In either case, the sealed record of each proposal would exist.
The diagnosis is the audit log, not a forensic reconstruction.

---

## Scenario 3 — The Compliance Question You Cannot Answer

A regulated organization has been using AI-assisted automation
in its change management workflow for eight months.

An audit begins. The auditor asks:

*"For this infrastructure change on this date — what was proposed,
what policy was it evaluated against, who authorized it,
and what exactly was executed?"*

The engineering team spends three days reconstructing the answer
from Git history, CI/CD logs, Slack threads, and ticketing system entries.
The reconstruction is incomplete. Two approvals cannot be traced
to a specific artifact. One of the changes cannot be fully attributed.

The auditor notes the gap.

**What went wrong:**

The organization has good processes. They have logs. They have approvals.
What they do not have is a tamper-evident, cryptographically sealed record
of each decision — linking the proposal, the policy it was evaluated against,
the approval chain, and the artifact that executed — produced at decision time,
not reconstructed afterward.

The audit trail was assembled from sources that were not designed
to answer that specific question. None of them are authoritative alone.

**With ZTI:**

The auditor's question is answered with a single lookup:

- What was proposed: the proposal hash and content
- What policy it passed: the registry version and constraint set
- Who authorized it: the lineage record with sealed approver entries
- What executed: the decision artifact hash, which matches the execution system's record

The record was sealed at decision time. It was not assembled for the audit.
It was produced by the verification process itself.

---

## The Pattern

These three scenarios are structurally different incidents with the same root cause:

There is no execution boundary.

The proposal reaches execution without passing through a layer that enforces
a deterministic verification contract, produces a tamper-evident record,
and fails closed when the contract is not satisfied.

Guardrails shape what the model generates.
Observability records what happened.
Human review catches what it catches, at the pace it catches it.

None of these is an execution boundary.

The boundary is the missing layer.
