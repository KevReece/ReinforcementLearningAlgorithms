from environments.AbstractEnvironment import AbstractEnvironment


class TwoDMazeEnvironment(AbstractEnvironment):
    class Actions:
        Up = 0
        Right = 1
        Down = 2
        Left = 3

    def __init__(self, position_shape=(5,5), initial_agent_position=(0,0), exit_positions=[(4,4)], initial_position_rewards={(4,4): 10}):
        self._position_shape = position_shape
        self._initial_agent_position = initial_agent_position
        self._exit_positions = exit_positions
        self._initial_position_rewards = initial_position_rewards
        self.reset()

    def act(self, action: int):
        reward = 0
        new_position = self._agent_position
        last_bottom_y = self._position_shape[1] - 1
        last_right_x = self._position_shape[0] - 1
        if action == self.Actions.Up and self._agent_position[1] > 0:
            new_position = (self._agent_position[0], self._agent_position[1] - 1)
        elif action == self.Actions.Right and self._agent_position[0] < last_right_x:
            new_position = (self._agent_position[0] + 1, self._agent_position[1])
        elif action == self.Actions.Down and self._agent_position[1] < last_bottom_y:
            new_position = (self._agent_position[0], self._agent_position[1] + 1)
        elif action == self.Actions.Left and self._agent_position[0] > 0:
            new_position = (self._agent_position[0] - 1, self._agent_position[1])
        if (not self._is_position_valid(new_position)):
            raise Exception('Invalid new position')
        if new_position in self._position_rewards:
            reward += self._position_rewards[new_position]
            self._position_rewards.pop(new_position)
        self._agent_position = new_position
        return reward, self._position_to_state(self._agent_position)

    def is_done(self):
        return self._agent_position in self._exit_positions
    
    def print(self):
        output = [[' '] * self._position_shape[0] for _ in range(self._position_shape[1])]
        for position in self._position_rewards:
            output[position[0]][position[1]] = 'R'
        for position in self._exit_positions:
            output[position[0]][position[1]] = 'E'
        output[self._agent_position[0]][self._agent_position[1]] = 'A'
        for row in output:
            print('[' + '|'.join(row) + ']')

    def reset(self):
        self._agent_position = self._initial_agent_position
        self._position_rewards = self._initial_position_rewards.copy()

    def get_all_actions(self):
        return [self.Actions.Up, self.Actions.Right, self.Actions.Down, self.Actions.Left]
    
    def get_agent_state(self):
        agent_state = self._position_to_state(self._agent_position)
        if agent_state is None:
            raise Exception('Invalid agent position')
        return agent_state
    
    def get_initial_state_rewards(self):
        initial_state_rewards = {
            self._position_to_state(position): reward 
            for position, reward in self._initial_position_rewards.items()
        }
        if None in initial_state_rewards:
            raise Exception('Invalid initial position rewards')
        return initial_state_rewards
    
    def get_reward_values(self):
        return [0] + [reward for reward in self._initial_position_rewards.values()]
    
    def get_states_count(self):
        return self._position_shape[0] * self._position_shape[1]
    
    def get_actions_count(self):
        return len(self.get_all_actions())
    
    def get_exit_states(self):
        exit_states = [
            self._position_to_state(exit_position) 
            for exit_position in self._exit_positions
        ]
        if None in exit_states:
            raise Exception('Invalid exit positions')
        return exit_states
    
    def get_outcome_probabilities(self, state, action):
        next_state = self.get_action_next_states(state)[action]
        if next_state == None:
            return []
        next_position = self._state_to_position(next_state)
        reward = 0
        if next_position in self._initial_position_rewards:
            reward = self._initial_position_rewards[next_position]
        reward_index = self.get_reward_values().index(reward)
        return [(next_state, reward_index, 1)]

    def get_action_next_states(self, state):
        position = self._state_to_position(state)
        return [
            self._position_to_state((position[0], position[1] - 1)),
            self._position_to_state((position[0] + 1, position[1])),
            self._position_to_state((position[0], position[1] + 1)),
            self._position_to_state((position[0] - 1, position[1])),
        ]
    
    def _is_position_valid(self, position):
        return (
            position[0] >= 0 
            and position[0] < self._position_shape[0] 
            and position[1] >= 0 
            and position[1] < self._position_shape[1]
        )
    
    def _position_to_state(self, position):
        if not self._is_position_valid(position):
            return None
        return position[0] + position[1] * self._position_shape[0]

    def _state_to_position(self, state):
        return (state % self._position_shape[0], state // self._position_shape[0])
