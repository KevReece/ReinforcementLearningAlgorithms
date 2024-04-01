import random
from agents.AbstractAgent import AbstractAgent
from environments.AbstractEnvironment import AbstractEnvironment
from environments.NoughtsAndCrossesTwoPlayerEnvironment import NoughtsAndCrossesTwoPlayerEnvironment


class NoughtsAndCrossesVersusAgentEnvironment(AbstractEnvironment):
    def __init__(self):
        self.environment = NoughtsAndCrossesTwoPlayerEnvironment()
        self.self_player = self.environment.Player.X
        self.opponent_player = self.environment.Player.O
        self.environment.reset()
    
    def set_opposition_agent(self, opponent: AbstractAgent):
        self.opponent = opponent

    def act(self, action: int):
        next_state = self.environment.act(action)
        while (self.environment.get_current_turn_player() == self.opponent_player 
                and not self.environment.is_done()):
            opponent_action_policy = self.opponent.get_action_policy(next_state)
            action = random.choices(self.environment.get_all_actions(), opponent_action_policy)[0]
            next_state = self.environment.act(action)
        reward = self.environment.calculate_reward(self.self_player)
        return reward, next_state

    def is_done(self):
        return self.environment.is_done()
    
    def print(self):
        self.environment.print()

    def reset(self):
        self.environment.reset()

    def get_all_actions(self):
        return self.environment.get_all_actions()
    
    def get_agent_state(self):
        return self.environment.get_state()
    
    def get_initial_state_rewards(self):
        return self.environment.get_initial_state_rewards(self.self_player)
    
    def get_reward_values(self):
        return self.environment.get_reward_values()
    
    def get_states_count(self):
        return self.environment.get_states_count()
    
    def get_actions_count(self):
        return self.environment.get_actions_count()
    
    def get_exit_states(self):
        return self.environment.get_exit_states()
    
    def get_probability_of_next_state_and_reward_given_state_and_action(self, state, action, next_state, reward):
        return self.environment.get_probability_of_next_state_and_reward_given_state_and_action(state, action, next_state, reward, self.self_player)

    def get_action_next_states(self, state):
        return self.environment.get_action_next_states(state)
    
    def get_outcome_probabilities(self, state, action):
        return self.environment.get_outcome_probabilities(state, action, self.self_player)