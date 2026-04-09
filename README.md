# Zero Trust Intelligence (ZTI)

## A Protocol for Verifiable AI Systems

Artificial intelligence systems produce outputs that appear intelligent.
But they are not inherently trustworthy.

Zero Trust Intelligence (ZTI) introduces a deterministic verification layer
that transforms AI outputs into provable, auditable, and tamper-evident decisions.

ZTI does not make AI smarter.

It makes AI accountable.

Zero Trust Intelligence (ZTI)
Author: Chad McCormack
© 2026 Chad McCormack
(Future ownership may be assigned to a legal entity)

*Version 1.0 — April 2026*

---

## What ZTI Is

ZTI defines a new architectural layer in modern systems:

**The Intelligence Trust Layer**

```text
AI System -> Intelligence Trust Layer -> Execution System
```

This layer does not generate intelligence.
It does not execute actions.

It enforces one rule:

**Only verified decisions are allowed to pass.**

---

## The Core Principle

No decision is trusted unless it is proven.

A decision is only valid if it is:

- Deterministically derived
- Fully explainable
- Strictly validated
- Cryptographically verifiable
- Lineage-bound to its origin

If any condition fails:

**The decision does not exist.**

---

## Architecture

ZTI transforms raw AI output into a Verified Decision through a deterministic pipeline:

```text
INPUT (AI Output)
  ↓
Pattern Registry
  ↓
Detection
  ↓
Explainability
  ↓
Validation
  ↓
Integrity
  ↓
Lineage
  ↓
VERIFIED DECISION
```

- Pattern Registry defines what is allowed.
- Detection determines what applies.
- Explainability produces a complete reasoning trace.
- Validation enforces correctness.
- Integrity locks the decision with cryptographic sealing and chaining.
- Lineage tracks origin and approval history.

---

## The Verified Decision

A Verified Decision is:

- Derived
- Explained
- Validated
- Sealed
- Traceable

Only Verified Decisions are allowed to cross system boundaries.

Everything else is discarded.

---

## Determinism as a Requirement

ZTI systems are:

- Deterministic
- Schema-bound
- Fully reproducible

There is:

- No randomness
- No implicit behavior
- No hidden state

If a result cannot be reproduced:

It is invalid.

---

## Fail-Closed Systems

ZTI does not degrade gracefully.

It fails deliberately.

If verification cannot be completed:

**The decision is rejected.**

This prevents uncertainty from entering execution systems.

---

## Cryptographic Decision Chains

Each decision is recorded as a tamper-evident record:

- Decision hash
- Previous hash
- Timestamp
- Version

If any record is altered:

The entire chain becomes invalid.

---

## Simple Example

```python
from zti import (
    DEFAULT_REGISTRY,
    Interaction,
    InteractionBundle,
    detect_patterns,
    explain_patterns,
    create_decision_record,
    validate_chain,
)
from zti.serialization import serialize_explanation_artifact

bundle = InteractionBundle(
    session_id="session-001",
    interactions=(
        Interaction("i-001", ("open_question_density",), 10),
        Interaction("i-002", ("option_space_expansion",), 20),
        Interaction("i-003", ("hypothesis_generation",), 30),
    ),
)

patterns, _, err = detect_patterns(bundle, DEFAULT_REGISTRY)
assert err is None and patterns

artifacts, _, err = explain_patterns(tuple(patterns), DEFAULT_REGISTRY)
assert err is None and artifacts

record, err = create_decision_record(
    record_id="session-001:exploratory",
    decision_data=serialize_explanation_artifact(artifacts[0]),
    previous_record=None,
)
assert err is None

valid, err = validate_chain((record,))
assert valid is True and err is None
```

---

## What ZTI Is Not

ZTI does not:

- Improve AI accuracy
- Replace AI models
- Execute actions
- Provide autonomy
- Act as an agent framework

ZTI is a constraint system.

It enforces trust boundaries on intelligence.

---

## Where This Matters

ZTI becomes critical anywhere decisions have consequences:

- Infrastructure automation
- Security enforcement
- Financial systems
- Compliance and audit pipelines
- Autonomous systems

As systems become more automated, verification becomes non-optional.

---

## Install

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/bitscon/zerotrustintelligence
cd zerotrustintelligence
python3 -m pip install -e .
```

Run the test suite locally with:

```bash
python3 -m pytest -q
```

---

## Examples

Reference examples are available in [`examples/`](examples/).

---

## Whitepaper

Full protocol specification:

[`whitepaper/zti-whitepaper.md`](whitepaper/zti-whitepaper.md)

---

## Site

Landing page:

[`site/index.html`](site/index.html)

---

## License

MIT License
