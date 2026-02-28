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

So BFS moves in "circles" outward from the initial state.

---

## 2. Data Structure Behind BFS

BFS uses a **FIFO queue** (First-In, First-Out):

- New nodes are added to the back.
- Expansion happens from the front.

Because of this queue behavior, earlier levels are always explored before deeper levels.

---

## 3. Simple Procedure

1. Put the start node in the queue.
2. Repeat until the queue is empty:
3. Remove the front node.
4. If it is the goal, stop and return the path.
5. Otherwise, add its unvisited neighbors to the back of the queue.

In practice, we also keep a `visited` set to avoid repeating states.

---

## 4. Real-World Illustration

Imagine you are looking for a friend in a large school:

- You check all classrooms on the ground floor first.
- Then all classrooms on the first floor.
- Then the second floor.

You do not jump deep into one corner immediately.
You search by distance from where you started.

That is BFS behavior.

---

## 5. Key Guarantee

BFS guarantees a **shortest path in number of steps** when each action has the same cost.

If step cost is uniform (for example, every move costs 1), BFS is optimal.

If action costs are different, BFS may not give the lowest-cost path.
That is why UCS is needed later.

---

## 6. Completeness and Complexity

Let:

- `b` = branching factor (average number of children per node)
- `d` = depth of the shallowest goal

Then BFS has:

- Time complexity: `O(b^d)`
- Space complexity: `O(b^d)`

So BFS is complete for finite `b` (it will eventually find a solution if one exists),
but memory usage can become very large.

---

## 7. When BFS Is a Good Choice

Use BFS when:

- the goal is likely close to the start,
- edge costs are equal,
- and shortest path in steps is important.

Avoid BFS when:

- the search tree is very deep,
- or memory is limited.

---

## 8. Why BFS Matters in the Lineage

BFS is one of the first clear examples that intelligence can be treated as:

- explicit state representation
- plus explicit search control

No learning is happening.
No probability is used.
It is pure systematic exploration.

And that was a major step in early AI.

---

## 9. Transition to the Next Algorithm

BFS is reliable, but memory-heavy.

This naturally leads to the next question:

> Can we use less memory by going deep first?

That question leads directly to **Depth-First Search (DFS)**.
