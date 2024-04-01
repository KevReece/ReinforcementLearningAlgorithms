from agents.AbstractAgent import AbstractAgent
from agents.helpers.BellmansEquations import BellmansEquations
from agents.helpers.PolicyFunctions import PolicyFunctions
from environments.AbstractEnvironment import AbstractEnvironment


class PolicyIterationAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment, discount=0.9):
        self.n_actions = environment.get_actions_count()
        environment_rewards = environment.get_reward_values()
        self.policy = BellmansEquations.evaluate_and_improve_policy_iteration(environment.get_states_count(), self.n_actions, discount, environment, environment_rewards)

    def get_action_policy(self, state):
        policy_action = self.policy[state]
        return PolicyFunctions.single_action_as_action_probabilities(policy_action, self.n_actions)

    def print(self):
        print(self.policy)