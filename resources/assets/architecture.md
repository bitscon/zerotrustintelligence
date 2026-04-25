# Architecture Diagrams

Reusable reference diagrams for ZTI adoption materials.
All definitions sourced from: [bitscon/zti](https://github.com/bitscon/zti)

---

## 1. Three-Tier Execution Stack

The canonical ZTI position in the execution stack.

```
AI (stochastic generation layer)
              ↓
ZTI (deterministic decision verification layer)
              ↓
        Execution systems
```

Reading: AI proposes. ZTI verifies. Only verified decisions execute.

---

## 2. Four-Tier Stack with API Layer

```
  User / API Request
          ↓
  AI System (LLM / Agent)
          ↓
  ZTI Verification Layer    ← execution boundary
          ↓
  Execution Systems
  (infrastructure, databases, APIs)
```

ZTI is applied only to high-risk, actionable execution pathways.
Not all AI interactions require verification.

---

## 3. Verification Pipeline

```
INPUT (AI Output / Proposal)
          ↓
  Pattern Registry
  (contract of allowed decision classes)
          ↓
  Detection
  (deterministic classification)
          ↓
  Explainability
  (explicit evidence artifact)
          ↓
  Validation
  (admissibility against declared constraints)
          ↓
  Integrity
  (cryptographic sealing)
          ↓
  Lineage
  (provenance and approval chain)
          ↓
  VERIFIED DECISION
```

---

## 4. Mode Model

```
┌─────────────────────────────────────────────────────┐
│  AUDIT MODE                                         │
│  Observe → Classify → Validate → Seal → Report      │
│  Does not block execution                           │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  ENFORCEMENT MODE                                   │
│  Same pipeline — execution boundary is fail-closed  │
│  Unverifiable outputs do not execute                │
└─────────────────────────────────────────────────────┘
```

---

## 5. Trust and Enforcement Boundaries

```
  AI System
      │
      │  ← Trust boundary
      ↓
  ZTI Verification Layer
      │
      │  ← Enforcement boundary
      ↓
  Execution Systems
      │
      └── Audit surface: sealed decision records + lineage entries
```

---

## 6. Integration Points

```
  API gateways        → intercept AI-generated action payloads before routing
  Agent runtimes      → wrap tool-call or action-dispatch paths
  CI/CD pipelines     → gate infrastructure proposals before apply
  Infra automation    → enforce policy before Terraform / Ansible / Pulumi execute
```
