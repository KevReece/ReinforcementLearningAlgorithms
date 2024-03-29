from agents.AbstractAgent import AbstractAgent
from agents.helpers.PolicyFunctions import PolicyFunctions
from environments.AbstractEnvironment import AbstractEnvironment
from agents.tables.QTable import QTable


class SarsaAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment, learning_rate=0.1, discount_factor=0.999, exploration_rate=0.2):
        self.q_table = QTable(environment.get_states_count(), environment.get_actions_count())
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.prior = None

    def get_action_policy(self, state):
        greedy_action_policy = self.q_table.get_greedy_action_policy(state)
        return PolicyFunctions.combine_policy_with_exploratory_policy(greedy_action_policy, self.exploration_rate)

    def post_act_learning(self, state, action, reward, next_state):
        if state == next_state:
            return
        if self.prior is not None:
            prior_state, prior_action, prior_reward = self.prior
            prior_q = self.q_table.table[prior_state][prior_action]
            current_q = 0
            if state is not None and action is not None:
                current_q = self.q_table.table[state][action]
            self.q_table.table[prior_state][prior_action] += self.learning_rate * (prior_reward + self.discount_factor * current_q - prior_q)
        self.prior = state, action, reward
    
    def post_episode_learning(self):
        self.post_act_learning(None, None, 0, None)
        self.prior = None

    def print(self):
        self.q_table.print()