# Chapter 2.2.4: Uniform-Cost Search (UCS)

In DFS, we saw that going deep first can save memory.
But DFS and BFS both miss one key thing:

> Not all actions have the same cost.

Uniform-Cost Search (UCS) solves that problem.

---

## 1. Core Idea

UCS always expands the node with the **lowest path cost so far**.

This path cost is written as:

g(n) = cumulative cost from the start node to node n.

UCS is cost-aware from the beginning.

---

## 2. How UCS Priority Queue Works

The key to understanding UCS is the **priority queue** (min-priority queue):

- Each node is stored with its **cumulative cost g(n)**
- The node with the **smallest g(n)** is always expanded first

This means **the cheapest path found so far gets explored first**, which creates the "lowest-cost-first" behavior.

This is different from:
- **BFS (FIFO queue)** - expands by depth/order
- **DFS (LIFO stack)** - expands by recency
- **UCS (priority queue)** - expands by cost

### Visual Representation of a Priority Queue:

```
    Priority Queue (Min-Heap)
    Ordered by cost g(n)
    
         (A, 1)  ← Lowest cost, removed first
        /      \
    (B, 3)    (C, 2)
    /    \      /   \
 (D, 5) (E, 4) (F, 6) (G, 7)

Operation: Always remove the node with SMALLEST cost
           New nodes inserted based on their cost

Example removal order: A(1) → C(2) → B(3) → E(4) → D(5)...
```

**Real-World Analogy:**

Think of a priority queue like an emergency room at a hospital:
- Patients don't get treated in the order they arrive (not FIFO like BFS)
- They don't get treated by who arrived most recently (not LIFO like DFS)
- Instead, patients are treated by **urgency/priority**
- A critical patient who arrives later gets treated before someone with a minor injury who arrived earlier
- The "cost" here is the severity - lowest severity (highest priority) gets treated first

This is exactly how UCS works: it doesn't care about arrival order or depth - only about which path has accumulated the lowest cost so far.

---

## 3. Visual Example

Let's say you have this graph with edge costs:

```
      A
    /   \
   1     4
  /       \
 B         C
  \       /
   2     1
    \   /
      D
```

**Step-by-step execution:**

1. Create an empty Priority Queue
```
    Priority Queue (Min-Heap)
    Empty
    
PQueue: []
```

2. **PQueue: []** → Add the start Node 'A' with cost 0
```
         (A, 0)  ← Lowest cost (Added 'A' with cumulative cost 0)
         
PQueue: [(A, 0)]
```

3. **PQueue: [(A, 0)]** → Remove A (cost 0), add its neighbors with their costs
```
         (B, 1)  ← Lowest cost (Removed 'A', added 'B' with cost 1 and 'C' with cost 4)
        /
    (C, 4)
    
PQueue: [(B, 1), (C, 4)]
```

4. **PQueue: [(B, 1), (C, 4)]** → Remove B (cost 1), add its neighbors
```
         (D, 3)  ← Lowest cost (Removed 'B', added 'D' with cost 1+2=3)
        /
    (C, 4)
    
PQueue: [(D, 3), (C, 4)]
```

5. **PQueue: [(D, 3), (C, 4)]** → Remove D (cost 3), not C!
```
         (C, 4)  ← Lowest cost remaining
         
PQueue: [(C, 4)]
```

6. **PQueue: [(C, 4)]** → Remove C (cost 4)...

Notice how we explored **A → B → D → C** even though C is a direct child of A. Why? Because the path A→B→D (cost 3) is cheaper than exploring C (cost 4) directly.

**Path costs:**
- A → B: cost 1
- A → C: cost 4
- A → B → D: cost 1 + 2 = 3
- A → C → D: cost 4 + 1 = 5

UCS found the cheaper path to D!

---

## 4. Why It Chooses by Cost

When you add nodes to the priority queue, they are automatically ordered by their cumulative cost g(n).

This creates a pattern where:
- Cheaper paths are always explored before expensive ones
- Even if a node is "closer" in steps, a cheaper longer path might be explored first
- The first time we reach the goal, we have found the optimal (lowest-cost) path

---

## 5. Simple Procedure

1. Put the start node in the priority queue with cost 0.
2. Repeat until the queue is empty:
   - Remove the node with the smallest g(n) ← This is key! Always the cheapest
   - If it is the goal, stop and return the path ← Guaranteed optimal!
   - Otherwise, expand it and compute new costs for successors
   - Add successors to the queue (or update if we found a cheaper path)

In graph search, we keep the best known cost for each state and ignore worse duplicates.

The confusion might be: "Why not just use BFS if we want the shortest path?"

**Answer:** BFS finds the shortest path in **number of steps**, but UCS finds the shortest path in **total cost**. When actions have different costs, these are not the same thing!

---

## 6. Real-World Illustration

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

## 7. Key Guarantee

UCS is:

- **Complete** if step costs are bounded below by a positive value ε > 0.
- **Optimal** when all step costs are non-negative.

This is why UCS is the standard uninformed method for unequal edge costs.

Also, if all step costs are equal (for example, every edge cost = 1), UCS behaves like BFS.

---

## 8. Complexity

UCS complexity depends on the cost structure, not just depth.

A common bound is:

- Time and space are exponential in the number of nodes with path cost less than or equal to the optimal goal cost.

In practical terms:

- UCS can still be expensive,
- But it gives the right answer for minimum-cost paths under its conditions.

---

## 9. When UCS Is a Good Choice

Use UCS when:

- Action costs are different,
- And lowest total cost matters.

Avoid UCS when:

- Memory is extremely limited,
- Or a fast approximate answer is enough.

---

## 10. Why UCS Matters in the Lineage

UCS is an important step in classical AI because it introduces a stronger decision rule:

- Not just "closest in depth,"
- But "best cumulative cost so far."

This is still not learning.
It is still explicit search.

But it moves AI closer to optimization thinking, which becomes central later in the lineage.

---

## 11. Key Insight

**Priority Queue (by cost) = Cost-First = Optimal Path**
- Cheapest path explored first
- Guarantees optimal solution when costs are non-negative
- Generalizes BFS to handle unequal costs

**Queue (FIFO) = Breadth-First = Shortest Steps**
- Oldest addition explored first
- Guarantees shortest path in number of steps
- Special case of UCS when all costs equal 1

**Stack (LIFO) = Depth-First = Memory Efficient**
- Newest addition explored first
- No optimality guarantee
- Uses less memory

The data structure choice determines what we optimize for: cost, steps, or memory!

---

## 12. Transition to Shared Structure

Now we have seen three uninformed strategies:

- BFS (depth-by-level),
- DFS (deep-first),
- UCS (cost-first).

Underneath their differences, they all share one common backbone.

That is what we formalize next in **Chapter 2.2.5: The Shared Structure**.
