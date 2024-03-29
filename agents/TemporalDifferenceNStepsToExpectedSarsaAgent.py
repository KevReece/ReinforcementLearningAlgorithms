from agents.AbstractAgent import AbstractAgent
from agents.helpers.PolicyFunctions import PolicyFunctions
from environments.AbstractEnvironment import AbstractEnvironment
from agents.tables.QTable import QTable


class TemporalDifferenceNStepsToExpectedSarsaAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment, learning_rate=0.2, discount_factor=0.999, exploration_rate=0.2, n_steps=2):
        self.q_table = QTable(environment.get_states_count(), environment.get_actions_count())
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.n_steps = n_steps
        self.priors = []

    def get_action_policy(self, state):
        greedy_action_policy = self.q_table.get_greedy_action_policy(state)
        return PolicyFunctions.combine_policy_with_exploratory_policy(greedy_action_policy, self.exploration_rate)

    def post_act_learning(self, state, action, reward, next_state):
        if state == next_state:
            return
        self.priors.append((state, action, reward, next_state))
        if len(self.priors) >= self.n_steps:
            self._update_once_from_priors()

    def post_episode_learning(self):
        while(self.priors):
            self._update_once_from_priors()

    def _update_once_from_priors(self):
        returns = 0
        target_state, target_action, _, _ = self.priors[0]
        for step in range(min(self.n_steps, len(self.priors))):
            _, _, step_reward, _ = self.priors[step]
            returns += step_reward * self.discount_factor ** step
        if len(self.priors) == self.n_steps:
            _, _, _, last_step_next_state = self.priors[self.n_steps-1]
            last_step_expected_q = sum(self.q_table.table[last_step_next_state]) / len(self.q_table.table[last_step_next_state])
            returns += last_step_expected_q * self.discount_factor ** self.n_steps
        target_current_q = self.q_table.table[target_state][target_action]
        self.q_table.table[target_state][target_action] += self.learning_rate * (returns - target_current_q)
        self.priors.pop(0)

    def print(self):
        self.q_table.print()