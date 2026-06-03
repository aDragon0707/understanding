---
name: lijie
description: Learn, explain, summarize, and internalize new knowledge with Feynman-style teaching, first-principles decomposition, and explicit knowledge-structure mapping. Use when Codex is asked to understand a concept, article, book, paper, course, domain, mental model, workflow, or unfamiliar material; to produce study notes, summaries, learning paths, teach-back explanations, analogies, quizzes, flashcards, or concept maps; or to expose relationships such as sequential 1-2-3 chains, parallel 1/2/3 sets, one-to-many, many-to-one, networks, hierarchies, dependencies, open loops, closed loops, feedback systems, and required supporting frameworks.
---

# Lijie

## Operating Principle

Turn material into learnable structure, not just a shorter version of itself.

Use three lenses together:

1. Feynman learning: explain simply, find the fuzzy parts, rebuild, and test recall.
2. First principles: separate facts, assumptions, primitives, mechanisms, constraints, and derived conclusions.
3. Structure mapping: make every important point's relation to other points explicit.

If the user gives no target level, default to an intelligent beginner who wants practical mastery. If the user gives source material, stay faithful to it and mark inferences. If the task involves recent, legal, medical, financial, or high-stakes facts, follow normal verification rules before teaching from them.

## Workflow

1. Define the learning object.
   - Name the central question the material answers.
   - State what counts as "understanding" for this request: intuition, use, critique, memorization, or transfer.
   - Identify likely prerequisites and unknown terms.

2. Decompose from first principles.
   - Separate primitives, definitions, assumptions, mechanisms, constraints, examples, edge cases, and consequences.
   - Ask: "If I had to rebuild this idea from nothing, what irreducible pieces must exist?"
   - Mark claims as source-backed, inferred, uncertain, or context-dependent.

3. Explain with the Feynman cycle.
   - Give a plain-language version first.
   - Then give the precise version.
   - Surface gaps, hidden leaps, jargon, and non-obvious dependencies.
   - Use analogies only when they preserve the core mechanism; state where each analogy breaks.

4. Map the knowledge structure.
   - Load `references/structure-framework.md` when the user asks for structural mapping, system frameworks, loops, "1-2-3", "one-to-many", "many-to-one", or when the material has more than a few concepts.
   - Label each important relationship with a structure type: sequence, parallel set, hierarchy, one-to-many, many-to-one, many-to-many, dependency, contradiction, feedback loop, or open loop.
   - Identify whether each loop is closed, open, missing inputs, missing outputs, or missing feedback.

5. Build the learning artifact.
   - Prefer a compact but complete output: overview, primitives, structure map, detailed explanation, examples, failure modes, and practice.
   - For long material, summarize in layers: 10-second gist, 2-minute map, deep structure, then study plan.
   - Include retrieval questions or teach-back prompts when the user wants to learn, not merely summarize.

## Output Contract

When useful, use this shape:

```markdown
## Core Question
What problem or question this knowledge answers.

## Feynman Explanation
Simple explanation, then precise explanation.

## First-Principles Decomposition
- Primitives:
- Assumptions:
- Mechanisms:
- Constraints:
- Consequences:

## Knowledge Structure
- 1-2-3 sequence:
- 1/2/3 parallel set:
- One-to-many:
- Many-to-one:
- Network/dependency:
- Closed loops:
- Open loops:

## Mastery Checks
- Explain:
- Apply:
- Compare:
- Diagnose:
```

Adapt the headings to the user request. Do not force every section when the answer should be short.

## Quality Bar

- Do not hide behind generic summary language.
- Convert abstractions into mechanisms.
- State dependencies and directionality.
- Distinguish "parts of a thing" from "steps in a process" and "reasons for a conclusion".
- Prefer small diagrams, tables, and bullet maps over long prose when relationships matter.
- End with practice only when it helps the user's stated goal.
