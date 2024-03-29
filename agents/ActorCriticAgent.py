from agents.AbstractAgent import AbstractAgent
from environments.AbstractEnvironment import AbstractEnvironment
from agents.helpers.SoftmaxFunctions import SoftmaxFunctions
from agents.tables.QTable import QTable
from agents.tables.StateValueTable import StateValueTable


class ActorCriticAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment, discount=0.9, learning_rate=0.1, softmax_temperature=0.9):
        self.learning_rate = learning_rate
        self.softmax_temperature = softmax_temperature
        self.discount = discount
        self.critic_state_value_table = StateValueTable(environment.get_states_count())
        self.actor_q_table = QTable(environment.get_states_count(), environment.get_actions_count())

    def get_action_policy(self, state):
        return SoftmaxFunctions.actions_softmax(self.actor_q_table.table[state], self.softmax_temperature)

    def post_act_learning(self, state, action, reward, next_state):
        if state == next_state:
            return
        state_value = self.critic_state_value_table.table[state]
        next_state_value = self.critic_state_value_table.table[next_state]
        state_value_delta = reward + self.discount * next_state_value - state_value
        self.critic_state_value_table.table[state] += self.learning_rate * state_value_delta
        action_softmax = SoftmaxFunctions.action_softmax(self.actor_q_table.table[state], action, self.softmax_temperature)
        self.actor_q_table.table[state][action] += self.learning_rate * state_value_delta * (1 - action_softmax) / self.softmax_temperature

    def print(self):
        self.actor_q_table.print()