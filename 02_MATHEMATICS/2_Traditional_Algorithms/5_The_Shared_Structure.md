# Chapter 2.2.5: The Shared Structure

We have now studied:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform-Cost Search (UCS)

They look different on the surface, but they all run on the same backbone.

This chapter shows that backbone clearly.

---

## 1. One Core Search Template

All uninformed search methods follow this pattern:

1. Put the start node in a frontier.
2. Repeat:
3. If frontier is empty, return failure.
4. Remove one node from frontier (based on a rule).
5. If node is a goal, return success/path.
6. Expand node and generate successors.
7. Add valid successors to frontier (while handling repeats).

So the real difference is simple:

> The algorithms differ mostly in how they manage the frontier.

---

## 2. The Three Shared Building Blocks

### 1. Frontier (open list)

The frontier stores nodes discovered but not yet expanded.

- BFS: frontier is a FIFO queue.
- DFS: frontier is a LIFO stack.
- UCS: frontier is a min-priority queue by `g(n)`.

### 2. Repeated-state handling (visited / best-cost memory)

Without repeat handling, search can loop and waste time.

- BFS/DFS commonly use a `visited` set.
- UCS tracks best known path cost to each state.

### 3. Termination condition

Search stops when:

- a goal is found, or
- there are no more nodes to explore.

---

## 3. Same Problem Frame, Different Expansion Rule

All three still use the same formal problem setup:

- initial state `s0`
- actions `A(s)`
- transition model `T(s, a) -> s'`
- goal test `Goal(s)`
- (for UCS) path cost function

What changes is the **node-selection rule**:

- BFS selects smallest depth.
- DFS selects greatest depth (latest pushed).
- UCS selects smallest cumulative cost `g(n)`.

This is why we call them one family of algorithms.

---

## 4. Real-World Illustration

Think of searching for a lost book in a big library.

- The building and rooms are the same problem space.
- Your search method changes your behavior:
  - BFS: check nearby shelves first, layer by layer.
  - DFS: follow one aisle deeply before changing aisle.
  - UCS: if moving between sections has different time/cost, pick the cheapest next move.

Same world.
Same goal.
Different frontier rule.

---

## 5. What This Reveals About Classical AI

This shared structure teaches a big lineage lesson:

> In early AI, intelligence was often "good control over search," not learning from data.

The system is still:

- explicit
- rule-based
- hand-designed

Performance improvements come from smarter search control, data structures, and cost handling.

---

## 6. Limits Shared by All Three

Even with different frontier rules, these methods still face common limits:

- state spaces can explode combinatorially,
- memory can become a bottleneck,
- runtime can become very high,
- there is no heuristic guidance toward likely goals.

So they are foundational, but not enough for large real-world problems.

---

## 7. Key Takeaway

BFS, DFS, and UCS are not three unrelated ideas.
They are three variants of one search skeleton.

Once you understand the shared skeleton, you can read many later AI algorithms more easily.

---

## 8. Transition in the Lineage

This closes the uninformed-search block.

We now have:

- formal state-space modeling,
- and systematic search procedures over that space.

Next, the pressure for speed and scalability pushes AI toward more informed guidance and, later in the lineage, toward probability and learning-based methods.
