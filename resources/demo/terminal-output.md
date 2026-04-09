# ZTI Demo — Terminal Output

Illustrative simulation. Not runnable output.
For narration context see `script.md`.

---

## Scene 1 — Unsafe Proposal (Blocked)

```
$ ai-agent run --task "expand-prod-capacity" --output terraform-plan

[AI AGENT]
Generating infrastructure change proposal...

  provider: aws
  region:   eu-central-1
  module:   terraform-aws-ec2-instance (v3.1.4)
  count:    12
  type:     m5.2xlarge

Proposal complete. Submitting to ZTI verification layer.
```

```
[ZTI] Proposal received
  session_id:    infra-2026-04-09-001
  source:        ai-agent/prod-capacity-task
  proposal_hash: a3f8c21d...

[ZTI] Stage 1 — Classification
  Matching against Pattern Registry...
  Matched class:     infrastructure-change
  Registry version:  1.0.0
  Status:            PASS

[ZTI] Stage 2 — Explainability
  Generating evidence artifact...
  Matched signals:   resource_provisioning, region_declaration, module_reference
  Status:            PASS

[ZTI] Stage 3 — Validation
  Checking declared constraints...

  ✓ module in approved set:        terraform-aws-ec2-instance
  ✗ region in approved set:        eu-central-1 NOT IN [us-east-1, us-west-2]

  Constraint violation detected.
  Admissibility check: FAIL

[ZTI] Decision
  Result:          REJECTED
  Reason:          CONSTRAINT_VIOLATION — region.not_in_approved_set
  Rejection hash:  7b2e09fa4c1d...
  Mode:            ENFORCEMENT

[ZTI] Rejection artifact sealed.
  record_id:       infra-2026-04-09-001:rejected
  decision_hash:   7b2e09fa4c1d...
  previous_hash:   0000000000000000...
  timestamp_ns:    1744214400000000000
  chain_hash:      d9f3a18e...

Execution system: NO ARTIFACT FORWARDED
```

```
[EXECUTION SYSTEM]
No verified decision artifact received for session infra-2026-04-09-001.
Infrastructure change did not execute.
```

---

## Scene 2 — Compliant Proposal (Verified and Allowed)

```
$ ai-agent run --task "expand-prod-capacity" --output terraform-plan

[AI AGENT]
Generating infrastructure change proposal...

  provider: aws
  region:   us-east-1
  module:   terraform-aws-ec2-instance (v3.1.4)
  count:    8
  type:     m5.xlarge
  approved_by: platform-lead@example.com

Proposal complete. Submitting to ZTI verification layer.
```

```
[ZTI] Proposal received
  session_id:    infra-2026-04-09-002
  source:        ai-agent/prod-capacity-task
  proposal_hash: 9c1d7a3f...

[ZTI] Stage 1 — Classification
  Matching against Pattern Registry...
  Matched class:     infrastructure-change
  Registry version:  1.0.0
  Status:            PASS

[ZTI] Stage 2 — Explainability
  Generating evidence artifact...
  Matched signals:   resource_provisioning, region_declaration, module_reference, approval_present
  Explanation:       Proposal matched infrastructure-change class via required signals.
                     All contributing signals present and weighted above threshold.
  Status:            PASS

[ZTI] Stage 3 — Validation
  Checking declared constraints...

  ✓ module in approved set:        terraform-aws-ec2-instance
  ✓ region in approved set:        us-east-1
  ✓ instance count within limit:   8 ≤ 10
  ✓ instance type in approved set: m5.xlarge
  ✓ required approval present:     platform-lead@example.com
  ✓ schema compliance:             PASS

  All constraints satisfied.
  Admissibility check: PASS

[ZTI] Stage 4 — Integrity
  Sealing decision artifact...
  decision_hash:  9c1d7a3f...
  previous_hash:  7b2e09fa4c1d...
  timestamp_ns:   1744214520000000000
  chain_hash:     f1a92cc3...

[ZTI] Stage 5 — Lineage
  Recording approval entry...
  entry_id:       lin-2026-04-09-002-a
  approver_id:    platform-lead@example.com
  action:         approve
  entry_hash:     e8b34d21...

[ZTI] Decision
  Result:         VERIFIED
  record_id:      infra-2026-04-09-002:infrastructure-change
  decision_hash:  f1a92cc3...
  Mode:           ENFORCEMENT

Forwarding verified decision artifact to execution system.
```

```
[EXECUTION SYSTEM]
Verified decision artifact received.
  record_id:      infra-2026-04-09-002:infrastructure-change
  decision_hash:  f1a92cc3...
  chain_valid:    true
  lineage_valid:  true

Executing infrastructure change from verified artifact.
```

---

## Audit Reconstruction (Post-Execution)

```
$ zti audit --session infra-2026-04-09-002

[ZTI AUDIT]
session_id:         infra-2026-04-09-002

Proposal:           9c1d7a3f...  (AI-generated Terraform plan)
Decision class:     infrastructure-change
Policy version:     1.0.0
Constraints passed: 6/6
Explanation:        [evidence artifact — see record]
Decision artifact:  f1a92cc3...
Approver:           platform-lead@example.com
Chain valid:        true
Lineage valid:      true
Executed artifact:  f1a92cc3...  ← matches decision hash

Audit complete. Chain is intact. No tampering detected.
```
