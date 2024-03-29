import random
from agents.AbstractAgent import AbstractAgent
from agents.helpers.PolicyFunctions import PolicyFunctions
from environments.AbstractEnvironment import AbstractEnvironment
from agents.tables.QTable import QTable


class DoubleQLearningAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment, learning_rate=0.1, discount_factor=0.999, exploration_rate=0.2):
        self.q_table1 = QTable(environment.get_states_count(), environment.get_actions_count())
        self.q_table2 = QTable(environment.get_states_count(), environment.get_actions_count())
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    def get_action_policy(self, state):
        greedy_action_policy = [
            (q1 + q2) / 2 
            for q1, q2 in zip(self.q_table1.table[state], self.q_table2.table[state])
        ]
        return PolicyFunctions.combine_policy_with_exploratory_policy(greedy_action_policy, self.exploration_rate)

    def post_act_learning(self, state, action, reward, next_state):
        if state == next_state:
            return
        if random.choice([True, False]):
            q_table = self.q_table1.table
            source_q_table = self.q_table2.table
        else:
            q_table = self.q_table2.table
            source_q_table = self.q_table1.table
        max_action = q_table[next_state].index(max(q_table[next_state]))
        q_table[state][action] += self.learning_rate * (reward + self.discount_factor * source_q_table[next_state][max_action] - q_table[state][action])

    def print(self):
        self.q_table1.print()
        self.q_table2.print()
