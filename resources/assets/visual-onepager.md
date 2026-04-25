# Visual One-Pager — Specification

A single diagram. The most shareable visual for ZTI.
This document describes every element needed to produce it.
A designer can build from this description alone.

---

## Canvas

Format: horizontal landscape, 16:9 ratio
Background: very dark — near-black (#090909 or equivalent)
Text: light (#e7e7e7 or equivalent)
Accent: amber/orange (#f5a623 or equivalent)
Font: monospace for labels and technical terms; sans-serif for descriptions

---

## Layout: Three Columns

The diagram has three vertical columns of equal width.
Left column: AI layer. Center column: ZTI layer. Right column: Execution layer.
A clear visual boundary line separates center from right.

---

## Left Column — AI Layer

**Header label (monospace, small, muted):** AI LAYER

**Main label (large, light weight):** AI System

**Subtext (small, muted):**
Stochastic generation
Probabilistic
Exploratory

**Visual element:** Downward arrow exiting the bottom of the column,
pointing toward the center column.

**Arrow label (small, accent color):** Proposal

---

## Center Column — ZTI Layer

**Header label (monospace, small, accent color):** ZTI LAYER

**Main label (large, light weight):** Decision Verification

**Inside the column — vertical pipeline (top to bottom):**

Six small cards, stacked vertically, each with a monospace label and one-line description:

1. REGISTRY — contract of allowed decision classes
2. DETECTION — deterministic classification
3. EXPLAINABILITY — evidence artifact
4. VALIDATION — admissibility against declared rules
5. INTEGRITY — cryptographic sealing
6. LINEAGE — provenance and approval chain

**Below the pipeline, two mode labels side by side:**
- AUDIT MODE (muted): observe and report, no execution block
- ENFORCEMENT MODE (accent): fail-closed at execution boundary

**Downward arrow exiting the bottom of the column:**
Label (accent color): Verified Decision

---

## Right Column — Execution Layer

**Header label (monospace, small, muted):** EXECUTION LAYER

**Main label (large, light weight):** Execution Systems

**Subtext (small, muted):**
Infrastructure
Databases
APIs
Automated workflows

**Visual element:** Upward-pointing blocked arrow on the left edge of this column,
meeting the boundary line. Label: Unverified proposals do not cross.

---

## The Boundary Line

A vertical line between the center and right columns.
Heavier weight than other lines. Accent color or white.

Label above the line (monospace, small, accent): EXECUTION BOUNDARY

This line is the most important visual element in the diagram.
It should be the first thing the eye finds.

---

## Bottom Bar

Full-width bar below all three columns. Dark surface, slightly lighter than background.

Left side: the canonical line in light weight sans-serif:
"AI generates. ZTI verifies. Only verified decisions execute."

Right side: monospace, muted:
bitscon/zti

---

## Pre-ZTI Contrast Panel (Optional, Recommended)

Small inset in the top-left corner or as a separate half-width panel above the main diagram.

Label (monospace, small, muted): WITHOUT ZTI

Shows the same three columns — but the center column is empty (no ZTI layer),
and a direct arrow connects AI directly to Execution with no boundary line.

Label on the direct arrow (small, muted): Unverified

This contrast makes the boundary visible by showing its absence.

---

## What This Diagram Must Communicate in Under 5 Seconds

1. There are three layers: generation, verification, execution.
2. There is a hard boundary between verification and execution.
3. Only verified decisions cross that boundary.
4. The boundary is the point — everything else is in service of it.

If a reviewer looks at the diagram for five seconds and cannot identify the boundary line,
the diagram needs to be revised. The boundary is the message.
