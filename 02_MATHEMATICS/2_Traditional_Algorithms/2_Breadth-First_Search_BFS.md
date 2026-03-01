# Chapter 2.2.2: Breadth-First Search (BFS)

In Chapter 2.2.1, we introduced uninformed search.
Now let us start with the most intuitive one: **Breadth-First Search (BFS)**.

BFS explores the state space **level by level**.

---

## 1. Core Idea

BFS always expands the **shallowest** unexpanded node first.

That means:

- First, it checks states 1 step away from the start.
- Then, states 2 steps away.
- Then, states 3 steps away.
- And so on.

BFS moves in "circles" outward from the initial state.

---

## 2. How BFS FIFO Queue Works

The key to understanding BFS is the **FIFO (First-In, First-Out)** property of a queue:

- New nodes are added to the **back**
- Expansion happens from the **front**

This means **the earliest added node gets explored first**, which creates the "level-by-level" behavior.

### Visual Representation of a Queue:

```
FRONT                                    BACK
  ↓                                        ↓
┌───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │  ← Elements in queue
└───┴───┴───┴───┴───┘
  ↑                   ↑
 Remove              Add
 here               here

Operation: Remove from FRONT, Add to BACK
```

**Real-World Analogy:**

Think of a queue like standing in line at your favorite coffee shop:
- The first person in line is the first to be served (FIFO)
- New customers join at the back of the line
- No one cuts in front - everyone waits their turn
- The barista always serves from the front

This is exactly how BFS works: nodes that arrive first get explored first, ensuring we check all nearby states before moving to distant ones.

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

1. **Queue: [A]** → Remove A (front), add its neighbors to back
2. **Queue: [B, C]** → Remove B (front), add its neighbors to back
3. **Queue: [C, D, E]** → Remove C (front), add its neighbors to back
4. **Queue: [D, E, F]** → Remove D (front), no neighbors
5. **Queue: [E, F]** → Remove E (front), then F...

Notice how we went **A → B → C → D → E → F** (level by level). That's the "breadth-first" behavior caused by the queue.

**Exploration order by level:**
- Level 0: A
- Level 1: B, C
- Level 2: D, E, F

---

## 4. Why It Goes Level by Level

When you add multiple neighbors to the back of the queue, they all wait their turn behind nodes from earlier levels.

This creates a pattern where:
- All nodes at distance 1 are explored before any node at distance 2
- All nodes at distance 2 are explored before any node at distance 3
- And so on

---

## 5. Simple Procedure

1. Put the start node in the queue.
2. Repeat until the queue is empty:
   - Remove the front node ← This is key! Always from the front
   - If it is the goal, stop and return the path.
   - Otherwise, add its unvisited neighbors to the back of the queue ← They go to the back

In practice, we also keep a `visited` set to avoid repeating states.

The confusion might be: "If we add all neighbors, won't we explore them immediately?"

**Answer:** No! Because we remove from the front in the next iteration, we explore nodes in the order they were discovered, ensuring level-by-level exploration.

---

## 6. Real-World Illustration

Imagine you are looking for a friend in a large school:

- You check all classrooms on the ground floor first.
- Then all classrooms on the first floor.
- Then the second floor.

You do not jump deep into one corner immediately.
You search by distance from where you started.

That is BFS behavior.

---

## 7. Key Guarantee

BFS guarantees a **shortest path in number of steps** when each action has the same cost.

If step cost is uniform (for example, every move costs 1), BFS is optimal.

If action costs are different, BFS may not give the lowest-cost path.
That is why UCS is needed later.

---

## 8. Completeness and Complexity

Let:

- b = branching factor (average number of children per node)
- d = depth of the shallowest goal

Then BFS has:

- Time complexity: O(b^d)
- Space complexity: O(b^d)

BFS is complete for finite b (it will eventually find a solution if one exists), but memory usage can become very large.

---

## 9. When BFS Is a Good Choice

Use BFS when:

- The goal is likely close to the start,
- Edge costs are equal,
- And shortest path in steps is important.

Avoid BFS when:

- The search tree is very deep,
- Or memory is limited.

---

## 10. Why BFS Matters in the Lineage

BFS is one of the first clear examples that intelligence can be treated as:

- Explicit state representation
- Plus explicit search control

No learning is happening.
No probability is used.
It is pure systematic exploration.

And that was a major step in early AI.

---

## 11. Key Insight

**Queue = FIFO = Breadth-First**
- Earliest addition gets explored next
- Creates level-by-level exploration
- Guarantees shortest path (when costs are equal)

**Stack = LIFO = Depth-First**
- Most recent addition gets explored next
- Creates deep exploration before wide exploration

The data structure choice (queue vs stack) is what fundamentally determines the search behavior!

---

## 12. Transition to the Next Algorithm

BFS is reliable, but memory-heavy.

This naturally leads to the next question:

> Can we use less memory by going deep first?

That question leads directly to **Depth-First Search (DFS)**.
