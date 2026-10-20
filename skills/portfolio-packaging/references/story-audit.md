# Portfolio Story Audit

Use this reference during the read-only story phase of `$portfolio-packaging`.

The purpose of this phase is to understand a mature repository well enough to describe it accurately, clearly, and professionally **before** changing the README or creating visual assets.

This is not product discovery, feature planning, or release QA. The product already exists. The task is to identify the strongest truthful story already supported by the repository.

---

## Objective

Produce a compact portfolio story that answers:

```text
Audience:
One-sentence value:
Problem solved:
Core capabilities:
Primary real proof:
Engineering evidence:
First successful action:
```

This story becomes the source of truth for later README packaging.

Do not begin visual design or rewrite the README until this audit is coherent enough to guide them.

---

## 1. Start from repository evidence

Inspect the repository read-only.

Use only the evidence needed to understand the current product, such as:

- `README.md`;
- repository tree and package/project metadata;
- current screenshots and product assets;
- current examples or sample outputs;
- current product/status/release documents;
- architecture, design, privacy, security, or technical notes when relevant;
- tests only when they support a concrete public engineering claim;
- actual user-facing workflows visible in the product or documentation.

Historical milestone documents may help explain how the product evolved, but they should not automatically define the public story.

Prefer current product behavior and current release documentation over historical implementation narratives.

If two sources materially conflict, do not silently choose one and move on. Record the conflict and avoid making the disputed claim until it is resolved.

---

## 2. Identify the audience

Ask:

```text
Who benefits from understanding or using this project?
Who is the likely first-time GitHub visitor?
Who needs to evaluate the engineering depth?
```

The audience may include more than one group, but avoid broad labels that explain nothing.

Weak:

```text
Developers
Everyone
AI users
```

Better:

```text
Language learners who need sentence-level listening practice
Analysts who need structured interpretation of social text
Developers who need a local-first token accounting tool
```

For portfolio projects, also remember the secondary evaluator:

```text
technical recruiter / hiring manager / engineer reviewing the repository
```

Do not make the recruiter the product's fake end user. The product audience and the portfolio evaluator are different roles.

---

## 3. Write the one-sentence value

The one-sentence value should explain the product in plain language.

A useful pattern is:

```text
[Product/category] helps [user] [achieve outcome] by [concrete mechanism or differentiator].
```

The sentence does not need to follow this grammar literally.

Prefer:

- concrete outcome;
- clear product category;
- one meaningful differentiator;
- language understandable without repository-specific jargon.

Avoid:

- generic adjectives such as "powerful", "innovative", "next-generation";
- "AI-powered" as the main value proposition;
- technology stacks in place of user value;
- long feature lists;
- claims that require assumptions not supported by repository evidence.

A strong one-sentence value should still make sense if the project name is removed.

---

## 4. Define the problem solved

Write the problem in one short paragraph or one to three bullets.

Focus on the user or workflow problem that makes the product necessary.

Do not turn this into market research unless the repository actually contains evidence for market claims.

Prefer:

```text
Existing workflow → concrete friction → what this project changes
```

Avoid:

```text
The industry is broken.
Millions of users need this.
This revolutionizes...
```

unless the repository contains credible evidence for those statements.

---

## 5. Select the core capabilities

Choose **3–5 capabilities** that best explain why the product matters.

A capability deserves a place in the portfolio story when it is:

- central to the intended workflow;
- visible or demonstrable;
- stable in the current release;
- useful for distinguishing the project;
- understandable to a first-time visitor.

Do not use the README as a complete feature inventory.

Prefer capability wording that describes an outcome or workflow:

```text
Analyze a single text and return structured signals
Process a batch while preserving per-item evidence
Practice sentence-level listening with repeat and review
Track local token usage across sessions
```

Avoid internal milestone wording:

```text
M7 analytics
Batch C
FCR-042
DB v10 migration
```

Internal implementation terms may appear later as engineering evidence when they genuinely matter.

If the project has many features, group closely related features under one capability.

---

## 6. Choose the primary real proof

Find the strongest artifact that makes the product immediately believable.

Priority:

```text
real current product UI
→ real current output
→ real end-to-end example
→ real workflow sequence
→ simplified architecture or process diagram
```

A primary proof should answer:

```text
What can a visitor see that proves this project actually exists and works?
```

Examples:

- a current screenshot of the main workflow;
- input and structured output shown together;
- a before/after artifact;
- a short sequence of real screens;
- a real exported result;
- a concise workflow diagram when the product is primarily infrastructural.

Prefer proof that explains the product, not merely proof that the repository contains code.

Do not use:

- fake dashboards;
- mock screenshots presented as real;
- generic stock imagery;
- decorative AI imagery;
- conceptual diagrams that could be mistaken for implemented behavior.

If conceptual material is useful, label it clearly as conceptual later in the README.

---

## 7. Extract engineering evidence

The portfolio story should expose engineering depth without turning into a development diary.

Select the strongest **3–6 engineering signals** supported by the repository.

Useful categories include:

- architecture or system boundaries;
- local-first or privacy design;
- data integrity and persistence;
- structured contracts or schemas;
- error handling and recovery;
- workflow/state management;
- batch or asynchronous processing;
- packaging or deployment design;
- testing and regression evidence;
- performance constraints;
- privacy/security boundaries;
- migration or compatibility handling;
- meaningful AI/NLP pipeline design;
- reproducibility or deterministic behavior.

An engineering signal should answer:

```text
What technical judgment or engineering work does this project demonstrate?
```

Strong:

```text
Local-first persistence with explicit export/privacy boundaries
Structured analysis contracts shared across direct and batch workflows
Regression coverage for critical state and data-integrity behavior
```

Weak:

```text
Uses Python
Uses SQLite
Uses pytest
Built with AI
```

Technology names may support the story, but they are not engineering evidence by themselves.

Do not claim test counts, benchmark results, reliability levels, security properties, or performance characteristics unless the repository currently supports them.

---

## 8. Identify the first successful action

Find the shortest path from a new user starting the project to experiencing meaningful value.

Examples:

```text
launch → paste text → analyze → inspect structured result
install → import media → select sentence → begin listening practice
launch → create collection → add entry → retrieve it
```

This is not necessarily the full core workflow.

The goal is to answer:

```text
What is the smallest real success that lets a visitor understand why this product exists?
```

This will later guide Quick Start, demo order, screenshots, and visual proof.

Avoid selecting setup steps as the "success":

```text
clone repository
create virtual environment
install dependencies
```

Those may be prerequisites, but they are not product value.

---

## 9. Separate product story from development history

Portfolio packaging should not make a new visitor reconstruct the project from milestone history.

Use milestone/history documents as evidence when needed, but translate them into current product meaning.

Example:

```text
Historical:
M8 export privacy rewrite

Portfolio meaning:
Export behavior uses explicit privacy rules and avoids exposing local-only data by default.
```

Do not publish internal milestone names as headline product capabilities unless the project is itself a development-process tool.

Preserve detailed history in its existing documentation when it remains useful.

---

## 10. Apply the claim-evidence rule

For every important public claim, ask:

```text
What repository evidence supports this?
```

Classify claims mentally as:

```text
directly demonstrated
documented and supported
reasonable description of visible behavior
uncertain / conflicting
unsupported
```

Only the first three categories should normally enter the portfolio story.

For uncertain or conflicting claims:

- report the uncertainty;
- use narrower wording;
- omit the claim until verified;
- ask the user only when the unresolved point materially affects positioning.

Never upgrade an inference into a fact because it sounds better.

---

## 11. Compress the story

After collecting evidence, reduce it.

The target is not completeness.

A good audit should usually fit into:

```text
1 audience statement
1 one-sentence value
1 concise problem statement
3–5 core capabilities
1 primary proof strategy
3–6 engineering signals
1 first-success path
```

If the story requires a long explanation before the project makes sense, simplify again.

Prefer one coherent narrative over many disconnected strengths.

---

## 12. Story quality checks

Before handing off to README packaging, verify:

### Clarity

Could a person outside the project understand the one-sentence value?

### Truthfulness

Can each major claim be traced to current repository evidence?

### Compression

Have implementation history and secondary features been removed from the main story?

### Proof

Is there at least one real artifact that can demonstrate the product?

### Portfolio value

Does the story reveal meaningful engineering work, rather than only listing technologies?

### Product integrity

Does the story describe the product that exists now, not the product that was planned or might exist later?

If any of these fail, refine the story before moving to README work.

---

## Output contract

End the audit with this structure:

```text
Portfolio Story Audit

Audience:
...

One-sentence value:
...

Problem solved:
...

Core capabilities:
1. ...
2. ...
3. ...

Primary real proof:
...

Engineering evidence:
1. ...
2. ...
3. ...

First successful action:
...

Claims deliberately excluded or narrowed:
- ...

Evidence conflicts / unresolved positioning questions:
- ...

Recommended README emphasis:
...
```

Keep `Recommended README emphasis` short. It should identify the strongest story direction, not design the README itself.

Example:

```text
Lead with the input → structured-result workflow.
Use the current result screen as primary proof.
Keep milestone history out of the opening.
Surface local-first/privacy and structured contract design in the engineering section.
```

---

## Boundary with the next phase

This reference determines **what the project story is**.

It does not determine:

- exact README section names;
- visual style;
- SVG composition;
- GIF production;
- repository metadata values;
- final presentation QA.

Those belong to later portfolio-packaging phases.

Once this story is stable, return to `SKILL.md` and continue with `references/readme-packaging.md`.
