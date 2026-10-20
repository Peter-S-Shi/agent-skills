# Integrations

This directory is the local integration boundary for `$portfolio-packaging`.

Integrations are **optional third-party capability providers**. They may extend the parent Skill with specialized work such as README visual design, SVG production, screenshot composition, diagrams, motion, or other packaging tasks.

They are not part of the core `portfolio-packaging` implementation.

> Integrate capabilities, not third-party source.

---

## 1. Ownership boundary

The parent Skill owns:

```text
portfolio positioning
story accuracy
scope control
README-first policy
minimum sufficient change
repository metadata
presentation QA
publication approval
```

A specialist integration owns only the bounded task delegated to it.

Use this separation:

### Parent

```text
What should this project communicate?
Why is it portfolio-worthy?
What evidence should lead?
What files may change?
What public claims are justified?
Does the final repository pass presentation QA?
```

### Specialist

```text
How should this bounded presentation task be executed well?
```

An integration must not become the de facto parent workflow.

---

## 2. Local-only installation model

A local working copy may look like:

```text
integrations/
├── README.md
├── .gitignore
│
├── beautify-github-readme/
├── another-specialist/
└── ...
```

Only the integration policy files are intended to be tracked by this repository.

Installed third-party integrations remain local and Git-ignored by default.

Benefits:

- clear authorship boundaries;
- simpler license compliance;
- easier upstream updates;
- no unnecessary duplication;
- lower maintenance burden;
- cleaner public Git history;
- less risk that third-party work is mistaken for original work.

The parent Skill must remain useful when no third-party integration is installed.

---

## 3. Integration contract

When the parent Skill may benefit from a specialist, use:

```text
Discover
→ Inspect
→ Match
→ Delegate
→ Review
→ Return
```

### Discover

Inspect locally installed integration directories only when the current task may benefit from a specialist.

Do not load every integration by default.

### Inspect

Read the candidate's own primary instructions, such as:

```text
SKILL.md
README.md
relevant references required by that Skill
```

Do not infer behavior from the directory name.

### Match

Confirm that the integration's real capability matches the current bounded task.

Examples:

```text
README visual redesign
SVG hero production
workflow diagram
screenshot composition
GitHub-safe motion
```

Do not use a specialist merely because it is installed.

### Delegate

Give a bounded brief:

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

Delegate the smallest coherent task that benefits from specialist expertise.

### Review

Treat the specialist result as a proposal.

Verify:

- factual claims;
- consistency with the Portfolio Story Audit;
- README-first compatibility;
- real-proof priority;
- file-scope compliance;
- visual usefulness;
- license/attribution obligations;
- absence of unrelated changes.

Reject or simplify output that increases decoration without improving communication.

### Return

After the delegated task is complete, return control to `$portfolio-packaging`.

The parent still owns:

```text
final README coherence
repository metadata
Portfolio QA
diff review
user approval
publication handoff
```

---

## 4. Optional means optional

No integration may become an undeclared hard dependency.

If a preferred specialist is unavailable:

1. continue with the parent Skill when practical;
2. produce a simpler result;
3. identify the optional enhancement that could be added later;
4. do not block basic portfolio packaging merely because a specialist is missing.

A valid installation may contain only:

```text
integrations/
├── README.md
└── .gitignore
```

---

## 5. Third-party, license, and Git boundary

Each integration keeps its own license and copyright terms.

Before redistribution, copying, modification, or publication of third-party material:

1. inspect the current license;
2. identify the material being copied;
3. preserve required copyright/license notices;
4. comply with redistribution or attribution requirements;
5. keep third-party ownership distinguishable from original work.

Third-party material may include:

```text
source code
SKILL.md
README text
reference documents
scripts
examples
visual assets
templates
```

Source-code separation alone is not enough.

Prefer:

```text
reference the external integration
→ let it keep its own instructions
→ delegate bounded work
```

rather than copying substantial third-party content into the parent Skill.

Expected tracked files:

```text
integrations/README.md
integrations/.gitignore
```

Expected untracked local content:

```text
integrations/<third-party-skill>/**
```

Before publication, verify that no local third-party directory has entered the Git diff.

This directory grants no additional rights over third-party integrations.

---

## 6. Permissions and external actions

A third-party integration does not inherit unlimited permission over the target repository.

The delegation brief should define:

```text
Allowed files
Protected files
External actions allowed
External actions forbidden
```

A common packaging delegation may allow:

```text
README.md
assets/readme/**
```

while protecting:

```text
src/**
tests/**
database/**
application behavior
```

If the integration requests broader changes, return to the parent Skill or user for authorization.

Do not let an integration independently:

- commit;
- push;
- open a PR;
- merge;
- publish;
- make a repository public;
- change repository visibility;
- submit the user's project to an external showcase;
- add promotional attribution;

unless the user explicitly authorizes that specific action.

Functional license obligations remain separate from optional promotional attribution.

---

## 7. Example: beautify-github-readme

`beautify-github-readme` is a suitable optional specialist for README presentation and visual packaging.

A local installation may appear as:

```text
integrations/
└── beautify-github-readme/
```

Potential delegated responsibilities:

```text
README visual direction
project-native hero
SVG assets
proof-board composition
workflow diagrams
optional meaningful motion
README-specific visual checks
```

The parent `$portfolio-packaging` Skill continues to own:

```text
portfolio positioning
recruiter-facing story
claim/evidence decisions
change budget
repository metadata
final Portfolio QA
publication approval
```

Do not vendor `beautify-github-readme` into this repository by default.

Do not copy its Skill/reference documentation into this repository merely to make the integration self-contained.

Users who want it should obtain it from its upstream project and install it locally.

---

## 8. Integration quality test

Before treating a specialist as a recommended integration, ask:

```text
Does it solve a real packaging problem?
Does it materially reduce effort or improve quality?
Can it be given a bounded responsibility?
Does it preserve user control?
Can the parent workflow function without it?
Are authorship and license boundaries clear?
Does it avoid unnecessary repository pollution?
```

If several answers are no, do not integrate it merely because the tool is interesting.

Do not grow this directory into a catalog of tools.

Add integration-specific tracked documentation only when a future specialist requires stable parent-side configuration that the generic contract cannot express.

---

## 9. Handoff report

When an integration is used, the parent should be able to report:

```text
Integration used:
Delegated task:
Why specialist use was justified:
Files changed by specialist:
Output retained:
Output rejected or simplified:
License / attribution considerations:
Control returned to parent workflow:
```

Keep this concise unless the user asks for more detail.

---

## Final test

A healthy integration strengthens the parent workflow without becoming its identity.

Ask:

> If this integration disappeared tomorrow, would `$portfolio-packaging` still have a clear purpose, workflow, and useful core capability?

If yes, the boundary is healthy.
