# What Artificial INtelligence Originally meant

## Intelligence as Goal-Directed Behavior

- The original problem AI tried to solve was not 'thinking'.

- When the field of Artificial Intelligence was born in the 1950s - 1960s, the core quetion was not:
  "How do we make machines think like humans?"

- That framing came later and caused decades of confusion.

- The original operational questions was:
  "How can we build systems that behave intelligently in pursuit of goals?"

- This is a fundamentally different question, and this distinction matters deeply. Because it defines AI as 'Behavioral competence', rather than 'Internal experience'.

- The focus was on creating systems that could perform tasks effectively, adapt to new situations, and achieve objectives, rather than replicating human thought processes.

## Personal Reflection

- Initially, I felt that was a letdown. I wanted to build machines that could think like humans. But after careful reflection, I realized that this goal-directed behavior perspective was more practical and achievable.
- In the field of Neuroscience (which I also belong to), the human brain is made up of billions of neurons working together to produce behavior; and millions of years of evolution have shaped our cognitive abilities.
- Trying to create a machine that thinks like a human is not only incredibly complex but also unnecessary for many applications. We have a 'seamingly capable brain', what we need now is how to extend it or maybe complement it with machine that can perform better where it's lacking (e.g., in the computational power).

## Intelligence as a Control Problem

- Intelligence can be understood as the ability to achieve goals in a wide range of environments.

- At its core, intelligence involves:
  - Perceiving the environment
  - Making decisions based on that perception
  - Taking actions that lead to desired outcomes

- At its earliest and cleanest abstraciton, intelligence was modeled as:
  "A system thats selects actions to achieve goals under constraints."

- This framing delibrately avoids:
  - Emotions
  - Consciousness
  - Creativity
  - Human likeness

- Instead, we focused on:
  - Goals
  - Actions
  - Outcomes

* This makes intelligence a control problem, not a psychological one.

## The minimal ingredients of goal-directed behavior

- To define intelligence as goal-directed behavior, we need to identify the minimal ingredients required for a system to exhibit such behavior:
  - An **Agent**: The entity that perceives the environment and takes actions. Something that can act in the environment.
  - **Environment**: The external context in which the system operates. Something the goal acts within.
  - **Perception**: The ability to sense and interpret the environment. Some way of observing (the 'state' of the) environment.
  - **Action**: The capability to perform actions that can influence the environment. A set of possible interventions the agent can take.
  - **Goal/Objective**: Clearly defined objectives that the system aims to achieve. A criterion for success (that helps the agent to distinguish between good and bad outcomes).

- That's it.

- No learning is required. No probability. No reasoning. No data.

* This means that AI is all about setting a desired goal (say, switching off the light), then asking a program (the Agent in this case) to perform the task for the goal.

* But before we do this, we wanted a condition: 'Only switch off the light during the daytime'.

- Now that we have the full concept of what we want and the conditions involved, we can begin structuring out how we want to go about it. Below are the parameters involved in this simple task:
  - Agent: The software we want to build for this task (That will switch off the light).
  - Environment: This will be the room whose light we want to switch off.
  - Perception: This will be how the agent will be able to perceive the room's state. How does the agent get to know if we are in the daytime or nighttime?
  - Action: This is exactly what step or act we want the agent to go through in order to achieve its goal/object.
  - Goal/Objective: This is the goal we set for the agent or what we want the agent to perform.

- Just a system that can perceive and act in a given environment in order to achieve a set of goals.

## Why this definition was revolutionary

- This definition was revolutionary because it allows researches to say:
  - A chess program is intelligent
  - A route-finding system is intelligent
  - A theorem prover is intelligent

* Regardless of:
  - Even if none of them 'understand' anything they are doing (in the human sense).
  - They only need to get the 'job done'.
  - Because all these systems can be described as goal-directed behavior systems.

* This is because they:
  - Pursue explicit goals (winning the game, finding the route, proving the theorem).
  - Operate in specific environments (the chessboard, the map, the logical space).
  - Perceive relevant information (the positions of pieces, the layout of roads, the premises of the theorem).
  - Take actions (making moves, choosing paths, applying inference rules).
  - With consistent improvement towards their objectives.

## Intelligence is NOT Correctness

- A crucial insight from this perspective is that intelligence is not about being 'correct' or 'true' in a philosophical sense.
  - An intelligent system can fail and still be intelligent.

- Intelligence is about effectiveness and adaptability in achieving goals. Not about always being right.

- This is because intelligence is about decision quality relative to information and constraints, not about absolute truth or perfection.

### To Keep in Mind

- This idea of intelligence as goal-directed behavior later influenced many areas of AI research, including:
  - Reinforcement learning
  - Probabilistic reasoning
  - Bounded rationality
  - Modern agent design

## Intuition

- Abstractly, an agent can be seen as implementing a function:

  `Agent function: Action = f(Perception, Goal)`

- Where:
  - Action: represents the decision or move the agent makes to influence the environment.
  - f: A function that defines the relationship between percepts, goals, and actions. The function f indicates that the action taken by the agent is a function of both its perceptions and its goals.
  - Perception: represents the current state of the environment as observed by the agent.
  - Goal: represents the desired outcome or objective the agent aims to achieve.

- This can also be represented in simpler terms as:
  - `Agent Function: Percepts → Actions`
  - Where:
    - π: This is the policy function that maps percepts to actions.
    - Percepts: These are observations from the environment.
    - Actions: These influence future states of the environment.

- At this stage in history:
  - π was hand-designed by researchers based on their understanding of the task and environment.
  - Not learned from data.
  - Not optimized from data.
  - The focus was on creating effective policies for specific tasks rather than learning from data.

- This is the seed from which everything else grows.

## Why this early stage framing survives to modern Agentic AI

- Even in today's most advanced systems:
  - LLM agents
  - Tool-using systems
  - Multi-agent workflows
  - MCP-orchestrated architectures
    The core idea remains the same:
    "Build systems that can perceive their environment, make decisions, and take actions to achieve specific goals."

- What changes later is how we design the function f or the policy π:
  - Using probabilistic models
  - Using learning algorithms
  - Using optimization techniques

- Meaning, we changed how:
  - policies are represented
  - goals are specified
  - actions are chosen
  - feedback is incorporated

- But the fundamental framework of goal-directed behavior remains intact.

## The hidden consequence

- By defining intelligence this way, early AI implictly assumed:
  - The world is describable in terms of goals.
  - Goals are specifiable and measurable.
  - Good behavior can be engineered through appropriate action selection.

- This led to several implicit assumptions about intelligence:
  - That intelligence can be fully captured by observable behavior.
  - That internal states (like beliefs, desires, or emotions) are not necessary for intelligent action.
  - That a system's ability to achieve goals is the primary measure of its intelligence.

- These assumptions will break later - and that break gives birth to:
  - Probability
  - Learning
  - Neural Networks
  - Representation Learning
  - LLMs
  - Agentic Systems

- But at this early stage, the clarity of defining intelligence as goal-directed behavior provided a solid foundation for the field of AI to build upon.

## Conclusion

- Remember that:
  `Intelligence began as engineered goal-directed behavior, not learning or human-like thought.`

- Everything else in this journey exists because engineering intelligence by hand does not scale.
