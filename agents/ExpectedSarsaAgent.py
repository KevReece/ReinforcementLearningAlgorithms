from agents.AbstractAgent import AbstractAgent
from agents.helpers.PolicyFunctions import PolicyFunctions
from environments.AbstractEnvironment import AbstractEnvironment
from agents.tables.QTable import QTable


class ExpectedSarsaAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment, learning_rate=0.1, discount_factor=0.999, exploration_rate=0.2):
        self.q_table = QTable(environment.get_states_count(), environment.get_actions_count())
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    def get_action_policy(self, state):
        greedy_action_policy = self.q_table.get_greedy_action_policy(state)
        return PolicyFunctions.combine_policy_with_exploratory_policy(greedy_action_policy, self.exploration_rate)

    def post_act_learning(self, state, action, reward, next_state):
        if state == next_state:
            return
        current_q = self.q_table.table[state][action]
        expected_q = sum(self.q_table.table[next_state]) / len(self.q_table.table[next_state])
        self.q_table.table[state][action] += self.learning_rate * (reward + self.discount_factor * expected_q - current_q)

    def print(self):
        self.q_table.print()