# Chapter 2.2.3: Depth-First Search (DFS)

In the last chapter, we saw that BFS is reliable but memory-heavy.
Now we study the opposite style: **Depth-First Search (DFS)**.

DFS goes deep first before it comes back.

---

## 1. Core Idea

DFS always expands the **deepest** unexpanded node first.

That means:

- pick one path,
- keep moving forward on that path,
- stop only when:
  - you find the goal, or
  - you hit a dead end,
- then backtrack and try another path.

So DFS is like "go all the way, then return."

---

## 2. Data Structure Behind DFS

DFS uses a **LIFO stack** (Last-In, First-Out), either explicitly or through recursion:

- newest node added is expanded first.

Because of this, DFS naturally dives deep into one branch.

---

## 3. Simple Procedure

1. Put the start node on the stack.
2. Repeat until the stack is empty:
3. Pop the top node.
4. If it is the goal, stop and return the path.
5. Otherwise, push its unvisited neighbors onto the stack.

In graph search, keep a `visited` set to avoid cycling forever.

---

## 4. Real-World Illustration

Imagine you are in a large cave with many tunnels:

- You choose one tunnel and keep walking inside.
- You do not check all nearby tunnel entrances first.
- If the tunnel ends, you return and try another one.

That is DFS behavior.

---

## 5. Key Properties

- DFS is **not optimal**: it does not guarantee the shortest path.
- DFS can be very fast if the goal happens to be deep in the first branch explored.
- DFS can waste time if it goes deep in the wrong branch.

Without cycle checking (or depth limits), DFS can loop forever in cyclic or infinite spaces.

---

## 6. Completeness and Complexity

Let:

- `b` = branching factor
- `m` = maximum depth of the search tree

Typical DFS bounds:

- Time complexity: `O(b^m)`
- Space complexity: `O(bm)` (much smaller than BFS in many cases)

Completeness:

- Not complete in infinite-depth spaces.
- In finite graphs with cycle checking, it is complete.

---

## 7. When DFS Is a Good Choice

Use DFS when:

- memory is limited,
- the space is deep,
- and any valid solution is acceptable (not necessarily shortest).

Avoid DFS when:

- shortest path is required,
- or infinite/deep branches can trap the search.

---

## 8. Why DFS Matters in the Lineage

DFS shows an important engineering truth from classical AI:

> Search strategy is a tradeoff.

BFS traded memory for shortest-path guarantees.
DFS trades optimality guarantees for lower memory.

So even before learning, AI already faced design choices under constraints.

---

## 9. Transition to the Next Algorithm

BFS focuses on shallow depth.
DFS focuses on deep expansion.

But both ignore a major reality:

> Some actions are more expensive than others.

To handle unequal costs, we need **Uniform-Cost Search (UCS)**.
