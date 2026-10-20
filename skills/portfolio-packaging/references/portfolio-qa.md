# Portfolio QA

Use this reference after the portfolio story and README packaging are stable.

This is **presentation QA**, not product QA.

Its job is to answer:

```text
Can a stranger quickly understand the project,
see real evidence,
recognize meaningful engineering work,
and trust what the repository claims?
```

If not, return only to the smallest relevant packaging step.

Do not reopen product development, hardening, release engineering, or architecture unless the user explicitly changes scope.

---

## 1. Reconfirm QA scope

Review:

```text
README.md
assets/readme/**
repository presentation metadata
relevant existing specialized docs
```

Do not treat QA as authorization to modify:

```text
src/**
app/**
tests/**
database/**
migrations/**
product behavior
```

If review exposes a real product defect, report it separately as out of scope.

---

## 2. 30-second comprehension gate

From the perspective of a visitor with no prior project context, answer:

```text
What is this?
Who is it for or what problem does it solve?
What can it actually do?
What real proof should I look at?
What engineering ability does this project demonstrate?
Where do I go next if I want to try or inspect it?
```

Classify:

```text
PASS
PARTIAL
FAIL
```

### PASS

The opening, proof, capability hierarchy, and technical signals answer these questions without requiring project-history reconstruction.

### PARTIAL

The project is understandable, but one or two important answers require too much scrolling, jargon decoding, or inference.

### FAIL

A new visitor cannot confidently determine product value, proof, or engineering significance.

A FAIL returns to README packaging.

---

## 3. Story, claim, and proof gate

Verify that the final README remains consistent with the Story Audit:

```text
Audience
One-sentence value
Problem solved
Core capabilities
Primary real proof
Engineering evidence
First successful action
```

Check every major public claim against current repository evidence.

Pay special attention to:

- core capabilities;
- supported platforms/languages/formats;
- privacy/security/local-first claims;
- reliability/testing claims;
- model/provider claims;
- compatibility and release/version claims;
- benchmarks, accuracy, performance, or adoption numbers.

Classify questionable claims as:

```text
SUPPORTED
TOO BROAD
STALE
CONFLICTING
UNSUPPORTED
```

Default correction:

```text
narrow wording
remove stale claim
report conflict
omit unsupported claim
```

Do not keep a claim because it improves marketing.

Verify that the primary proof is:

```text
current
legible
truthful
relevant
properly described
```

Flag mockups presented as real, stale screenshots, conceptual diagrams presented as implementation, or decorative imagery presented as functional proof.

---

## 4. Product and engineering hierarchy gate

The README should support two reading speeds.

### Fast product scan

A recruiter or general visitor should quickly find:

```text
what it is
what it does
real proof
main capabilities
```

### Technical inspection

An engineer should be able to continue into:

```text
mechanism
engineering evidence
architecture
testing
privacy
source
specialized docs
```

Flag either extreme:

```text
too shallow:
marketing with no engineering evidence

too deep:
internal documentation with no accessible product story
```

Check that approximately 3–5 core capabilities receive clear priority.

Engineering evidence should demonstrate technical judgment, not only list technologies.

---

## 5. First-use and limitation gate

Verify that Quick Start or the evaluation path matches the `First successful action` from Story Audit.

Check:

- prerequisites are honest;
- commands are copyable;
- ordering is clear;
- advanced setup is not front-loaded;
- expected result is understandable.

If the project is not intended for easy end-user installation, the README should state the intended evaluation path honestly.

Verify that material limitations affecting user choice or interpretation remain visible.

Do not hide limitations for cosmetic reasons.

Do not turn the README into an issue tracker.

---

## 6. Visual, rendering, and accessibility gate

For every retained visual, ask:

```text
What does this help the visitor understand?
```

Valid jobs include:

- identity;
- proof;
- comparison;
- sequence;
- architecture;
- system boundary;
- output variety.

Flag visuals that are:

- generic decoration;
- redundant;
- more dominant than the product;
- inconsistent with project identity;
- too dense to interpret;
- misleading.

Check screenshots and raster assets for accidental disclosure:

- personal names/emails;
- usernames;
- local filesystem paths;
- API keys/tokens;
- private URLs;
- real customer/user data;
- unredacted personal messages;
- machine-specific information.

Check image references:

- local files exist;
- paths and filename case are correct;
- major images have useful alt text;
- no obsolete asset remains referenced.

Check normal GitHub width and narrow/mobile-like width.

Essential text, screenshots, and diagrams should remain understandable without zooming.

Check that visuals remain readable against both light and dark GitHub surroundings.

If GIF/motion is present, verify that it explains something meaningful and has a static or textual fallback.

If generated imagery is present, verify that it is not being used as product proof and does not overpower real evidence.

---

## 7. Links and metadata gate

Check important public links:

```text
installation / release
documentation
demo
architecture/design/security docs
license
external dependency or integration references
```

Flag:

- broken links;
- links to private resources;
- local filesystem paths;
- placeholder URLs;
- inaccessible evaluation paths.

Verify repository metadata:

### Description

Concise, factual, and aligned with README positioning.

### Topics

Small, coherent, relevant set. No keyword dump.

### Social preview

If present, it should identify the project and remain legible at small size.

### Homepage/demo

If present, the destination should be meaningful and current.

Leaving optional fields empty is acceptable.

---

## 8. Integration and diff-scope gate

If optional integrations were used, verify that:

- third-party source did not accidentally enter the public repository;
- local integration directories remain ignored;
- third-party work is not presented as original work;
- required license/attribution obligations are respected;
- the parent workflow remains understandable without the integration;
- the specialist did not change unrelated files.

Inspect the actual packaging diff.

Look for:

- unrelated file changes;
- formatting churn;
- deleted useful documentation;
- stale generated assets;
- temporary files;
- local environment files;
- third-party source accidentally tracked;
- unexpected product-code edits.

The final diff should match the declared packaging scope.

Also record files deliberately left untouched, such as product code, tests, database, release configuration, or historical milestone records.

---

## 9. Issue severity and stop rule

Classify remaining findings:

### Blocker

Publication would materially mislead, expose sensitive information, break the evaluation path, or fail basic comprehension.

Examples:

- unsupported major claim;
- exposed secret/private data;
- missing primary proof asset;
- broken README image paths;
- first-time visitor cannot understand the product;
- public link points to private/inaccessible material.

### Significant

The project is understandable, but professional presentation is meaningfully weakened.

Examples:

- important screenshot too small;
- repository description inconsistent;
- Quick Start unclear;
- major engineering evidence buried;
- unnecessary visual clutter.

### Minor

Cosmetic or low-impact issue.

Examples:

- small wording refinement;
- optional topic improvement;
- nonessential spacing.

Only Blockers automatically prevent handoff for publication.

Significant issues should normally be fixed when the cost is small and the benefit is clear.

Minor issues should not trigger endless polishing.

Stop when:

- no Blocker remains;
- the 30-second test passes;
- claims are supported;
- proof is visible;
- metadata is coherent;
- the public evaluation path works;
- remaining issues are minor or consciously deferred.

---

## 10. Publication gate

Passing Portfolio QA does **not** authorize external actions.

Before any of the following:

```text
commit
push
open PR
merge
publish
change repository visibility
make repository public
edit public metadata
```

obtain explicit user authorization for the relevant action.

When approval is not yet granted, stop at preview + diff + recommendations.

---

## Output contract

End Portfolio QA with:

```text
Portfolio QA

30-second comprehension:
PASS / PARTIAL / FAIL

Story / claim / proof consistency:
PASS / PARTIAL / FAIL

Product / engineering hierarchy:
PASS / PARTIAL / FAIL

First use / limitations:
PASS / PARTIAL / FAIL

Visual / accessibility / privacy:
PASS / PARTIAL / FAIL

Links / metadata:
PASS / PARTIAL / FAIL

Integration / diff scope:
PASS / PARTIAL / FAIL

Blockers:
- ...

Significant issues:
- ...

Minor / optional improvements:
- ...

Files intentionally untouched:
- ...

Overall result:
READY FOR USER APPROVAL
or
RETURN TO README PACKAGING

Recommended next action:
...
```

If the result is `RETURN TO README PACKAGING`, identify the smallest corrective pass required.
