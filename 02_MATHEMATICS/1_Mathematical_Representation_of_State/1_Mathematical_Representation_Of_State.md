# Chapter 2.1.1: Mathematical Representation of State

To build **rational, goal-directed agents**, AI needed a formal way to describe the world. This required **mathematical representation of states**.

### 1. What Is a State?

A **state** is a complete description of the environment at a specific moment in time.
Mathematically:

> s ∈ S

Where:

- s = a single state
- S = the set of all possible states (the **state space**)

**Examples:**

- Chess board configuration -> s = positions of all pieces
- 8-puzzle -> s = tiles arrangement
- Robot navigation -> s = (position,orientation,sensor readings)

**Key properties:**

1. **Completeness:** A state must capture all information relevant to decision-making.
2. **Distinctiveness:** Each unique configuration is a distinct state.
3. **Determinism (initially):** State transitions are predictable under known actions.

---

### 2. Representing States Mathematically

States can be represented in several ways:

1. **Vectors / Tuples:**

> s = (x1​, x2​, …, xn​)

- Each component (x_i) represents a variable of the environment
- Common in robotics, planning, and combinatorial problems

2. **Graphs / Networks:**

- Nodes represent states
- Edges represent **actions** or **transitions**
- Example: 8-puzzle or chess state-space graph

3. **Symbolic Representations:**

- Use meaningful **tokens** to represent facts:
  {KING_IN_CHECK,OBSTACLE_PRESENT,GOAL_REACHED}
- Simplifies reasoning for rule-based systems

---

### 3. State Space Size and Complexity

If indeed States can be represented in several ways, then how do we know which state to pick (or use), and when?

- **Finite, small state space:** Can enumerate all states (e.g., 8-puzzle: 9! = 362,880 states)
- **Large or infinite state space:** Requires **search algorithms and heuristics**
- **Combinatorial explosion** motivates abstraction and compact representation
- State Spaces will be discussed more in the next chapter.

---

This takes us to Chapter 2.2: State Spaces, Actions, and Transitions.
