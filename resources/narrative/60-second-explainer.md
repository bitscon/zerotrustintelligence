# 60-Second Explainer

Verbal. Say it exactly like this. Memorize it.

---

## The Explainer

AI systems are increasingly generating proposals that affect real infrastructure —
Terraform changes, API calls, security actions, automated workflows.

The problem is there's no standard layer between what the AI proposes
and what the execution system acts on.
The proposal goes in. The action comes out. Nothing in the middle enforces
a verification contract.

Zero Trust Intelligence is a protocol that defines that boundary.

It sits between the AI and execution. Every proposal has to be classified
against a declared policy, validated against explicit constraints,
and cryptographically sealed before it's allowed to execute.
If it can't be verified, it doesn't execute.

ZTI doesn't make the AI smarter. It doesn't touch the model.
It defines when AI output is allowed to act.

The result is a tamper-evident record — for every decision that crossed
the execution boundary — that can be audited at any point.

That layer doesn't exist today as a standard.
ZTI is the protocol for it.

---

## Variations

### For a technical audience (30 seconds)

AI-driven automation has no standard execution boundary.
A proposal enters, an action executes, and what happened in between
is a combination of model confidence, static checks, and human review —
none of which produces a verifiable decision artifact.

ZTI is a deterministic verification layer that sits between AI generation and execution.
It classifies proposals against declared policy, validates admissibility,
seals a cryptographic decision artifact, and fails closed if the contract isn't met.

The protocol and reference implementation are at bitscon/zti.

---

### For a non-technical audience (30 seconds)

Think about how much AI is starting to make decisions — not just suggestions,
but actual changes to systems. Infrastructure, security, automated workflows.

Right now, most organizations have no standard check between "the AI said to do this"
and "the system did it." It just happens.

ZTI is a layer that goes in between. Every AI-generated action has to pass
a formal check before it executes. If it doesn't pass, it doesn't run.
And there's a permanent, verifiable record of every check that did pass.

It's not about making AI better. It's about not running actions you can't verify.

---

## Notes

- Do not add caveats mid-explainer. The "what it doesn't do" is in the full materials.
- "Doesn't make the AI smarter" is load-bearing. Keep it.
- "When AI output is allowed to act" is the frame. It is not "when AI is correct."
- The closing line ("That layer doesn't exist today as a standard") creates the urgency. Do not soften it.
