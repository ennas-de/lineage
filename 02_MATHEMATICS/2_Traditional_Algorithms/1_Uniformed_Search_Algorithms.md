# Chapter 2.2.1: Uninformed Search Algorithms (BFS, DFS, UCS)

In Chapter 2.1, we built the mathematical foundation:

- State
- Action
- Transition
- Goal

Once that foundation is in place, a practical question emerges:

> How does an agent actually move through the state space to find a solution?

This is where classical search algorithms enter.

---

## 1. What "Uninformed" Means

Uninformed search (also called blind search) means:

> The algorithm does not know how close any state is to the goal.

It only uses the problem definition:

- Initial state
- Legal actions
- Transition model
- Goal test
- (Optionally) path cost

No extra guidance is provided.

The algorithm explores systematically, not magically.

---

## 2. Why This Was a Big Step in Classical AI

Early AI needed a general way to solve many different problems:

- Puzzle solving
- Pathfinding
- Planning
- Theorem proving

Uninformed search provided that general mechanism.

Once a problem is modeled as a state-space graph:

- Nodes = states
- Edges = actions/transitions

The agent can search that graph using a fixed procedure.

This was powerful because one algorithmic idea could be reused across many domains.

---

## 3. The Core Logic Behind All Uninformed Search

All these algorithms follow the same basic loop:

1. Start from an initial state.
2. Expand states to generate successor states.
3. Check whether the goal is reached.
4. Repeat until success or failure.

In simple terms: they keep asking, "What can I try next from here?"

---

## 4. Real-World Illustration

Imagine you enter a new school building and need to find the principal's office, but you have no map.

- If you check rooms level by level from the entrance, that is BFS-style behavior.
- If you keep following one hallway as far as possible before coming back, that is DFS-style behavior.
- If moving between some corridors has different effort or cost and you always pick the cheapest route so far, that is UCS-style behavior.

Same building. Different search strategy.

---

## 5. The Three Main Uninformed Algorithms in This Chapter

### Breadth-First Search (BFS)

- Expands the shallowest states first (level by level).
- Complete for finite branching.
- Optimal when each step has equal cost.

### Depth-First Search (DFS)

- Expands the deepest available state first.
- Uses less memory than BFS.
- Not guaranteed to find the shortest path.

### Uniform-Cost Search (UCS)

- Expands the node with the lowest cumulative path cost g(n).
- Complete and optimal when all step costs are non-negative.
- Generalizes BFS to handle unequal action costs.

---

## 6. Why This Section Matters in the Lineage

This section marks an important shift:

- From "How do we represent a problem?"
- To "How do we compute a solution inside that representation?"

It is still classical AI:

- Explicit states
- Explicit rules
- Explicit transitions
- No learning

But we are now moving from representation to algorithmic procedure.

That transition is a core part of AI's lineage.

---

## 7. What Comes Next

The next sections examine these algorithms one by one:

- Chapter 2.2.2: BFS
- Chapter 2.2.3: DFS
- Chapter 2.2.4: UCS
- Chapter 2.2.5: Their shared structure

After that, we can clearly see both their power and their limits, which naturally opens the door to smarter search guidance and, later, probabilistic thinking.
