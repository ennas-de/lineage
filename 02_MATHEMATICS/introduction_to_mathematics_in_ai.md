# Chapter 02: Introduction of Mathematics into Artificial Intelligence

This section marks the first **formal mathematical grounding** of classical Artificial Intelligence.

- In Section 1, we defined **intelligence** as the ability to achieve goals across a range of environments.

- At this stage in AI’s history, intelligent behavior was implemented primarily through:
  - **Symbolic representations of the world**
  - **Explicit rules and constraints**
  - **Deterministic inference procedures**

- Symbolic systems worked by:
  - Representing relevant aspects of the world,
  - Encoding rules over those representations, and
  - Applying inference to select actions.

- Manipulating symbols was not intelligence itself, but the **mechanism through which intelligent behavior was realized**.

- We also introduced the minimal structure of intelligence as a **closed perception-action loop**, where:
  - the agent observes the environment,
  - selects an action,
  - affects the environment,
  - and receives new information in return.

---

### Before Learning Became Central

- At this point in history:
  - There was little or no data
  - Learning was not the dominant paradigm
  - There were no _learned_ parameters
  - Intelligence was defined as **explicit reasoning over explicitly defined spaces**

- The central question was no longer _what intelligence is_, but:

> **How do we formally represent states, actions, and goals so that an agent can act rationally?**

- This question forced AI to adopt **mathematical structures** that could:
  - define states precisely,
  - describe transitions rigorously,
  - and evaluate actions objectively.

---

- We now begin Section 2.1: **Mathematical Representation of State**
