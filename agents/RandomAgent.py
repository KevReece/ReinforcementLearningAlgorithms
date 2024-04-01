from agents.AbstractAgent import AbstractAgent
from environments.AbstractEnvironment import AbstractEnvironment


class RandomAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment):
        self.actions_count = environment.get_actions_count()

    def get_action_policy(self, _):
        return [1/self.actions_count] * self.actions_count