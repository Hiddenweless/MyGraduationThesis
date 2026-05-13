# PlanGraph DSE Content Optimization v1

This note is based on three sources:

- the current journal manuscript in `sn-article-template/sn-article.tex`;
- the thesis method chapter in `SEU-master-thesis-template-master/chapters/chapter3.tex`;
- the thesis system and experiment chapters in `SEU-master-thesis-template-master/chapters/chapter4.tex` and `chapter5.tex`.

## Current judgment

The current journal draft is already closer to a journal paper than the thesis, but it still carries two thesis traces:

1. it occasionally sounds like a multi-agent system implementation paper rather than a method paper on reliable graph reasoning;
2. the empirical section is broad, but some of the strongest evidence from the thesis is still not surfaced in the main narrative.

Your judgment about `Fig. 2` is correct. That figure is method-to-system bridge material from the thesis. In a DSE submission focused on the method contribution, it is weaker than the framework overview, benchmark table, retrieval evidence, and ablation evidence.

## What should stay

- The overall problem framing from Chapter 3:
  graph reasoning is hard because task understanding, algorithm choice, API use, constraint satisfaction, and output formatting are entangled.
- The core method chain:
  task parsing -> pseudocode planning -> plan-guided retrieval -> executable solving -> execution-grounded repair.
- The key technical claim:
  pseudocode plans are better retrieval anchors than raw question text.
- The key empirical claims from Chapter 5:
  better overall EM, larger gains on high-constraint tasks, planning is the largest contributor, and verification materially improves reliability.

## What should not enter the main journal paper

- Blackboard scheduling.
- Shared artifact versioning and event logs.
- Scheduler states and rollback-control details.
- Cache, replay, reproducibility plumbing.
- Any description whose main question is how the system is orchestrated at runtime rather than why the method improves graph reasoning.

These belong to the thesis Chapter 4 logic, not to the journal main text unless the target paper is positioned as a workflow platform or agent runtime system.

## Proposed next manuscript version

I suggest the next version use this section logic:

1. Introduction
2. Related Work
3. Problem Formulation
4. Method: PlanGraph
5. Experimental Setup
6. Results
7. Discussion
8. Conclusion

Within Section 4, the method should be narrowed to four subsections:

- Task parsing and structured task representation
- Pseudocode planning as an intermediate representation
- Plan-guided retrieval
- Execution verification and repair

The current algorithm block should stay. It is compact and gives enough procedural clarity without pulling in Chapter 4 system architecture.

## Recommended content upgrades

### 1. Weaken the agent rhetoric

The current draft still uses names such as `QuestionAgent`, `PlanningAgent`, `SearchAgent`, `CodingAgent`, and `ReasoningAgent`. For the next version, I would convert most of these into neutral module names:

- parser
- planner
- retriever
- code generator
- verifier / repair module

Reason:
this will move the paper away from "agent orchestration" and toward "reliable LLM-based graph reasoning methodology", which is a cleaner journal positioning.

### 2. Add one stronger reliability table from Chapter 5

The thesis has a useful stability observation with:

- EM fluctuation range
- first-pass success rate
- repair convergence rate

This is better journal evidence than a feedback-path figure. It directly supports the reliability claim. I recommend adding one compact table in the main text or appendix.

### 3. Upgrade the retrieval section from descriptive to evidential

The current draft already has a retrieval-quality table. In the next version, the surrounding text should make one stronger point:

- plan-guided retrieval is not a generic RAG add-on;
- it is the mechanism that aligns algorithmic intent with executable graph knowledge.

This claim is already supported by Chapter 3 and Chapter 5. It should be stated more sharply.

### 4. Move some qualitative case material out of the main body

The current TSP case study is useful, but the figure can be optional. For the next version:

- keep the short case description in the main text if needed;
- move the visual case figure to the appendix if space becomes tight.

If we need one more main-text slot, the stability table is more valuable than the case figure.

### 5. Strengthen the limitation section with thesis evidence

Chapter 5 already gives a good failure taxonomy:

- coarse plans on dynamic tasks
- imperfect retrieval ranking
- limited validation coverage
- high search cost on hard combinatorial tasks
- formatting failures

This should be condensed into a sharper Discussion section. That will make the paper read more like a mature journal submission and less like a benchmark report.

### 6. Add a task-family adaptation paragraph, but keep it short

Chapter 3 has useful material on task families:

- path tasks
- connectivity/reachability
- matching/flow
- combinatorial optimization
- dynamic graph tasks

I would keep only one compact paragraph in the method or discussion section to explain why the same planning-feedback pattern transfers across graph task families. Do not import the full thesis template-library discussion into the main paper.

## Figure plan for the next round

Recommended main-text figures:

- Fig. 1: framework overview
- category/complexity figure
- ablation figure

Optional:

- case-study figure -> appendix first candidate

Removed:

- the old `Fig. 2` feedback-path figure

## Concrete next-step edit package

If we continue immediately, I recommend the next batch of edits be:

1. rename most "Agent" wording to neutral module wording;
2. add one stability/reliability table from Chapter 5;
3. tighten the discussion and limitation paragraphs using the thesis error taxonomy;
4. decide whether the case-study figure stays in main text or moves to appendix.

## My recommendation

The strongest next version is not to add more mechanism diagrams. It is to make the paper more method-centric and more evidence-centric:

- fewer orchestration details;
- stronger reliability evidence;
- clearer boundary between method contribution and thesis-only implementation details.
