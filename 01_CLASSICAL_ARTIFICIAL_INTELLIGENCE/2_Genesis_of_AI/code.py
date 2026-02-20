"""
This is an illustration of Intelligence as goal-directed behavior.

The Agent moves towards a defined goal. This Agent exhibits strict planning by following a pattern.
Note: We can swap in a Human-like agent that uses randomness instead.

Perception -> Decision -> Action loop, is implimented with perceive, decide, and act.

Symbol manipulation is enough. 
Actions like "increment"/"decrement" are symbolic manipulations of state.
"""

from abc import ABC, abstractmethod


class Environment(ABC):
    """ An abstraction for the Environment class """

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def perform_action(self, action):
        pass

    @abstractmethod
    def is_terminal(self):
        pass


class NumberLineEnvironment(Environment):
    """ The Environment class """

    def __init__(self, start=0, goal=5):
        self.state = start
        self.goal = goal

    def get_state(self):  # type: ignore
        return self.state

    def perform_action(self, action):
        if action == "increment":
            self.state += 1
        elif action == "decrement":
            self.state -= 1

        print(f"Action: {action}, New State: {self.state}")

    def is_terminal(self):  # type: ignore
        return self.state == self.goal


class Agent(ABC):
    """ An abstraction for the Agent class """

    @abstractmethod
    def perceive(self, state):
        pass

    @abstractmethod
    def decide(self):
        pass

    @abstractmethod
    def act(self, environment: Environment):
        pass


class GoalDirectedAgent(Agent):
    """ The Agent (a simple goal-directed agent) """

    def __init__(self, goal):
        self.goal = goal
        self.current_state = None
        self.plan = []

    def perceive(self, state):
        self.current_state = state

    def decide(self):
        # very naive planning: move towards goal if not already there
        if self.current_state < self.goal:
            self.plan = ["increment"]
        elif self.current_state > self.goal:
            self.plan = ["decrement"]
        else:
            self.plan = []

    def act(self, environment):
        if self.plan:
            action = self.plan.pop(0)
            environment.perform_action(action)


# Let's run our agent inside the environment
def run_simulation():
    env = NumberLineEnvironment(start=0, goal=5)
    agent = GoalDirectedAgent(goal=5)

    while not env.is_terminal():
        state = env.get_state()
        agent.perceive(state)
        agent.decide()
        agent.act(env)

    print(f"Goal reached: {env.get_state()}")


if __name__ == "__main__":
    run_simulation()


"""
Explanation:

1. Initially, we defined an Environment class 'NumberLineEnvironment'.
In this Environment, we defined:
    a. The state, 
    b. The termination, and 
    c. The possible actions the agent can perform in the environment

2. We defined the Agent class 'GoalDirectedAgent'.
In this Agent class we defined:
    a. A method/way to perceive the state
    b. A decision making method 
    c. An action-enabled method

3. To run this setup:
    a. We initialized the Environment's object 'env', and we set the 'goal' to 5. This is the goal we want the agent (or any agent at that) that will act on the environment to achieve. Just like in our switching off the light task. The desired target we want the environment's state to be set to after the agent's actions have been performed.
    b. We also initialized the object of the Agent's class and also set the same goal for the agent.

4. We kept a constant loop to keep checking if the agent has effected the environment enough that the state has now reached the intended goal. 
With this loop, the agent keeps affecting the environment's state till the goal is reached. The agent perceive the state, decide the actions to perform (depending on the perceived state), then act on the environment.

5. In every loop, we check the state, the agent perceive the (new) state from the environment, and updates it's own internal state's record, then decide on which best action moves it closer to the intended goal. Then it act on the environment to update the state of the environment.

"""
