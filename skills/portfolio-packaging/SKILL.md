---
name: portfolio-packaging
description: >-
  Package a mature, post-RC software repository into a clear, evidence-driven, recruiter-readable GitHub portfolio project. Use when product development, hardening, and release-candidate work are already complete and the remaining work is presentation: portfolio story, README structure, real proof, repository metadata, optional specialist integrations, presentation QA, and safe handoff. Do not use this Skill as a substitute for product development, hardening, release engineering, or feature work.
---

# Portfolio Packaging

Turn a technically finished repository into a portfolio-ready GitHub project without reopening product development.

## Core principles

1. **README-first**  
   Treat `README.md` as the primary product homepage and navigation layer.

2. **Minimum sufficient change**  
   Make the smallest set of changes that materially improves clarity, evidence, and professional presentation.

3. **Real proof before claims**  
   Prefer current screenshots, outputs, workflows, examples, and existing engineering evidence over marketing language or decorative visuals.

4. **Product first, engineering second**  
   First help a new visitor understand the product. Then expose enough engineering depth for a technical reviewer to evaluate it.

## Scope gate

Assume the target repository is already:

- feature complete for the intended release;
- through product hardening;
- through release-candidate validation;
- ready for post-RC packaging.

Do not independently reopen engineering work unless the user explicitly changes scope.

By default, do **not**:

- add features;
- fix application bugs;
- refactor product code;
- redesign product architecture;
- change product behavior;
- expand test coverage;
- reopen hardening or release engineering;
- create documentation merely for completeness.

If packaging reveals a mismatch between a public claim and actual product behavior, correct or narrow the claim. Do not silently change the product to make the claim true.

## Default change budget

Editable by default:

```text
README.md
assets/readme/**
repository presentation metadata
```

Conditional:

```text
existing specialized documentation
```

Modify specialized documentation only when it is materially stale, contradicts the current release, or must change to support an accurate README link.

Protected by default:

```text
src/**
app/**
tests/**
database/**
migrations/**
product configuration that changes behavior
```

Broader changes require explicit authorization.

## Workflow

### 0. Start read-only

Inspect enough of the repository to understand the current product:

- existing `README.md`;
- repository tree and package/project metadata;
- current screenshots and assets;
- current examples and outputs;
- relevant product, architecture, design, privacy, security, status, or release documents.

Preserve unrelated user changes.

Do not commit, push, publish, merge, rename, or change repository visibility without explicit authorization.

### 1. Build the portfolio story

Read:

```text
references/story-audit.md
```

Produce:

```text
Audience:
One-sentence value:
Problem solved:
Core capabilities:
Primary real proof:
Engineering evidence:
First successful action:
```

Do not invent capabilities, benchmarks, adoption, compatibility, testimonials, or engineering properties.

### 2. Package the README

Read:

```text
references/readme-packaging.md
```

Choose the smallest meaningful change:

```text
Correction
Reorder and clarify
Portfolio redesign
```

Use the portfolio story as the source of truth.

A useful default information flow is:

```text
Value
→ Proof
→ What it does
→ Mechanism
→ Engineering evidence
→ First use
→ Detail
```

This is an information sequence, not a fixed template.

### 3. Use optional integrations when useful

Read:

```text
integrations/README.md
```

Third-party integrations are optional local capability providers.

When a specialist is available:

1. inspect only the candidate relevant to the current task;
2. read its own instructions;
3. delegate a bounded responsibility;
4. review its output against the parent portfolio story and change budget;
5. return control to this parent workflow.

The core Skill must remain useful when no integrations are installed.

Default visual priority:

```text
real product evidence
→ deterministic project-native visuals
→ meaningful motion
→ generated expressive material only when justified
```

### 4. Package repository presentation

Continue using:

```text
references/readme-packaging.md
```

Review, when applicable:

- repository description;
- topics;
- social preview;
- homepage/demo link;
- README navigation to deeper technical documentation.

Use concise, factual metadata. Do not fill optional fields merely for completeness.

### 5. Run portfolio QA

Read:

```text
references/portfolio-qa.md
```

This is **presentation QA**, not product QA.

A first-time visitor should be able to answer:

```text
What is this?
Who is it for or what problem does it solve?
What can it actually do?
What real proof should I look at?
What engineering ability does this project demonstrate?
Where do I go next if I want to try or inspect it?
```

If QA finds a packaging failure, return only to the smallest relevant packaging step.

Do not reopen unrelated engineering phases.

### 6. Preview, diff, and hand off

Before external publication actions:

- show or summarize the proposed README result;
- show the relevant diff;
- list added or changed assets;
- list proposed metadata changes;
- report unresolved presentation issues;
- state which files were deliberately left untouched.

Do not commit, push, open a PR, merge, publish, change visibility, or edit public metadata until the user explicitly authorizes the relevant action.

## Documentation policy

Do not expand repository documentation by default.

Prefer:

```text
README.md
+ existing specialized docs
+ only the visual assets required by the README
```

Do not automatically create:

```text
PORTFOLIO.md
SHOWCASE.md
FEATURES.md
CASE_STUDY.md
PRODUCT.md
ARCHITECTURE.md
DESIGN.md
```

If a specialized document already owns deep technical content, link to it rather than duplicating it.

## Quality bar

A successful result should satisfy all of the following:

- the first screen explains the project without prior context;
- real evidence appears early;
- the README is clearer, not merely more decorated;
- milestone history does not define the public story;
- engineering depth is visible without overwhelming product understanding;
- visuals have a communication job;
- the repository does not look forced into a generic template;
- no capability is invented or exaggerated;
- no unrelated product code is changed;
- optional integrations remain optional;
- the result is ready for user review before publication.

## Handoff summary

End a packaging pass with:

```text
Portfolio story:
README changes:
Visual assets:
Repository metadata:
Presentation QA:
Known limitations / unresolved items:
Files intentionally untouched:
Recommended next action:
```

## Invocation examples

```text
Use $portfolio-packaging to package this post-RC repository for a public GitHub portfolio. Start read-only, preserve product code, and show me the README/asset diff before any push or publication.
```

```text
Use $portfolio-packaging to audit this mature repository for portfolio readiness. Do not edit anything yet.
```

```text
Use $portfolio-packaging to improve the README and repository presentation only. Use available local integrations when they add real value, but keep third-party source outside the public repository.
```
