# ZTI / ZTAP Alignment

*Keeping the doctrine and the protocol conceptually locked together*

---

## Purpose

ZTI is the doctrine. ZTAP is the first open protocol that implements that doctrine for
governed agent transactions. For the ecosystem to be coherent, these two must remain
conceptually aligned: every principle stated in ZTI doctrine must have a clear and
consistent expression in ZTAP, and every ZTAP protocol decision must be traceable to a
ZTI principle.

This document defines that alignment, the shared invariants across both repos, and
the rules that prevent the two from drifting apart.

---

## Core Relationship

```
ZTI doctrine
  └── ZTAP open protocol      ← first open protocol under ZTI doctrine
        └── ZTI Core           ← one commercial control-plane implementation of ZTAP
```

| Layer | Repository | Purpose |
|---|---|---|
| **ZTI** | `bitscon/zti` | Doctrine, governing principles, reference library, threat model |
| **ZTAP** | `bitscon/ztap` | Open transaction protocol, schema, conformance, examples |
| **ZTI Core** | private/commercial | Commercial control-plane implementation — not in either doctrine repo |
| **ZTI Adoption** | `bitscon/zti-adoption` | Public education and marketing — not authoritative |

**ZTI defines the why. ZTAP defines the how. ZTI Core defines one product. ZTI Adoption explains the story.**

---

## Concept Map

| ZTI Doctrine Concept | ZTAP Protocol Expression | Notes |
|---|---|---|
| AI output is not a decision | `transaction_request` exists in `created` state; no action taken until control plane authorizes | The envelope captures the proposal; the authorization decision is the governance artifact |
| Models draft; deterministic systems govern | Control plane evaluates policy deterministically; `authorization_status` is the outcome; model confidence is not part of evaluation | The AI can initiate a request; only the control plane can authorize it |
| Trust must be proven, not assumed | "ZTAP does not secure the pipe. ZTAP governs the action." Transport security ≠ transaction authorization; authorization record required | An arrival over a secure channel is not an authorized transaction |
| Verified Decision | `authorization_decision` with `auto_authorized` or `human_approved` status, `policy_refs`, valid `integrity.hash_value` | The decision is the sealed authorization record, not the AI's output |
| Integrity / sealing | `integrity` object on every envelope: RFC 8785 JCS canonicalization + SHA-256 hash of content | Hash of `hash_value` excluded; all other integrity fields included; tamper-evident |
| Lineage / provenance | Hash chain: `request_hash` in every `authorization_decision`, `execution_receipt`, `evidence_record`; append-only audit log | Each envelope references the immutable original request; modifications detectable |
| Audit trail | Append-only, hash-linked control plane audit log; every envelope and receipt retained and queryable | A log records; an audit trail proves |
| Execution boundary | Level 3 (Governed Executor) conformance: must refuse work without valid, unexpired ZTAP authorization record, regardless of transport | The enforcement boundary is at the point of action, not at the network perimeter |
| Fail-closed enforcement | Protocol invariant: missing/invalid/expired authorization = reject; no permissive fallback; `SCHEMA_INVALID`, `ACTOR_UNREGISTERED`, `EXPIRED`, `INTEGRITY_FAILED` | Fail-closed is not a default setting — it is an invariant |
| Pattern Registry | Actor registry + capability registry in the control plane; `registration_ref` on every actor | Defines what classes of action are allowed; closed, explicit |
| Detection (classification) | Control plane evaluates `requested_action.action_type` and `profile` against policy; routes to correct policy evaluation | Deterministic: no inference, no probability |
| Explainability | `policy_refs` and `reason_codes` in `authorization_decision`; `evidence_refs` linking accepted evidence | Every authorization decision records its policy basis |
| Validation | Schema validation, `capability_claims` matching, `requested_capabilities` subset check, integrity hash verification | Admissibility check against declared constraints |
| Human approval | `human_approval_required` → `human_approved` two-envelope flow; `approval_scope` binding (`transaction_id`, `request_hash`, `action_ids`, `target_actor_id`, `expires_at`, `single_use: true`) | Approval is transaction-specific, action-bound, time-limited, single-use by default |
| Break-glass | Break-glass path is governed authorization with elevated evidence; `break_glass_context` on request; incident ref, named approver, compensating controls, post-incident review required | More evidence than standard, not less; no bypass mode |
| Governance-class changes | Governance transactions (actor registration, capability grant, policy modification) require elevated authorization; never auto-authorized | Changes to governance rules are the highest-risk transaction class |
| Evidence / receipts | `evidence_record` envelope type; `execution_receipt` with `verification_results`, `atomicity_result`, `actions_completed` | Every terminal transaction state produces a receipt; no receipt = non-compliant |
| Control plane | ZTAP Control Plane (Level 2 conformance): evaluates policy, issues authorization records, maintains audit trail; does not execute | The entity that governs does not execute; the entity that executes does not self-authorize |
| Policy | `policy_refs` array in `authorization_decision`; determines `authorization_status`; organizational policy is external to the protocol | Policy quality matters; ZTI/ZTAP enforce declared constraints, not policy correctness |
| Registered actors / capabilities | `actor_id`, `role`, `capability_claims`, `registration_ref`, `organization_id` in actor objects; separate registry at the control plane | Roles are governance classifications; `implementation_ref` is metadata, not authority |
| Deterministic verification | Schema validation is machine-verifiable; capability matching is deterministic; `reason_codes` are structured enumerations | No heuristic, no inference, no model judgment in authorization evaluation |

---

## Shared Invariants

These principles must always remain true across both the ZTI doctrine and the ZTAP protocol.
If either repo introduces content that contradicts any of these, it introduces misalignment.

1. **AI output is proposal, not authority.** A model's output, however confident or capable,
   is a candidate. It does not become a decision until it has passed through a deterministic
   verification layer.

2. **Models draft. Deterministic systems govern.** The generation process does not need to be
   deterministic. The governance layer does.

3. **Integrity is mandatory.** Every governed artifact must be hashable, tamper-detectable,
   and verifiable. Encryption is policy-conditional; integrity is not.

4. **Encryption is policy-conditional, not protocol-mandatory.** ZTAP envelopes are plain JSON
   by default and must be human-auditable without decryption. Organizations may layer encryption
   on top; the protocol does not require it.

5. **Execution must verify authorization at the point of action.** Transport security does not
   substitute for an authorization record. The enforcement boundary is at the action, not at
   the network.

6. **Roles are governance classifications, not tool or vendor names.** Tool names, model names,
   SaaS product names, and vendor identifiers are not protocol roles. Using implementation
   identity as role identity makes governance vendor-dependent.

7. **The control plane governs; executors execute.** These are permanently separate. The
   entity that governs does not execute. The entity that executes does not self-authorize.

8. **Ungoverned messages may exist, but cannot become accepted governed work.** A ZTAP-compliant
   executor refuses ungoverned instructions regardless of their origin. Ungoverned messages
   do not automatically become authorized by arriving via a trusted channel.

9. **Fail-closed is an invariant, not a default.** Ambiguity resolves to denial. There is no
   permissive fallback mode.

10. **Receipts and evidence are required for governed outcomes.** An action that produces no
    receipt is not a governed action. Governance requires evidence.

---

## Terminology Rules

### Use in public doctrine docs

| Preferred term | Where it appears |
|---|---|
| Zero-Trust Intelligence | Full name; use in formal contexts |
| ZTI doctrine | The governing philosophy |
| ZTAP protocol | The Zero Trust Agent Protocol |
| ZTAP transaction | The full governed unit of work |
| ZTAP envelope | The serialized JSON object carrying a transaction event |
| ZTAP receipt | The result envelope at a terminal state |
| control plane | The authority layer that evaluates policy and issues authorization records |
| actor | Any entity participating in a ZTAP transaction |
| role | A protocol-level governance classification |
| capability | A declared, registered ability an actor can exercise |
| evidence | Supporting material submitted to satisfy a policy requirement |
| integrity | Tamper detection via hash; mandatory in both ZTI and ZTAP |
| verified decision | ZTI concept: an AI proposal that has passed deterministic verification |
| authorization record | ZTAP concept: the `authorization_decision` envelope issued by the control plane |

### Avoid in public doctrine docs

| Avoid | Reason |
|---|---|
| `barn-first` | Internal infrastructure terminology; not meaningful to external readers |
| `barn`, `workshop`, `homestead` | Local development environment names; confusing and internal |
| `single-source workflow` | Internal build methodology; irrelevant to doctrine |
| Billy-specific language | Billy is a possible future reference case, not a protocol authority |
| Tool names as roles (`codex`, `claude`, `gpt-4`, etc.) | Protocol roles must be product-neutral |
| Implying ZTI Core is already part of this repo | ZTI Core is separate; the open library is here, not ZTI Core |
| Implying ZTAP replaces MCP or A2A | ZTAP complements; it does not compete with or replace |
| Implying encryption is mandatory | Integrity is mandatory; encryption is policy-conditional |
| `bitscon/zerotrustintelligence` URLs | Stale after rename; update to `bitscon/zti` |
| Overpromising future protocol versions | ZTAP v1.0-draft is the current state; do not commit to unspecified future work |

---

## ZTI vs ZTAP Boundary

ZTI and ZTAP describe related but distinct things. They must not be collapsed.

**ZTI describes:**
- Why verification is necessary (the doctrine problem)
- The architectural concept of a decision verification layer
- What a Verified Decision is
- The verification pipeline: Pattern Registry → Detection → Explainability → Validation → Integrity → Lineage
- The threat model
- What the `zti` reference library implements

**ZTAP describes:**
- How governed agent transactions are structured (the protocol solution)
- The transaction lifecycle (created → submitted → evaluated → authorized → ...)
- Specific envelope types and field definitions
- Conformance levels and test criteria
- How the control plane contract is defined
- How hashes are computed and verified
- Reason codes and evidence types

**The line:** ZTI says "verify before execution." ZTAP says "here is the exact structure of how that verification is requested, authorized, executed, and receipted for agent transactions."

Do not describe ZTAP in the ZTI doctrine repo as if ZTAP is the entirety of ZTI. ZTAP implements one layer of ZTI for one domain (agent transactions). ZTI is broader.

Do not describe ZTI in the ZTAP protocol repo as if ZTAP and ZTI are interchangeable terms. Reference ZTI as the doctrine that ZTAP implements.

---

## ZTI Core Boundary

ZTI Core is a separate commercial product. It is not part of the ZTI doctrine repo or the ZTAP protocol repo.

**The ZTI doctrine repo may:**
- Mention ZTI Core by name as a commercial control-plane implementation
- Link to ZTI Core when it has a public URL
- Describe the conceptual role of a commercial control plane (without ZTI Core's private details)

**The ZTI doctrine repo must not:**
- Contain ZTI Core product code
- Describe ZTI Core pricing, seat models, or private roadmap
- Define ZTI Core's private API as if it were the open protocol
- Make any claim that implies ZTI Core is the only compliant control plane

**The ZTAP protocol repo may:**
- Describe ZTI Core as one possible control-plane implementation of ZTAP
- State that ZTAP is open and any conformant control plane may implement it

**The ZTAP protocol repo must not:**
- Reference ZTI Core internals
- Tie conformance requirements to ZTI Core-specific behavior

---

## Adoption Site Boundary

The adoption site (`bitscon/zti-adoption`) is the public education and marketing surface.
It should be updated after the ZTI and ZTAP repos are clean and aligned.

The adoption site:
- consumes the ZTI and ZTAP doctrine, not the other way around
- is contextual and illustrative, not authoritative
- must not drift into defining protocol terms that conflict with ZTI or ZTAP definitions
- should be updated as the final step after repo cleanup and rename are complete

---

## Open Alignment Risks

The following items require operator decision or monitoring to maintain alignment:

| Risk | Location | Status |
|---|---|---|
| Old `bitscon/zerotrustintelligence` URLs in `resources/outreach/` | `resources/outreach/posts.md`, `enterprise.md`, `pilot.md`, `resources/deck/slides.md`, `resources/narrative/60-second-explainer.md` | Not yet updated. These files are scheduled for `zti-adoption` or archive. Update before any external use. |
| `resources/principles/boundary.md` perspective confusion | `resources/principles/boundary.md` | Partially addressed. The file was authored from the adoption site's perspective. Context note added. |
| Schema `$id` URLs | `schemas/audit_report.json`, `schemas/verification_trace.json` | Still reference `bitscon.github.io/zerotrustintelligence/`. Update after GitHub rename. |
| `pyproject.toml` repo URL | `pyproject.toml` | May reference old repo name. Verify and update as part of Phase 2 URL sweep. |
| ZTI whitepaper does not mention ZTAP | `whitepaper/zti-whitepaper.md` | The whitepaper predates ZTAP. It is accurate ZTI doctrine but has no ZTAP reference. A single paragraph addition acknowledging ZTAP as the first protocol under ZTI doctrine would close this gap. Operator decision: add or leave for next pass. |
| `resources/assets/architecture.md` old URL | `resources/assets/architecture.md` | References `bitscon/zerotrustintelligence`. Scheduled for URL sweep. |
