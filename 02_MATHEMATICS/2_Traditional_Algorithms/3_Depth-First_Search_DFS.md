# Chapter 2.2.3: Depth-First Search (DFS)

In the last chapter, we saw that BFS is reliable but memory-heavy.
Now we study the opposite approach: **Depth-First Search (DFS)**.

DFS goes deep first before it comes back.

---

## 1. Core Idea

DFS always expands the **deepest** unexpanded node first.

That means:

- Pick one path,
- Keep moving forward on that path,
- Stop only when:
  - You find the goal, or
  - You hit a dead end,
- Then backtrack and try another path.

DFS is like "go all the way, then return."

---

## 2. How DFS LIFO Stack Works

The key to understanding DFS is the **LIFO (Last-In, First-Out)** property of a stack:

- New nodes are added to the **top**
- Expansion happens from the **top**

This means **the most recently added node gets explored first**, which creates the "deep-first" behavior.

### Visual Representation of a Stack:

```
        ↑
      Add/Remove
     from TOP
        │
    ┌───────┐
    │   5   │  ← TOP (Last In, First Out)
    ├───────┤
    │   4   │
    ├───────┤
    │   3   │
    ├───────┤
    │   2   │
    ├───────┤
    │   1   │  ← BOTTOM (First In)
    └───────┘

Operation: Add to TOP, Remove from TOP
```

**Real-World Analogy:**

Think of a stack like a pile of plates in your kitchen:
- You add new clean plates on top of the pile
- When you need a plate, you take from the top (not the bottom!)
- The last plate you put on is the first one you use (LIFO)
- To reach the bottom plate, you must remove all plates above it first

This is exactly how DFS works: the most recently discovered node gets explored immediately, causing the algorithm to dive deep into one path before backtracking.

---

## 3. Visual Example

Let's say you have this graph:

```
    A
   / \
  B   C
 / \   \
D   E   F
```

**Step-by-step execution:**

1. Create an empty Stack
```
    ┌───────┐
    │       │
    └───────┘
Stack: []
```

2. **Stack: []** → Add the start Node 'A' to the Stack
```
    ┌───────┐
    │   A   │  ← TOP (Added/Pushed 'A' to the top of the Stack)
    └───────┘
Stack: [A]
```

3. **Stack: [A]** → Pop A (top), push its neighbors (B & C) to the top
```
    ┌───────┐
    │   C   │  ← TOP (Popped 'A', then pushed 'B' and 'C'. C is on top)
    ├───────┤
    │   B   │
    └───────┘
Stack: [B, C]
```

4. **Stack: [B, C]** → Pop C (top), push its neighbors (F) to the top
```
    ┌───────┐
    │   F   │  ← TOP (Popped 'C', then pushed 'F')
    ├───────┤
    │   B   │
    └───────┘
Stack: [B, F]
```

5. **Stack: [B, F]** → Pop F (top), no neighbors
```
    ┌───────┐
    │   B   │  ← TOP (Popped 'F', F has no children/neighbors)
    └───────┘
Stack: [B]
```

6. **Stack: [B]** → Pop B (top), push its neighbors (D & E) to the top
```
    ┌───────┐
    │   E   │  ← TOP (Popped 'B', then pushed 'D' and 'E'. E is on top)
    ├───────┤
    │   D   │
    └───────┘
Stack: [D, E]
```

7. **Stack: [D, E]** → Pop E (top), then D...

Notice how we went **A → C → F** before exploring B's children. That's the "depth-first" behavior caused by the stack.

**Exploration order:**
- A → C → F → B → E → D (deep into branches)

Compare this to BFS which would go:
- A → B → C → D → E → F (level by level)

---

## 4. Why It Goes Deep

When you push multiple neighbors onto the stack, the **last one pushed becomes the next one explored**.

This creates a chain that goes deep into one branch before backtracking.

**Example:** When we pop A and push [B, C]:
- C is on top (pushed last)
- C gets explored next
- We dive into C's branch completely before returning to B

---

## 5. Simple Procedure

1. Put the start node on the stack.
2. Repeat until the stack is empty:
   - Pop the top node ← This is key! Always from the top
   - If it is the goal, stop and return the path.
   - Otherwise, push its unvisited neighbors onto the stack ← They go on top

In graph search, keep a `visited` set to avoid cycling forever.

The confusion might be: "If we push neighbors, won't we explore them all at the same level?"

**Answer:** No! Because we immediately pop from the top in the next iteration, we explore the most recently added neighbor first, diving deep before exploring siblings.

---

## 6. Contrast with BFS

**BFS with queue:**
- A → B → C → D → E → F (level by level)
- Uses FIFO: oldest node explored first
- Explores all neighbors before going deeper

**DFS with stack:**
- A → C → F → B → E → D (deep into branches)
- Uses LIFO: newest node explored first
- Explores one branch completely before trying others

---

## 7. Real-World Illustration

Imagine you are in a large cave with many tunnels:

- You choose one tunnel and keep walking inside.
- You do not check all nearby tunnel entrances first.
- If the tunnel ends, you return and try another one.

That is DFS behavior.

---

## 8. Key Properties

- DFS is **not optimal**: it does not guarantee the shortest path.
- DFS can be very fast if the goal happens to be deep in the first branch explored.
- DFS can waste time if it goes deep in the wrong branch.

Without cycle checking (or depth limits), DFS can loop forever in cyclic or infinite spaces.

---

## 9. Completeness and Complexity

Let:

- b = branching factor
- m = maximum depth of the search tree

Typical DFS bounds:

- Time complexity: O(b^m)
- Space complexity: O(bm) (much smaller than BFS in many cases)

Completeness:

- Not complete in infinite-depth spaces.
- In finite graphs with cycle checking, it is complete.

---

## 10. When DFS Is a Good Choice

Use DFS when:

- Memory is limited,
- The space is deep,
- And any valid solution is acceptable (not necessarily shortest).

Avoid DFS when:

- Shortest path is required,
- Or infinite or deep branches can trap the search.

---

## 11. Why DFS Matters in the Lineage

DFS shows an important engineering truth from classical AI:

> Search strategy is a tradeoff.

BFS traded memory for shortest-path guarantees.
DFS trades optimality guarantees for lower memory.

Even before learning, AI already faced design choices under constraints.

---

## 12. Key Insight

**Stack = LIFO = Depth-First**
- Most recent addition gets explored next
- Creates deep exploration before wide exploration
- Uses less memory than BFS

**Queue = FIFO = Breadth-First**
- Oldest addition gets explored next
- Creates level-by-level exploration
- Guarantees shortest path (when costs are equal)

The data structure choice (stack vs queue) is what fundamentally determines the search behavior!

---

## 13. Transition to the Next Algorithm

BFS focuses on shallow depth.
DFS focuses on deep expansion.

But both ignore a major reality:

> Some actions are more expensive than others.

To handle unequal costs, we need **Uniform-Cost Search (UCS)**.
