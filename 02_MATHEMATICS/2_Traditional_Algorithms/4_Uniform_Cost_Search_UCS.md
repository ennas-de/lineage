# Chapter 2.2.4: Uniform-Cost Search (UCS)

In DFS, we saw that going deep first can save memory.
But DFS and BFS both miss one key thing:

> Not all actions have the same cost.

Uniform-Cost Search (UCS) solves that problem.

---

## 1. Core Idea

UCS always expands the node with the **lowest path cost so far**.

This path cost is written as:

`g(n)` = cumulative cost from the start node to node `n`.

So UCS is cost-aware from the beginning.

---

## 2. Data Structure Behind UCS

UCS uses a **priority queue** (min-priority queue):

- each node is stored with priority `g(n)`,
- the node with smallest `g(n)` is expanded first.

This is different from:

- BFS (FIFO queue)
- DFS (LIFO stack)

UCS chooses by cost, not by depth.

---

## 3. Simple Procedure

1. Put the start node in the priority queue with cost `0`.
2. Repeat until the queue is empty:
3. Remove the node with the smallest `g(n)`.
4. If it is the goal, stop and return the path.
5. Expand it, compute new costs for successors, and push/update them in the queue.

In graph search, we keep the best known cost for each state and ignore worse duplicates.

---

## 4. Real-World Illustration

Imagine you want to travel from home to school:

- Route A has 3 roads but heavy tolls.
- Route B has 5 roads but almost no tolls.

BFS may prefer Route A because it has fewer steps.
UCS may prefer Route B because the **total cost** is lower.

UCS answers:

> "Which path is cheapest overall?"  
not  
> "Which path has fewer moves?"

---

## 5. Key Guarantee

UCS is:

- **Complete** if step costs are bounded below by a positive value `epsilon > 0`.
- **Optimal** when all step costs are non-negative.

This is why UCS is the standard uninformed method for unequal edge costs.

Also, if all step costs are equal (for example, every edge cost = 1), UCS behaves like BFS.

---

## 6. Complexity

UCS complexity depends on the cost structure, not just depth.

A common bound is:

- Time and space are exponential in the number of nodes with path cost less than or equal to the optimal goal cost.

In practical terms:

- UCS can still be expensive,
- but it gives the right answer for minimum-cost paths under its conditions.

---

## 7. When UCS Is a Good Choice

Use UCS when:

- action costs are different,
- and lowest total cost matters.

Avoid UCS when:

- memory is extremely limited,
- or a fast approximate answer is enough.

---

## 8. Why UCS Matters in the Lineage

UCS is an important step in classical AI because it introduces a stronger decision rule:

- not just "closest in depth,"
- but "best cumulative cost so far."

This is still not learning.
It is still explicit search.

But it moves AI closer to optimization thinking, which becomes central later in the lineage.

---

## 9. Transition to Shared Structure

Now we have seen three uninformed strategies:

- BFS (depth-by-level),
- DFS (deep-first),
- UCS (cost-first).

Underneath their differences, they all share one common backbone.

That is what we formalize next in **Chapter 2.2.5: The Shared Structure**.
