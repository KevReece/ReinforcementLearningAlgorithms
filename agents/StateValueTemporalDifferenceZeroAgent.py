from agents.AbstractAgent import AbstractAgent
from agents.helpers.PolicyFunctions import PolicyFunctions
from environments.AbstractEnvironment import AbstractEnvironment
from agents.tables.StateValueTable import StateValueTable


class StateValueTemporalDifferenceZeroAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment, learning_rate=0.2, discount_factor=0.999, exploration_rate=0.2):
        self.state_value_table = StateValueTable(environment.get_states_count())
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.environment = environment

    def get_action_policy(self, state):
        action_to_next_state_dynamics = self.environment.get_action_next_states(state)
        goal_dynamics = self.environment.get_exit_states()
        greedy_action_policy = self.state_value_table.get_greedy_action_policy(action_to_next_state_dynamics, goal_dynamics)
        return PolicyFunctions.combine_policy_with_exploratory_policy(greedy_action_policy, self.exploration_rate)

    def post_act_learning(self, state, _, reward, next_state):
        if state == next_state:
            return
        next_state_value = self.state_value_table.table[next_state]
        current_state = self.state_value_table.table[state]
        self.state_value_table.table[state] += self.learning_rate * (reward + self.discount_factor * next_state_value - current_state)

    def print(self):
        self.state_value_table.print()