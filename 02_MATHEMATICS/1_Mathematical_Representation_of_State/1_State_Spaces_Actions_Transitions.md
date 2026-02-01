# State Spaces Actions Transitions

- From Section 1, we learnt that we can manipulating symbols leads to intelligence.

- But, say we have an extremly large number of symbols, how will it affect the performance of our agent?

- Or how de we efficiently map to each symbol?

- This lead us to the concept of `SEARCHING`.

- Where we need a form of way to correctly seek and identify the corresponding 'state' and it's symbol.

- Say, for example, we have a state A, we then map it to a corresponding symbol 1. With this, the agent can successfully implement the rules of the symbol 1 on the state A.

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
