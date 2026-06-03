# Knowledge Structure Framework

Use this reference when a task needs explicit knowledge topology: how points connect, generate, constrain, or complete one another.

## Relation Types

### 1-2-3 Sequence

Use for ordered dependency, process, causality, derivation, or learning progression.

Pattern:

```text
1 prerequisite/input -> 2 mechanism/operation -> 3 output/result -> 4 next state
```

Check:
- Can step 3 happen before step 2? If yes, it may not be a true sequence.
- Does each step transform the previous state?
- Is the transition rule explicit?

### 1/2/3 Parallel Set

Use for peer concepts under one category. Order does not matter.

Pattern:

```text
Parent category
|-- 1 peer dimension
|-- 2 peer dimension
`-- 3 peer dimension
```

Check:
- Do all items answer the same parent question?
- Are they mutually exclusive, overlapping, or complementary?
- Is there a missing fourth peer?

### One-to-Many

Use when one principle, cause, component, or decision branches into many effects, cases, subparts, examples, or tactics.

Pattern:

```text
1 source/principle
|-- A consequence/subpart
|-- B consequence/subpart
`-- C consequence/subpart
```

Check:
- What rule generates the branches?
- Are branches examples, components, effects, or options?
- Do branches feed back to the source?

### Many-to-One

Use when multiple facts, causes, constraints, observations, or mechanisms converge into one conclusion, capability, or outcome.

Pattern:

```text
A evidence/cause
B evidence/cause
C evidence/cause
        -> 1 conclusion/outcome
```

Check:
- Are all inputs necessary, sufficient, or merely supportive?
- Which input is the bottleneck?
- Does the conclusion disappear if one input is removed?

### Many-to-Many Network

Use when concepts affect each other through cross-dependencies instead of a clean tree.

Pattern:

```text
A <-> B
A -> C
B -> D
C <-> D
```

Check:
- Which nodes are hubs?
- Which edges are causal, logical, temporal, or analogical?
- Where can the network be simplified into smaller loops?

### Hierarchy

Use when concepts are nested by level of abstraction.

Pattern:

```text
Level 0: domain
Level 1: major systems
Level 2: modules
Level 3: mechanisms
Level 4: examples/actions
```

Check:
- Do lower levels instantiate or implement higher levels?
- Are any examples incorrectly placed as principles?
- Are any principles buried as examples?

### Dependency

Use when one concept cannot be understood, executed, or validated without another.

Pattern:

```text
Prerequisite -> dependent concept
Input -> operation
Constraint -> possible action
Evidence -> belief update
```

Check:
- Is the dependency conceptual, practical, empirical, social, or technical?
- Is it hard-required or just helpful?

### Contradiction or Tension

Use when two claims pull against each other.

Pattern:

```text
Claim A improves X but harms Y.
Claim B protects Y but limits X.
Tradeoff: choose based on context Z.
```

Check:
- Is it a real contradiction, a tradeoff, or a difference in level?
- What condition resolves it?

## Loop Types

### Closed Loop

A closed loop has input, action, output, feedback, comparison, and adjustment.

Pattern:

```text
Goal/standard
  -> Input/signal
  -> Action/mechanism
  -> Output/result
  -> Feedback/measurement
  -> Adjustment
  -> back to action or goal
```

Use closed-loop analysis to show how a system learns, self-corrects, compounds, stabilizes, or spirals.

Check:
- What is measured?
- Who or what compares measurement to the goal?
- What changes after feedback?
- What is the loop speed?
- Is the loop reinforcing or balancing?

### Open Loop

An open loop lacks feedback, measurement, comparison, or adjustment.

Pattern:

```text
Input -> action -> output
```

Open-loop risks:
- The system repeats errors.
- The learner feels familiar with material without testing recall.
- A strategy runs without knowing whether it works.
- A concept remains descriptive but not operational.

Convert open to closed:

```text
Add measurement -> compare with goal -> adjust method -> retest
```

## Framework Builder

For each important point, fill this mini-schema:

```text
Point:
Role: primitive | assumption | mechanism | constraint | example | consequence | test
Parent:
Children:
Inputs:
Outputs:
Depends on:
Enables:
Conflicts with:
Loop status: closed | open | no loop | unknown
Missing piece:
Mastery test:
```

## Common Transformations

- Summary -> structure: turn "main ideas" into typed relations.
- Jargon -> primitive: define what must be true before the term makes sense.
- Example -> mechanism: extract what the example proves or demonstrates.
- List -> hierarchy: group peers under parents and remove duplicates.
- Process -> closed loop: add feedback and adjustment.
- Opinion -> claim stack: identify evidence, assumption, inference, and implication.
- Theory -> use: map principles to decisions, actions, and failure modes.

