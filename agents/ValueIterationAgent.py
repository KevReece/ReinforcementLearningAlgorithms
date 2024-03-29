from agents.AbstractAgent import AbstractAgent
from agents.helpers.DynamicsFunctions import DynamicsFunctions
from agents.helpers.BellmansEquations import BellmansEquations
from agents.helpers.PolicyFunctions import PolicyFunctions
from environments.AbstractEnvironment import AbstractEnvironment


class ValueIterationAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment, discount=0.9):
        self.n_actions = environment.get_actions_count()
        environment_probabilities = DynamicsFunctions.build_environment_probabilities(environment)
        environment_rewards = environment.get_reward_values()
        self.policy = BellmansEquations.policy_value_iteration(environment.get_states_count(), self.n_actions, discount, environment_probabilities, environment_rewards)

    def get_action_policy(self, state):
        policy_action = self.policy[state]
        return PolicyFunctions.single_action_as_action_probabilities(policy_action, self.n_actions)

    def print(self):
        print(self.policy)