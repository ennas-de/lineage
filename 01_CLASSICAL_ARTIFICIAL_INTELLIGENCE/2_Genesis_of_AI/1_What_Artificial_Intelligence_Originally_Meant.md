# Section 1.2.1: What Artificial Intelligence Originally Meant

## 1. Historical Foundations

The question of intelligence predates computers by centuries. Philosophers and Scientists long debated whether reasoning could be formalized - whether thought itself might be reduced to rule-governed operations.

In 1651, Thomas Hobbes proposed that reasoning is simply _“calculation”_. This bold claim suggested that thinking might not be mysterious or ineffable, but computational in nature.

Centuries later, Alan Turing gave this idea operational form. He argued that if a machine could convincingly simulate intelligent behavior, we would have reason to call it intelligent. Intelligence, in this framing, becomes observable performance rather than hidden mental substance.

This leads to a foundational question:

> If reasoning is calculation, does sufficiently advanced calculation constitute intelligence?

The term _Artificial Intelligence_ was formally introduced in 1956 by John McCarthy at the Dartmouth Conference. From the beginning, AI was interdisciplinary—drawing from computer science, mathematics, psychology, linguistics, neuroscience, philosophy, and engineering.

---

## 2. From Thinking to Acting

Early AI developed along two conceptual paths:

- A **cognitive path**, focused on symbolic reasoning and internal representations.
- A **behavioral path**, focused on goal-directed action.

Over time, the second perspective gained dominance through the **rational agent framework**. The central question shifted from:

> “How can we build machines that think?”

to:

> “How can we build systems that act effectively in pursuit of goals?”

This shift was decisive.

Intelligence was no longer defined primarily in terms of human-like thought. Instead, it became defined in terms of **effective behavior under constraints**.

The goal of AI changed accordingly. Rather than modeling human cognition, researchers focused on engineering systems that could:

- Perform tasks reliably
- Adapt to varying conditions
- Optimize measurable outcomes
- Achieve explicit objectives

Under this view, intelligence became a property of behavior - not of inner experience.

---

## 3. Intelligence as a Control Problem

Within this framework, intelligence can be defined succinctly as:

> The ability to achieve goals across a range of environments.

Abstractly, an intelligent system is:

> A system that selects actions to achieve goals under constraints.

Notice what this definition does _not_ require:

- Consciousness
- Emotion
- Creativity
- Human likeness

Instead, it centers on:

- Goals
- Actions
- Outcomes

Intelligence becomes a control problem—an engineering challenge of mapping situations to effective responses.

---

## 4. The Minimal Structure of Goal-Directed Behavior

To formalize intelligence in this way, only a small set of components is required:

1. **Environment** - The external context in which the system operates.
2. **Agent** - The entity that perceives and acts.
3. **State** - A description of the current configuration of the environment.
4. **Perception** - The mechanism by which the agent acquires information.
5. **Action** - The set of interventions available to the agent.
6. **Goal** - A success criterion distinguishing desirable from undesirable outcomes.

That is sufficient.

In early AI systems:

- There were no learned models.
- No statistical training pipelines.
- No data-driven optimization loops.

Policies were explicitly designed by engineers.

---

## 5. A Minimal Example: The Light-Switch Agent

Consider a simple case:

- **Environment**: A room
- **State**: Light is ON or OFF
- **Agent**: A program controlling the switch
- **Perception**: Detects time of day and light status
- **Action**: Switch ON or OFF
- **Goal**: Light ON at night, OFF during the day

The agent observes the environment and selects the action that satisfies the goal.

Under the early definition of AI, this qualifies as intelligence.

No consciousness.
No understanding.
Only structured goal achievement.

---

## 6. Why This Definition Was Revolutionary

This behavioral definition allowed a wide range of systems to be classified as intelligent:

- Chess programs
- Route-planning algorithms
- Automated theorem provers

Even if such systems:

- Do not “understand” in a human sense
- Operate entirely through formal rules
- Lack subjective experience

They qualify as intelligent because they:

- Pursue explicit goals
- Process relevant information
- Select actions to optimize performance

Intelligence became measurable in terms of **performance relative to objectives**.

This was a profound conceptual shift.

---

## 7. Intelligence Is Not Infallibility

An important clarification followed:

> Intelligence does not imply correctness.

An intelligent system can fail.

Intelligence concerns the _quality of decisions given available information and constraints_, not perfection or certainty. This remains a foundational principle in modern AI theory.

---

## 8. The Agent Function

Formally, early AI systems were modeled as implementing a function:

Action = f(Perception, Goal)

More abstractly, a policy:

π : Percepts -> Actions

Where:

- π maps observations to actions.
- The mapping is explicitly engineered.
- It is not learned from data.

This formulation became the conceptual foundation for later developments in reinforcement learning, probabilistic reasoning, and modern agent architectures.

---

## 9. Why This Framing Still Matters

Even today, the same structural pattern persists:

> Perceive -> Decide -> Act -> Pursue Goals

Whether the system is:

- A classical planner
- A reinforcement learning agent
- A tool-using large language model

The architecture remains recognizably the same.

What has changed is not the structure, but the method of constructing the policy:

- Statistical modeling
- Optimization
- Machine learning
- Neural networks
- Large-scale data training

The form endures. The implementation evolves.

---

## 10. Implicit Assumptions

Defining intelligence as goal-directed behavior carries implicit commitments:

- The world can be represented in terms of goals.
- Goals are specifiable and measurable.
- Behavior is the proper metric of intelligence.
- Internal experience is not necessary for intelligent action.

Over time, these assumptions proved incomplete. This realization motivated the development of:

- Probabilistic inference
- Learning systems
- Neural architectures
- Representation learning
- Large language models

Yet the original framing provided essential clarity. It made intelligence an engineering problem rather than a metaphysical one.

---

## 11. Conclusion

Artificial Intelligence did not begin with neural networks or large-scale learning.

It began as:

> **Engineered goal-directed behavior.**

Everything that followed—learning, probability, deep architectures—arose from the limitations of handcrafted systems.

The original insight remains foundational:

Intelligence is the capacity to select actions that achieve goals under constraints.
