# The Environment-Agent Loop

(Perception -> Decision -> Action)

## Why this loop is the true birth of AI as a system

- Up to now, we've said:
  - Intelligence = goal-directed behavior
  - Agents should be rational, not human-like

But this is still incomplete.

- WHY?
  `Because intelligence does not exist in isolation.`

Because we can not just decide 'this is rational'. We have to also add what we are comparing it to.

- So, the moment researchers accepted reational agents, they were forced to answer a deeper questions:
  `Rational with respect to what?`

The answer is: `An Environment.`

This is the moment AI becomes a closed-loop systems, not a static algorithm.

## The core abstraction (this never go away)

- At the heart of all AI systems - classical or modern - is a `loop`.
  - `Perceive` the environment
  - `Decide` what to do
  - `Act` on the environment
  - `Observe` the consequences
  - `Repeat` the loop
    [PRADO]

- This is not a metaphor, it is a formal system boundary. One that holds true, even in modern systems.

- Once you define this loop, you can:
  - Reason about intelligence
  - Evaluate behavior
  - Compare systems
  - Generalize across domains

- Why 'loop' matters more than algorithms
  A static algorithm:
  - Take input
  - Produces output
  - Stops

- An intelligent agent:
  - Operates continuously
  - Reacts to change
  - Adapts behavior over time (even those without learning capabilities)

- This is the first step away from:
  - Theorem provers
  - Calculators
  - Batch programs
    and towards Agents.
    We are now moving towards agents that are able to continuously interact and effect the environment. Not just perform their action and stop.

## The three components, defined are

- Perception:
  - Perception answers:
    `What can the agent observe about the environment right now?`
  - Key Points:
    - Perception is partial, not complete
    - Observations are often noisy
    - The agent never sees the true state directly.
  - This limitation is not a bug - it's a defining constraint.

- Decision:
  - Decision answers:
    `Given what I observer, what action should I take?`
  - At this stage in history:
    - Decisions are rule-based
    - Policies are hand-written
    - No learning occurs
  - But critically:
    - Decisions depends on current perception
    - Not just forced logic

- Action:
  - Action answers:
    `How can the agent influence the environment?`
  - Actions:
    - Change the environment
    - Affect future perceptions
    - May have delayed consequences
  - This introduces `time` into intelligence

## The feedback principle (often overlooked)

- The agent's action:
  - Affect the environment
  - Which affects future perceptions
  - Which inturn affect future decisions

- This feedback loop creates:
  - Non-linearity
  - Compounding effects
  - Unintended consequences

- Later, this becomes central to:
  - Control theory
  - Reinforcement Learning
  - Agent Safety
  - Alignment problems
    But this 'uncertianty' of future states begins here.

## Formal but minimal abstraction

- At it's simplest, the loop can be described as:
  - Environment produces a percept (percept is the object of perception)
  - Agent applies a policy (policy: Percept -> Action)
  - Policy selects an action
  - Environment transitions

  No probability is required yet. No learning is also required yet. We just have simple interaction between an agent and it's environment.

## Why environments deserve equal attention

- Early AI failed repeatedly because:
  - Agents were studied in isolation
  - Environments were oversimplified
  - Assumptions were hidden

- This forced the field to explicitly model:
  - Environment dynamics
  - Observability
  - Determinism VS randomness
  - Episodic VS continuous interaction

## The quiet contraints of this ideology

- Once you define the agent loop, you can no longer pretend that:
  - Intelligence is static
  - Reasoning is timeless
  - Correctness is absolute

- Instead, you will see that:
  - Intelligence is situational
  - Decisions are contextual
  - Success is relative to the environment dynamics (mentioned above)

  This makes the `Perfect Logic` insufficient, and that pressure will crack symbolic AI open if not corrected.

## Why the Environment-Agent Loop survives

- Even today, LLM agents, Tool-using systems, Multi-Agent workflows, MCP-Orchestrated architectures all reduce to some:
  - `Perception` - (tokens, memory, retrieved context)
  - `Decision process` - (model + control logic)
  - `Action` - (tool calls, messages, state updates)

- The interface changed, but the loop did not.

## Conclusion

- You can see that:
  `Intelligence is not an algorithm, it is an ongoing interaction loop between an agent and an environment.`

#### Note

Once you understand this concept, you can start spotting fake intelligence immediately!

- The Environment-Agent loop forces a hard question:
  `If the environment is complex, how do we choose actions efficiently?`

- Answering this question leads us directly to:
  - State spaces
  - Transitions
  - Searches
  - Heuristics

We will be discussing all these in detail in the future, but for now we will explore Symbol Manipulations.
