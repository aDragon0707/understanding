# Formula Origin Protocol

Use this reference when a learner asks why a formula, transformation, notation, or standard derivation has its structure. Typical signals:

- "Where does this formula come from?"
- "Why do we transform it this way?"
- "Why is this term added?"
- "You are explaining symbols, not the source."
- "I know the formula; I do not know why it is shaped like that."

## Core Rule

Do not start from the standard formula. Start from the smallest causal, geometric, physical, or logical relationship that makes the formula necessary.

The goal is not to restate notation more clearly. The goal is to explain why each part must exist.

## Response Order

1. Name the problem the formula solves.
2. State the primitive relationship without specialized notation.
3. Translate each part of that primitive relationship into the course notation.
4. Explain why each symbol or term is necessary.
5. Only then present the compact formula.
6. Separate derivation from calculation.
7. If the learner asks again, stop rephrasing and diagnose which link in the causal chain is missing.

## Diagnostic Questions

Ask these internally before answering:

- Is the learner asking what a symbol means, or why the formula has this shape?
- What is the smallest relationship that would still be true if all notation disappeared?
- Which term would make the formula wrong if removed?
- Does this formula combine different roles, such as orientation plus position, cause plus correction, input plus feedback, or local plus global description?
- Am I explaining the source, or merely giving a cleaner textbook explanation?

## Good Pattern

For a coordinate transform, do not begin with:

```text
^A P = ^A_B R ^B P + ^A P_BORG
```

Begin with the vector relationship:

```text
vector(O_A -> P) = vector(O_A -> O_B) + vector(O_B -> P)
```

Then translate:

- `vector(O_A -> P)` becomes `^A P`, the point described in frame A.
- `vector(O_A -> O_B)` becomes `^A P_BORG`, the origin of frame B described in frame A.
- `vector(O_B -> P)` is known as `^B P`, but it is written in frame B.
- Because `vector(O_B -> P)` must be added in frame A, convert it with `^A_B R`.

Only after that, write:

```text
^A P = ^A_B R ^B P + ^A P_BORG
```

This makes the translation visible:

```text
global position of P
= global position of B's origin
+ local displacement from B's origin to P, rewritten in the global frame
```

## Anti-Pattern

Bad response:

1. Present the standard formula.
2. Define each symbol.
3. Re-explain the same symbols with more detail.
4. Add a numerical example.

Why it fails:

- It assumes the learner already accepts the formula structure.
- It answers "what does this symbol mean?" instead of "why must this term be here?"
- It can feel like a fluent dodge: locally correct, globally unhelpful.

## Repair Move

When the learner pushes back, say explicitly:

```text
You are asking for the source of the formula, not the meaning of the notation.
Let's remove the notation and rebuild the relationship first.
```

Then rebuild from the primitive relationship.

## Compact Checklist

Before finalizing, verify:

- The answer includes a notation-free primitive relationship.
- Every formula term is tied to a role in that relationship.
- The explanation states what would break if the term were omitted.
- The compact formula appears after the source relationship, not before it.
- Calculation is clearly separated from derivation.
