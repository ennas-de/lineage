# Chapter 2.2.1: Uninformed Search Algorithms (BFS, DFS, UCS)

In Chapter 2.1, we built the mathematical frame:

- state
- action
- transition
- goal

Once that frame is ready, the next question is practical:

> How does an agent actually move through the state space to find a solution?

This is where classical search algorithms enter.

---

## 1. What "Uninformed" Means

Uninformed search (also called blind search) means:

> The algorithm does not know how close any state is to the goal.

It only uses the problem definition:

- initial state
- legal actions
- transition model
- goal test
- (optionally) path cost

No extra guidance is provided.

So the algorithm explores systematically, not magically.

---

## 2. Why This Was a Big Step in Classical AI

Early AI needed a general way to solve many problems:

- puzzle solving
- path finding
- planning
- theorem proving

Uninformed search gave that general mechanism.

Once a problem is modeled as a state-space graph:

- nodes = states
- edges = actions/transitions

the agent can search that graph using a fixed procedure.

That was powerful because one algorithmic idea could be reused across many domains.

---

## 3. The Core Logic Behind All Uninformed Search

All these algorithms follow the same loop:

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
- If moving between some corridors has different effort/cost and you always pick the cheapest route so far, that is UCS-style behavior.

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

- Expands the node with the lowest cumulative path cost `g(n)`.
- Complete and optimal when all step costs are non-negative.
- Generalizes BFS to unequal action costs.

---

## 6. Why This Section Matters in the Lineage

This section marks an important shift:

- From "How do we represent a problem?"
- To "How do we compute a solution inside that representation?"

It is still classical AI:

- explicit states
- explicit rules
- explicit transitions
- no learning

But we are now moving from representation to algorithmic procedure.

That transition is a core part of AI lineage.

---

## 7. What Comes Next

The next sections break these algorithms one by one:

- Chapter 2.2.2: BFS
- Chapter 2.2.3: DFS
- Chapter 2.2.4: UCS
- Chapter 2.2.5: Their shared structure

After that, we can clearly see both their power and their limits, which naturally opens the door to smarter search guidance and later probabilistic thinking.
