# State Spaces Actions Transitions

- From Section 1, we learned that classical AI implemented intelligent behavior through explicit symbolic and rule-based manipulation.

- However, this immediately raises a critical question:
  `What happens when the number of possible states become extremely large?`

- If an agent must choose actions across thousands, millions, or even billions of possible states (or symbols), explicit enumeration quickly becomes infeasible.

# The core abstraction

- Every classical AI problem was reduced to:
  `Search over a state space.`

- Formally:
  - `State` (s): A complete decription of the world at a point in time.
  - `Action` (a): A legal operation the agent can perform
  - `Transition Function` (T):

  <br> This relationship can be represented mathematically as:
  `T: S × A → S, where T(s, a) = s'`

- This gives rise to a `state graph`, where:
  - **Nodes** = state
  - **Edges** = actions
  - **Paths** = plans/solutions

- Example (canonical):
  - 8-puzzle problem
    - State: arrangement of tiles
    - Actions: move blank tile (up/down/left/right)
    - Transition: deterministic tile swap
    - Goal: match target configuration

- Everything is explicit.

- Nothing is learned!

## Why this abstraction was powerful

- Because many problems collapse into this form, e.g.:
  - Chess
  - Mazes
  - Scheduling
  - Planning
  - Logic inference
  - Game playing

- And once mapped to a state space, the problem becomes algorithms.

- That is, once we have a state space correctly defined and its symbol correctly mapped to, then the only thing left is seeking an alogrithm that can correctly and efficiently manipulate the symbol to achieve the desired goal.

- These Algorithms are essential and we will talk more on them in the Algorithms subsections (traditonal and heuristic algorithms).
