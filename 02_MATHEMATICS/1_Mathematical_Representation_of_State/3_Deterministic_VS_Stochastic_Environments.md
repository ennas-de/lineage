# Chapter 2.1.3: Deterministic vs Stochastic Environments

In Chapter 2.1.2, we modeled intelligence as search over states using actions and transitions.

That model works very well, but only under one big condition:

> We must know what will happen after each action.

This gives us two kinds of environments.

## 1. Deterministic Environments

A deterministic environment means:

> Same state + same action = same next state, every time.

Formally:

`T(s, a) = s′`

or in probability form:

`P(s′ | s, a) = 1` for exactly one next state.

### Simple intuition

If you replay the same situation with the same move, you get the same result.

### Examples

- Chess (no hidden cards, no dice, fixed rules)
- Sudoku (a value you place stays what it is)
- Grid maze pathfinding with fixed walls

This is why early classical AI made strong progress in games, puzzles, and theorem proving.  
The world in those tasks was clean, known, and stable.

---

## 2. Stochastic Environments

A stochastic environment means:

> Same state + same action can lead to different next states.

Formally:

`P(s′ | s, a)` is a probability distribution over many possible next states.

No single outcome is guaranteed.

### Simple intuition

You can do the same thing twice and still get different outcomes.

### Examples

- Robot movement in the real world (wheels can slip, sensors can be noisy)
- Self-driving in traffic (other drivers behave unpredictably)
- Medical diagnosis (same symptoms can map to different true causes)
- Games with chance, like backgammon (dice add randomness)

---

## 3. Why This Difference Matters for AI

In deterministic settings:

- Planning is more direct
- Search trees are easier to trust
- A path found by the algorithm is usually reproducible

In stochastic settings:

- Planning must consider uncertainty
- The agent must reason about risk, not just logic
- Good decisions are based on expected outcomes, not guaranteed outcomes

So the core question changes from:

> "What action certainly works?"

to:

> "What action gives the best expected result?"

---

## 4. The Limitation This Revealed in Classical AI

Classical search methods often assumed:

- The state is known
- The transition is known
- The outcome is predictable

Real environments break these assumptions all the time.

This is the pressure point that pushed AI forward:

- from exact symbolic transitions
- to probabilistic modeling
- and later to statistical learning

So this section is a turning point in the lineage.

Deterministic thinking gave AI its first clear structure.
Stochastic reality forced AI to become mathematically deeper.

---

## 5. Key Takeaway

Deterministic environments helped us build the first strong AI formalisms.
Stochastic environments exposed their limits.

Once uncertainty enters the environment, probability is no longer optional.
