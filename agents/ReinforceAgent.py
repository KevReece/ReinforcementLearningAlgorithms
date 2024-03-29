from agents.AbstractAgent import AbstractAgent
from environments.AbstractEnvironment import AbstractEnvironment
from agents.helpers.SoftmaxFunctions import SoftmaxFunctions
from agents.tables.QTable import QTable
from agents.tables.StateValueTable import StateValueTable


class ReinforceAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment, discount=0.9, learning_rate=0.1, softmax_temperature=0.9):
        self.learning_rate = learning_rate
        self.softmax_temperature = softmax_temperature
        self.discount = discount
        self.critic_state_value_table = StateValueTable(environment.get_states_count())
        self.actor_q_table = QTable(environment.get_states_count(), environment.get_actions_count())
        self.priors = []

    def get_action_policy(self, state):
        return SoftmaxFunctions.actions_softmax(self.actor_q_table.table[state], self.softmax_temperature)

    def post_act_learning(self, state, action, reward, next_state):
        if state == next_state:
            return
        self.priors.append((state, action, reward, next_state))

    def post_episode_learning(self):
        step_discount = self.discount ** (len(self.priors)-1)
        returns = 0
        for step in range(len(self.priors)-1, -1, -1):
            state, action, reward, _ = self.priors[step]
            returns = reward + step_discount * returns
            state_value_delta = returns - self.critic_state_value_table.table[state]
            self.critic_state_value_table.table[state] += self.learning_rate * state_value_delta
            action_softmax = SoftmaxFunctions.action_softmax(self.actor_q_table.table[state], action, self.softmax_temperature)
            self.actor_q_table.table[state][action] += self.learning_rate * state_value_delta * step_discount * (1 - action_softmax) / self.softmax_temperature
            step_discount /= self.discount
        self.priors = []

    def print(self):
        self.actor_q_table.print()