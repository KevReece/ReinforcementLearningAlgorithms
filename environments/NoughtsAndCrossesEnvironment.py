from environments.AbstractEnvironment import AbstractEnvironment


class NoughtsAndCrossesEnvironment(AbstractEnvironment):
    class Actions:
        TopLeft = 0
        TopMiddle = 1
        TopRight = 2
        MiddleLeft = 3
        MiddleMiddle = 4
        MiddleRight = 5
        BottomLeft = 6
        BottomMiddle = 7
        BottomRight = 8

    class Rewards:
        WIN = 10
        DRAW = 1
        LOSE = 0

    def act(self, action: int):
        reward = 0
        action_position = self._action_to_position(action)
        next_board = ...(action_position)
        reward = self._calculate_reward(next_board)
        return reward, self._board_to_state(next_board)

    def is_done(self):
        pass
    
    def print(self):
        pass

    def reset(self):
        # swap player
        pass

    def get_all_actions(self):
        return [
            self.Actions.TopLeft,
            self.Actions.TopMiddle,
            self.Actions.TopRight,
            self.Actions.MiddleLeft,
            self.Actions.MiddleMiddle,
            self.Actions.MiddleRight,
            self.Actions.BottomLeft,
            self.Actions.BottomMiddle,
            self.Actions.BottomRight
        ]
    
    def get_agent_state(self):
        pass
    
    def get_initial_state_rewards(self):
        pass
    
    def get_reward_values(self):
        return [self.Rewards.LOSE, self.Rewards.DRAW, self.Rewards.WIN]
    
    def get_states_count(self):
        pass
    
    def get_actions_count(self):
        return len(self.get_all_actions())
    
    def get_exit_states(self):
        pass
    
    def get_probability_of_next_state_and_reward_given_state_and_action(self, state, action, next_state, reward):
        if (self.get_action_next_states(state)[action] != next_state or next_state is None):
            return 0
        next_board = self._state_to_board(next_state)
        return reward == self._calculate_reward(next_board)

    def get_action_next_states(self, state):
        pass

    def _action_to_position(self, action):
        pass

    def _state_to_board(self, state):
        pass
    
    def _board_to_state(self, board):
        pass

    def _calculate_reward(self, board):
        pass