# Chapter 2.1.2: State Spaces, Actions, and Transitions

In Chapter 1, we saw that **classical AI implemented intelligence through explicit symbolic and rule-based manipulation**.

This immediately raises a key question:

> _What happens when the number of possible states becomes extremely large?_

If an agent must select actions across thousands, millions, or even billions of possible states (or symbols), **explicit enumeration becomes infeasible**.

- This is not about recognizing symbols.
- This is about **finding the right sequence of actions efficiently**.

This challenge naturally leads to a **central concept of classical AI**:

> **Search.**

---

## Why Mathematical State Representations Matter

1. **Rational Decision-Making:** Allows agents to compute the consequences of actions.
2. **Search and Planning:** Enables algorithms to systematically explore the state space.
3. **Evaluation and Optimization:** Provides a basis for **performance measures** and **goal achievement**.
4. **Generality:** Abstracts the environment so that the same framework works across different domains.

---

## Transition to Actions and Dynamics

Almost every classical AI problem was framed as:

> **Search over a state space.**

Once states are represented mathematically, we can define:

- **State (s):** A complete symbolic description of the world at a specific time.
- **Action (a):** A legal operation the agent can perform in a state.
- **Transition Function (T):** Defines how actions transform the world.

Mathematically:

> T : S × A → S
> <br> T(s,a)=s'
> <br> where s,s'∈S and a∈A

This forms a **state-space graph**:

- **Nodes:** States
- **Edges:** Actions
- **Paths:** Plans or solutions

This is also the foundation for **search, planning, and optimization**-the next critical layer of classical AI.

**Canonical Example: 8-Puzzle**

- **State:** Arrangement of tiles

- **Actions:** Move the blank tile (up/down/left/right)

- **Transition:** Deterministic tile movement

- **Goal:** Reach the target configuration

- Everything is **explicit, deterministic, and symbolic**.

- **Nothing is learned.**

---

## Why This Abstraction Was Powerful

Many different problems collapse into this form:

- Chess
- Mazes
- Scheduling
- Planning
- Logic inference
- Game playing

Once a problem is expressed as a **state space**, intelligence becomes a matter of **search**.

The central question shifts from _what to represent_ to:

> **How do we search this space efficiently to reach a goal?**

---

## The Limits of Naive Search

Directly searching a state space is often **computationally impossible** due to:

- Exponential growth
- Combinatorial explosion
- Limited time and memory

This limitation motivated **search algorithms** designed to explore state spaces **systematically and efficiently**.

Examples include:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Uniform-Cost Search**
- **Heuristic Search**
- **A\* (A star) Search**

These algorithms **differ not in what they represent, but in**:

- Which states they explore
- In what order
- What guidance or heuristics they use

This marks a **transition from representation to algorithmic intelligence** in classical AI.

---

## Key Insights

1. Once a **state space is defined**, intelligence reduces to **efficient search under constraints**.
2. The limitations of brute-force search naturally led to **heuristics, approximation, probability, and learning**.
3. At this stage of classical AI:

> **Search is king.**
