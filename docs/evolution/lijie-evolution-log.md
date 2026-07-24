# Lijie Evolution Log

## R2 Workspace Initialization

### Date

2026-07-24 (Asia/Shanghai)

### Scope

This entry records the start of a separate redesign workspace for the `lijie` skill. The purpose is to preserve provenance before any new redesign work begins.

No global `lijie` files were modified in this step. The existing historical backup and the previous candidate revision remain untouched.

### Parent Artifacts

- Live skill source: `C:\Users\LENOVO\.codex\skills\lijie`
- Earlier baseline backup: `C:\Users\LENOVO\Documents\Codex\2026-07-24\co-de\work\lijie-backup-before-revision`
- Earlier candidate revision: `C:\Users\LENOVO\Documents\Codex\2026-07-24\co-de\work\lijie-revision`

### New Workspace

- Working record: `F:\lijie-redesign\lijie-evolution-log.md`
- Immutable source snapshot: `F:\lijie-redesign\source-snapshot`
- C: drive staging copy retained for verification: `C:\Users\LENOVO\Documents\Codex\2026-07-24\co-de\work\lijie-redesign\source-snapshot`

### Snapshot Manifest

The following SHA-256 values were calculated for the source snapshot. The same values were independently calculated for the F: drive copy.

| Relative path | Size | SHA-256 |
|---|---:|---|
| `SKILL.md` | 6342 | `218748BE7A0929CF5AEB26B64B55BCA95128DDF892FF458344EB6D6E37759DE9` |
| `agents/openai.yaml` | 268 | `9E0D36B5DCD34BCCD66A3FE9236E4080FB7CB1C9662293C4F50232092F3AE02A` |
| `references/structure-framework.md` | 5374 | `7CC5EE894AC19E54509F0E3299EFE781B367BD56AFD8DFD5770087B1DF341C19` |

### Why This Redesign Exists

The current skill already provides Feynman-style explanation, first-principles decomposition, knowledge-structure mapping, adaptive depth, and interactive checks. The redesign is motivated by questions and tests that exposed a larger requirement:

1. An AI cannot directly observe a learner's hidden context or reasoning state.
2. Personalization therefore needs observable evidence, calibration, and correction rather than fixed learning-style labels.
3. A long-lived personal learning system needs stable core rules, domain adapters, learner state, learning evidence, regression tests, and an explicit change history.
4. A generic relation taxonomy is not enough to teach different disciplines; code, mathematics, history, and other domains need distinct decomposition and validation adapters.
5. Historical and cognitive evidence suggests that model construction, active retrieval/generation, counterexamples, feedback, and revision should be treated as testable mechanisms rather than as personality myths.

### Proposed R2 Direction

The redesign will be evaluated as a learning protocol, not merely as a larger explanation template:

```text
goal -> calibration -> domain decomposition -> model construction
     -> learner generation -> retrieval/application/counterexample
     -> gap diagnosis -> targeted repair -> transfer -> delayed review
```

The intended layers are:

- stable core protocol;
- domain-specific references;
- explicit learner state;
- learning artifacts and evidence;
- regression tests and versioned evolution.

### Evidence and Design Boundaries

- Research findings, user feedback, direct file observations, and design inferences must remain distinguishable in later entries.
- Historical figures are used as sources of method hypotheses, not as proof of a universal "genius method".
- The redesign must not infer fixed visual/auditory learner types without evidence.
- A rule should not be promoted into the stable core because of one conversational success.

### Verification Receipt

- The first copy attempt used a wildcard with PowerShell `-LiteralPath`; it created the directories but copied no files.
- The copy was repaired using explicit paths for `SKILL.md`, `agents`, and `references`.
- C: and F: snapshots now contain the same three files.
- All three SHA-256 values match across the two snapshots.

### Next Planned Work

1. Write the R2 design specification without changing the live skill.
2. Define a domain-adapter template and learner-state schema.
3. Create a new draft from the immutable source snapshot.
4. Test the draft on at least mathematics, code, and one source-heavy subject.
5. Record failures, rejected alternatives, and validation results here.
6. Only after review decide whether any draft should replace the global skill.

### Rollback Boundary

At the time of this entry, the live skill remains unchanged. The F: drive snapshot is the protected starting point for the redesign, and the earlier C: drive backup remains an independent historical recovery point.

## R2 Design Specification — 2026-07-24

### Action

Created `R2-design-spec.md` in the redesign workspace. This is a design specification only; it is not the new skill implementation.

### Design Direction

The proposed redesign treats `lijie` as an evidence-driven learning protocol with separate layers for:

- stable core workflow;
- domain adapters;
- explicit learner state;
- learning evidence and artifacts;
- regression tests and controlled evolution.

The core state machine is:

```text
goal → calibration → domain decomposition → model construction
     → learner generation → verification → gap repair
     → transfer → delayed review → state update
```

### Files

- Staging design specification: `C:\Users\LENOVO\Documents\Codex\2026-07-24\co-de\work\lijie-redesign\R2-design-spec.md`
- Intended F: drive copy: `F:\lijie-redesign\R2-design-spec.md`
- R2 design specification SHA-256: `A3AC40AEB08FA0411141801919AE222F871D9D4292AFE371715955A87FA28E2B`

### Boundary

This step does not modify `C:\Users\LENOVO\.codex\skills\lijie` or `source-snapshot`.

## R2 Design Specification Language Revision — 2026-07-24

### User Feedback

The first design specification was written primarily in English and was difficult for the user to read. The user requested a Chinese version.

### Decision

Rewrite the design specification in Chinese. Keep only canonical protocol fields and technical identifiers such as `Depth`, `Interaction`, `Verification`, `Objects`, `Primitives`, `Evidence`, and `Transfer` in English where this reduces terminology drift.

### Boundary

This language revision changes only the project design document. The global skill and the protected source snapshot remain unchanged.

## Validation Status — 2026-07-24

### Current Usable Version

Command:

```text
python C:\Users\LENOVO\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\LENOVO\.codex\skills\lijie
```

Result: `Skill is valid!`

### Protected Snapshot

The same validator was run against the C: staging snapshot and also returned `Skill is valid!`. The F: snapshot has matching SHA-256 values for all skill files, so it is structurally equivalent.

### R2 Status

R2 is not yet a usable replacement skill. It currently contains a Chinese design specification and a protected source snapshot; no R2 `SKILL.md` implementation has been written, registered, or installed. The current global skill remains the active usable version.

## R2 Draft Implementation — 2026-07-24

### Action

Created the first R2 implementation in the isolated `draft` directory. The global skill and `source-snapshot` were not modified.

### Draft Files

- `draft/SKILL.md` — Chinese core protocol with `Depth`, `Interaction`, and `Verification` axes; calibration; domain decomposition; model construction; active generation; verification; repair; transfer; delayed review; and controlled evolution.
- `draft/agents/openai.yaml` — UI metadata and a default prompt that explicitly names `$lijie`.
- `draft/references/structure-framework.md` — minimal relation vocabulary, including sequence, dependency, hierarchy, contradiction, and real versus fabricated feedback loops.
- `draft/references/domain-adapter-template.md` — reusable slots for `Objects`, `Primitives`, `Operations`, `Assumptions`, `Invariants`, `Evidence`, `Transfer`, and related domain rules.
- `draft/references/learner-state-schema.md` — observable learner state, evidence, privacy, consent, and learning receipt fields.
- `draft/references/code-learning.md` — code-specific decomposition, execution traces, tests, debugging, contracts, and structural transfer.
- `draft/references/math-learning.md` — definitions, conditions, proof obligations, counterexamples, and condition-changing transfer.

### Validation Receipt

Command:

```text
$env:PYTHONUTF8='1'; python C:\Users\LENOVO\.codex\skills\.system\skill-creator\scripts\quick_validate.py F:\lijie-redesign\draft
```

Result: `Skill is valid!`

The UTF-8 mode is required in this Windows environment because the validator uses Python's locale default when calling `Path.read_text()`; without UTF-8 mode, the Chinese file is misread as GBK and raises `UnicodeDecodeError`. This is an environment/validator limitation, not a content validation failure.

Static reference checks confirmed that every reference named by `SKILL.md` exists. The core file is 227 lines, and the UI metadata's `short_description` is 54 characters.

### Forward Smoke Tests

Six contract-level cases passed:

| Case | Expected behavior | Result |
|---|---|---|
| Simple translation | Exclude from the full learning loop unless learning is explicitly requested | PASS |
| Mathematics | Route to the math adapter and require definitions, boundaries, proof/counterexample, or transfer evidence | PASS |
| Code | Route to the code adapter and use execution, tests, debugging, or implementation evidence | PASS |
| Source-heavy/history material | Distinguish `source-backed`, observed, inferred, uncertain, and uncovered claims | PASS |
| One-shot summary | Allow a complete answer without forcing interaction | PASS |
| Learner state | Avoid fixed learning-style labels and require consent before cross-session persistence | PASS |

These are static contract smoke tests, not a claim that the draft has been installed as an active runtime skill. Runtime behavior still requires an isolated installation/invocation test or explicit replacement review.

### Integrity Receipt

- C: staging and F: draft hashes match for all seven draft files.
- Live skill and C: `source-snapshot` hashes still match for the guarded files (`SKILL.md`, `agents/openai.yaml`, and `references/structure-framework.md`).
- `C:\Users\LENOVO\.codex\skills\lijie` remains unchanged.

### Current Status

The R2 draft is structurally valid and usable as an isolated skill package, but it is not the active global skill. The next decision is whether to run a true isolated runtime invocation test, revise the draft from failures, or approve a separate installation step. No installation was performed in this entry.

## A/B Protocol Test — 2026-07-24

### Task

Compared the old global skill and the R2 draft on one identical mathematics learning task: understand why `f(x)=|x|` is not differentiable at `x=0`, then solve a condition-changing transfer problem. Both groups received the same learner response: “I know derivative is like tangent slope, but I do not understand why left and right must be calculated separately.”

### Result

The old skill produced a strong explanation with a check question and lower interaction overhead. R2 made the learner state, math-specific objects/operations/assumptions, error diagnosis, transfer, and delayed retrieval explicit. A single-task manual rubric scored the old protocol `8/14` and R2 `13/14`; the only clear old-version advantage was lighter interaction overhead.

### Evidence Boundary

This was a controlled, qualitative simulation based on the two `SKILL.md` files, not a runtime A/B after registering R2 in Codex. Both outputs were generated by the same model, so the score is directional rather than an independent benchmark. Full details and representative output excerpts are in:

- `C:\Users\LENOVO\Documents\Codex\2026-07-24\co-de\work\lijie-redesign\AB-test-2026-07-24.md`
- `F:\lijie-redesign\AB-test-2026-07-24.md`

### Design Implication

Keep R2's domain adapters, evidence states, transfer, and delayed retrieval, but preserve the three-axis downgrade path (`Depth`, `Interaction`, `Verification`) so simple questions do not inherit the full coaching overhead.

## A/B Code Test: micrograd Semantics — 2026-07-24

### Scope

The user requested a code task from `micrograd`. The official repository was not available locally, and the environment could not connect to GitHub. To keep the test honest, a minimal local fixture implementing micrograd-style scalar `Value` nodes, graph traversal, reverse propagation, and gradient accumulation was used. This is a semantic test, not an official repository regression test.

### Task and Evidence

The task was to understand why `Value.backward()` needs reverse topological order and `+=` when `x` is reused in `z=x*x+x`, then transfer the rule to `y=x*x; z=y+y`.

Actual execution produced:

```text
CORRECT z=12.0 x.grad=7.0
OVERWRITE_MUTANT z=12.0 x.grad=3.0
TRANSFER z=18.0 x.grad=12.0
MICROGRAD_SEMANTIC_TESTS=3 FAILED=0
```

The overwrite mutant shows a concrete failure: forward value remains correct while one branch's gradient contribution is lost.

### A/B Result

Old `lijie` produced a correct explanation and a check question, but did not make execution, mutation testing, and graph-structure transfer explicit as completion evidence. R2's code adapter diagnosed the learner's missed branch, separated `data` from `grad`, required a runtime mutation check, and used `y+y` as a structural transfer. The directional manual score was `8/12` for old and `11/12` for R2; R2's advantage was evidence strength, while old's advantage was lower interaction overhead.

Full report:

- `C:\Users\LENOVO\Documents\Codex\2026-07-24\co-de\work\lijie-redesign\AB-test-micrograd-2026-07-24.md`
- `F:\lijie-redesign\AB-test-micrograd-2026-07-24.md`

### Boundary

No official `micrograd` source was downloaded or modified. The failed network attempt did not leave a clone directory. The global skill and protected snapshot remain unchanged.
