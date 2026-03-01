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

1. Put the start node in a **frontier** (the data structure that holds unexplored nodes).
2. Repeat:
   - If frontier is empty, return failure.
   - **Remove one node from frontier** (based on a rule) ← This is the key difference!
   - If node is a goal, return success or path.
   - Expand node and generate successors.
   - Add valid successors to frontier (while handling repeats).

The real difference is simple:

> The algorithms differ mostly in how they manage the frontier.

---

## 2. Visual Comparison: Same Graph, Different Frontiers

Let's see how all three algorithms explore the same graph:

```
    A
   / \
  B   C
 / \   \
D   E   F
```

### BFS (Queue - FIFO):
```
Step 1: Queue: [A] → Remove A (front)
Step 2: Queue: [B, C] → Remove B (front)
Step 3: Queue: [C, D, E] → Remove C (front)
Step 4: Queue: [D, E, F] → Remove D (front)
...
Order: A → B → C → D → E → F (level by level)
```

### DFS (Stack - LIFO):
```
Step 1: Stack: [A] → Pop A (top)
Step 2: Stack: [B, C] → Pop C (top)
Step 3: Stack: [B, F] → Pop F (top)
Step 4: Stack: [B] → Pop B (top)
...
Order: A → C → F → B → E → D (deep first)
```

### UCS (Priority Queue - by cost):
```
Step 1: PQueue: [(A,0)] → Remove A (lowest cost)
Step 2: PQueue: [(B,cost_b), (C,cost_c)] → Remove cheapest
Step 3: Continues removing lowest-cost node...
Order: Depends on edge costs (cheapest path first)
```

**Same graph. Same goal. Different frontier management. Different exploration order.**

---

## 3. The Three Shared Building Blocks

### 1. Frontier (open list)

The frontier stores nodes discovered but not yet expanded.

- **BFS:** frontier is a FIFO queue.
- **DFS:** frontier is a LIFO stack.
- **UCS:** frontier is a min-priority queue by g(n).

### Visual Comparison of Data Structures:

```
QUEUE (BFS - FIFO):
FRONT [1][2][3][4][5] BACK
      ↑           ↑
    Remove       Add
    
Order: 1 → 2 → 3 → 4 → 5
Analogy: Coffee shop line


STACK (DFS - LIFO):
      [5]  ← TOP (Add/Remove)
      [4]
      [3]
      [2]
      [1]  ← BOTTOM
      
Order: 5 → 4 → 3 → 2 → 1
Analogy: Stack of plates


PRIORITY QUEUE (UCS - Min-Cost):
       (A,1)  ← Lowest cost
      /     \
   (B,3)   (C,2)
   /   \     /  \
(D,5) (E,4) ...

Order: A(1) → C(2) → B(3) → E(4) → D(5)
Analogy: Hospital emergency room
```

### 2. Repeated-state handling (visited or best-cost memory)

Without repeat handling, search can loop and waste time.

- **BFS and DFS** commonly use a `visited` set.
- **UCS** tracks best known path cost to each state.

### 3. Termination condition

Search stops when:

- A goal is found, or
- There are no more nodes to explore.

---

## 4. Same Problem Frame, Different Expansion Rule

All three still use the same formal problem setup:

- Initial state s₀
- Actions A(s)
- Transition model T(s, a) → s'
- Goal test Goal(s)
- (For UCS) path cost function

What changes is the **node-selection rule**:

| Algorithm | Data Structure | Selection Rule | What It Optimizes |
|-----------|---------------|----------------|-------------------|
| BFS | FIFO Queue | Smallest depth | Fewest steps |
| DFS | LIFO Stack | Greatest depth | Memory usage |
| UCS | Priority Queue | Smallest cost g(n) | Lowest total cost |

This is why we call them one family of algorithms.

---

## 5. The Frontier is Everything

Here's the profound insight:

**If you change only the frontier data structure, you change the entire search behavior.**

```python
# Pseudocode showing the shared structure

def generic_search(problem, frontier_type):
    frontier = frontier_type()  # Queue, Stack, or PriorityQueue
    frontier.add(problem.initial_state)
    visited = set()
    
    while not frontier.is_empty():
        node = frontier.remove()  # The ONLY difference!
        
        if problem.is_goal(node):
            return solution(node)
        
        visited.add(node)
        
        for successor in problem.get_successors(node):
            if successor not in visited:
                frontier.add(successor)
    
    return failure
```

The algorithm is identical. Only the frontier type changes.

- `frontier = Queue()` → BFS
- `frontier = Stack()` → DFS  
- `frontier = PriorityQueue()` → UCS

---

## 6. Real-World Illustration

Think of searching for a lost book in a big library.

- The building and rooms are the same problem space.
- Your search method changes your behavior:
  - BFS: check nearby shelves first, layer by layer.
  - DFS: follow one aisle deeply before changing aisle.
  - UCS: if moving between sections has different time or cost, pick the cheapest next move.

Same world.
Same goal.
Different frontier rule.

---

## 7. What This Reveals About Classical AI

This shared structure teaches a big lineage lesson:

> In early AI, intelligence was often "good control over search," not learning from data.

The system is still:

- Explicit
- Rule-based
- Hand-designed

Performance improvements come from smarter search control, data structures, and cost handling.

---

## 8. Limits Shared by All Three

Even with different frontier rules, these methods still face common limits:

- State spaces can explode combinatorially,
- Memory can become a bottleneck,
- Runtime can become very high,
- There is no heuristic guidance toward likely goals.

They are foundational, but not enough for large real-world problems.

---

## 9. Key Takeaway

BFS, DFS, and UCS are not three unrelated ideas.
They are three variants of one search skeleton.

Once you understand the shared skeleton, you can read many later AI algorithms more easily.

---

## 10. Key Insight: The Power of Data Structures

**The choice of data structure determines the intelligence of the search.**

- Queue (FIFO) → Explores systematically by distance → Finds shortest paths
- Stack (LIFO) → Explores deeply and efficiently → Saves memory
- Priority Queue → Explores by cost → Finds optimal paths

This is a fundamental lesson in computer science and AI:

> The right data structure can completely change the behavior and performance of an algorithm.

Early AI researchers discovered that intelligence could be engineered through clever control structures, not just clever rules.

---

## 11. Transition in the Lineage

This closes the uninformed-search block.

We now have:

- Formal state-space modeling,
- And systematic search procedures over that space.

Next, the pressure for speed and scalability pushes AI toward more informed guidance and, later in the lineage, toward probability and learning-based methods.
