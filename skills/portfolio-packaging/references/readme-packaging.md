# README Packaging

Use this reference after `references/story-audit.md`.

Its job is to present an already-mature project clearly on GitHub without reopening product development.

The governing rules are:

```text
README-first
minimum sufficient change
real proof before claims
product first, engineering second
```

---

## 1. Choose the smallest useful change

Do not assume every repository needs a rewrite.

### Correction

Use when the README is already strong and only needs stale wording, weak links, missing current proof, or small metadata fixes.

### Reorder and clarify

Use when the content is mostly correct but the reading order is weak.

Common symptoms:

- installation appears before product explanation;
- milestone history dominates the opening;
- internal jargon appears before plain-language value;
- proof is buried;
- capabilities are scattered;
- engineering detail overwhelms the product story.

### Portfolio redesign

Use when the README does not function as a product homepage.

Common symptoms:

- a first-time visitor cannot tell what the product does;
- there is no real proof;
- the README reads like a development log;
- core capabilities are hard to identify;
- portfolio-relevant engineering evidence is invisible.

Choose the smallest level that can produce a meaningful improvement.

---

## 2. Preserve strong existing material

Before editing, identify what should survive.

Preserve material that is:

- accurate;
- concise;
- current;
- useful to a first-time visitor;
- useful as technical evidence;
- already owned by a specialized document.

Do not rewrite good material merely to make the README feel new.

Do not remove important limitations, privacy notes, installation constraints, or compatibility information for cosmetic reasons.

Prefer:

```text
README summary
→ link to specialized document
```

over duplicating architecture, security, design, or release documentation.

---

## 3. Use information roles, not a fixed template

A README should normally cover these roles:

```text
Identity / value
Real proof
Product explanation
Core capabilities
Mechanism / workflow
Engineering evidence
First use
Limits / deeper documentation
```

A useful default flow is:

```text
Value
→ Proof
→ What it does
→ Mechanism
→ Engineering evidence
→ First use
→ Detail
```

Reorder only when the product has a stronger information need.

Examples:

- a CLI tool may put a working command earlier;
- a visual product may put screenshots immediately after the hero;
- a library may need a minimal usage example earlier than a desktop app;
- a data/research project may need one result figure before installation.

The information roles are stable. Their exact headings are not.

---

## 4. Design the opening for comprehension

Without deep scrolling, a new visitor should understand:

```text
project identity
plain-language value
what to look at next
```

The opening may contain:

- project name;
- one-sentence value;
- concise category/context;
- a strong hero;
- one current screenshot or proof board;
- a small number of useful factual badges.

Avoid openings dominated by:

- long tables of contents;
- build instructions;
- internal architecture;
- milestone history;
- dependency lists;
- badge walls;
- generic AI artwork;
- unsupported slogans.

The first screen does not need to prove everything. It needs to make the rest worth reading.

---

## 5. Lead with real proof

Use the strongest proof identified during Story Audit.

Priority:

```text
real current UI
→ real current output
→ real end-to-end example
→ real workflow sequence
→ simplified explanatory diagram
```

Prefer one strong proof over many weak screenshots.

Good proof is:

```text
current
legible
truthful
relevant
easy to interpret
```

Do not present:

- mockups as production behavior;
- stale screenshots as current UI;
- conceptual diagrams as implemented workflows without labeling them;
- decorative visuals as if they prove functionality.

If several screenshots are required, give them a clear reading order and purpose.

---

## 6. Visual evidence strategy

Visuals should have a communication job.

Useful jobs include:

- establish identity;
- show current UI;
- show input → output;
- compare before / after;
- explain sequence;
- explain architecture or boundaries;
- show several related outputs.

Default preference:

```text
real product evidence
→ deterministic project-native visual
→ meaningful motion
→ generated expressive material only when justified
```

### Hero

A custom hero is optional.

Use:

- **minimal identity hero** when the project is technical or proof follows immediately;
- **identity + proof hero** when a few real outputs remain readable at README width;
- **hero followed by proof** when screenshots are too detailed to compress;
- **no custom hero** when a Markdown heading plus strong screenshot is clearer.

Do not create a hero by default.

### Project-native direction

Derive visual treatment in this order:

```text
product semantics
→ existing product identity
→ audience expectations
→ visual finish
```

Useful sources include UI colors, logo, design tokens, screenshots, code/terminal style, charts, maps, timelines, tables, or artifacts produced by the software.

Avoid generic AI clichés such as glowing brains, neural-network particles, purple-blue gradients by default, random circuits, or robot imagery unless the project genuinely uses that identity.

### Screenshots

Before publishing a screenshot, verify:

- it reflects the current release;
- no private information is visible;
- no local paths, API keys, tokens, private URLs, or sensitive user data are exposed;
- text is readable;
- the state shown is meaningful.

Prefer completed workflow states over empty screens.

### Workflow / architecture visuals

Use a diagram only when relationships are easier to understand visually than in prose.

A README diagram should answer one public question clearly.

Do not reproduce the entire internal architecture merely because it exists.

### Motion / GIF

Use motion only when movement explains a state transition, sequence, interaction, or transformation that static proof does not explain equally well.

Do not animate for decoration.

Keep a static or textual fallback.

### Generated imagery

Generated imagery is exceptional, not normal.

Use it only when it has a clear project-specific communication role and no real product asset communicates the same idea better.

Do not use generated imagery as product proof.

---

## 7. Keep searchable information in Markdown

Keep these outside images whenever practical:

- commands;
- install instructions;
- API examples;
- configuration;
- compatibility;
- links;
- limitations;
- version requirements;
- frequently updated facts;
- contribution guidance.

Rule:

```text
If a visitor may need to copy, search, translate, or frequently update it,
keep it in Markdown.
```

Use visuals for identity, hierarchy, proof, comparison, sequence, and relationships.

---

## 8. Present product capability and engineering evidence differently

### Core capabilities

Use the 3–5 capabilities selected during Story Audit.

Write them as outcomes or workflows rather than internal milestone labels.

Prefer:

```text
Analyze a single text and inspect structured evidence
Process multiple items while preserving per-item results
Export results through explicit privacy-aware rules
```

over:

```text
Direct Mode
Batch Mode
Export Module
```

when the internal names are not self-explanatory.

If product-native mode names matter, pair them with plain-language descriptions.

### Mechanism / how it works

Explain only the mechanism needed to understand why the product behaves differently.

Possible content:

- workflow;
- processing stages;
- data flow;
- state model;
- local-first boundary;
- model/provider boundary;
- structured contract;
- plugin architecture.

Do not write a full architecture document here.

### Engineering evidence

Use the engineering signals selected during Story Audit.

Show technical judgment, not merely technology names.

Useful topics may include:

- local-first architecture;
- persistence and data integrity;
- privacy boundaries;
- schemas/contracts;
- error recovery;
- state/workflow management;
- batch processing;
- packaging/deployment;
- regression strategy;
- performance constraints;
- provider/model separation;
- reproducibility.

A tech stack may appear separately, but it should not replace engineering evidence.

---

## 9. First use and limitations

### Quick Start

Use the `First successful action` from Story Audit.

A useful structure:

```text
Prerequisite
Install / launch
One minimal action
Expected result
```

Do not front-load advanced configuration.

If installation is complicated, separate Quick Start from advanced setup.

If the repository is not intended for easy end-user installation, explain the intended evaluation path honestly.

### Limitations

Keep limitations visible when they affect user choice or interpretation.

Examples:

- platform limitations;
- supported formats/languages;
- local-only assumptions;
- provider/model requirements;
- unsupported workflows;
- packaging constraints.

Do not hide limitations to make the portfolio look stronger.

Do not turn the README into an issue tracker.

---

## 10. Existing docs and project history

When deeper documentation already exists, use navigation rather than duplication.

Possible links:

```text
Architecture → existing architecture doc
Design → existing design doc
Security/privacy → existing security/privacy doc
Contribution → existing contribution doc
Release/history → existing release/history doc
```

Do not create these files merely because they are named here.

Historical milestones may prove maturity, but they should rarely define the README.

Translate history into present-day evidence.

Instead of:

```text
M1 complete
M2 complete
...
```

prefer current engineering outcomes and capabilities.

Keep detailed milestone history in its existing source when useful.

---

## 11. Badges and public metadata

### Badges

Badges are optional.

Use only badges that communicate something useful, such as:

- CI state;
- supported runtime/version;
- license;
- release version;
- package availability.

Avoid badge walls and vanity badges.

### Repository description

Use one concise sentence describing what the product is and what it helps do.

Avoid:

```text
A Python project
AI-powered application
My portfolio project
```

### Topics

Use a small coherent set covering:

```text
domain
product category
important technical area
distinctive architecture when useful
```

Do not create a keyword cloud.

### Social preview

Create or recommend one only when it adds clear value.

Use a project hero, simplified proof composition, or clean identity board.

Do not crop a dense README screenshot.

### Homepage / demo

Use the homepage field only for a meaningful destination such as a live demo, official docs, project site, or release landing page.

Leaving it empty is acceptable.

---

## 12. Optional integrations

Read:

```text
integrations/README.md
```

when specialist Skills are installed locally.

A README-focused integration may assist with:

- visual direction;
- hero production;
- SVG;
- screenshot composition;
- workflow diagrams;
- motion/GIF;
- README-specific visual checks.

The parent `$portfolio-packaging` Skill still owns:

- portfolio positioning;
- story accuracy;
- recruiter readability;
- scope;
- change budget;
- repository metadata;
- final Portfolio QA;
- publication approval.

Provide specialists a bounded brief:

```text
Portfolio story:
Task:
Target README role:
Primary real proof:
Allowed files:
Protected files:
Known limitations:
Output expected:
```

Review specialist output before accepting it.

The specialist's output is a proposal, not automatic approval.

---

## 13. File footprint, rendering, and accessibility

Default public packaging surface:

```text
README.md
assets/readme/**
existing specialized docs when necessary
repository metadata
```

Do not automatically create:

```text
PORTFOLIO.md
SHOWCASE.md
FEATURES.md
CASE_STUDY.md
PRODUCT.md
README_DESIGN.md
```

Prefer:

```text
assets/readme/
```

for README-specific assets.

Only retain production-source subdirectories when editable sources are worth keeping.

The README should remain meaningful when an image fails.

Use:

- useful headings;
- meaningful alt text;
- adjacent Markdown context;
- visible commands and links.

Check normal GitHub width and narrow/mobile-like width.

If a visual fails at narrow width:

```text
simplify
split
enlarge critical labels
move detail to Markdown
```

Do not solve density by shrinking everything.

Check that visuals remain understandable against both light and dark GitHub surroundings.

---

## 14. Copy and claim discipline

Prefer:

- plain language;
- short paragraphs;
- concrete verbs;
- specific outcomes;
- one explanation per concept.

Remove:

- repeated promises;
- internal project-management language;
- generic marketing adjectives;
- unnecessary self-congratulation;
- vague AI terminology;
- duplicate feature descriptions.

Be careful with:

- test counts;
- performance metrics;
- accuracy/benchmarks;
- supported platforms;
- compatibility;
- release versions;
- user/adoption claims;
- privacy/security claims.

Only publish numbers that can be traced to current evidence.

If an exact number is likely to become stale and adds little, use a durable evidence statement instead.

---

## 15. Recruiter readability

Support two reading speeds.

### Fast scan

A recruiter or hiring manager should quickly see:

```text
what the product is
what it does
real proof
main capabilities
technical signal
```

### Deep inspection

An engineer should be able to continue into:

```text
mechanism
architecture
testing
privacy
technical documentation
source code
```

Do not force either audience to read everything.

---

## 16. Stop condition

README packaging is sufficient when:

- the first screen explains the project;
- proof appears early;
- core capabilities are clear;
- engineering value is visible;
- first use is discoverable;
- deeper docs remain accessible;
- no major claim lacks evidence;
- visuals improve understanding;
- additional edits would mostly be decorative or stylistic.

Stop when the remaining work no longer materially improves comprehension or professional evidence.

---

## Output contract

End this phase with:

```text
README Packaging Plan

Change level:
Correction / Reorder and clarify / Portfolio redesign

Opening strategy:
...

Primary proof:
...

Core capability presentation:
...

Mechanism / workflow:
...

Engineering evidence emphasis:
...

Quick Start strategy:
...

Existing docs to link:
...

Visual assets to add:
...

Optional integrations used:
...

Repository description:
...

Topics:
...

Social preview:
...

Homepage/demo:
...

Files to modify:
...

Files deliberately left untouched:
...
```

If edits were made, also report:

```text
README changes:
Assets added/changed:
Metadata changes proposed:
Claims narrowed or removed:
```

Do not perform publication actions from this reference.

Return to `SKILL.md` and continue to `references/portfolio-qa.md`.
