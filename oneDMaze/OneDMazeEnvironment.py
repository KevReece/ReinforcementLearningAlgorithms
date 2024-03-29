from AbstractEnvironment import AbstractEnvironment


class OneDMazeEnvironment(AbstractEnvironment):
    class Actions:
        Left = 0
        Right = 1

    def __init__(self):
        self._agent_position = 0
        self._n_states = 5
        self._exits = [4]
        self._reward_values = [0, 10]
        self._initial_state_rewards = {4: 10}
        self._state_rewards = self._initial_state_rewards.copy()

    def move(self, direction: int):
        reward = 0
        new_position = self._agent_position
        if direction == self.Actions.Left and self._agent_position > 0:
            new_position -= 1
        elif direction == self.Actions.Right and self._agent_position < self._n_states - 1:
            new_position += 1
        if new_position in self._state_rewards:
            reward += self._state_rewards[new_position]
            self._state_rewards.pop(new_position)
        self._agent_position = new_position
        return reward, self._agent_position

    def is_done(self):
        return self._agent_position in self._exits
    
    def print(self):
        output = [' '] * self._n_states
        for position in self._state_rewards:
            output[position] = 'R'
        for position in self._exits:
            output[position] = 'E'
        output[self._agent_position] = 'A'
        print('[' + '|'.join(output) + ']')

    def reset(self):
        self._agent_position = 0
        self._state_rewards = self._initial_state_rewards.copy()

    def get_all_actions(self):
        return [self.Actions.Left, self.Actions.Right]
    
    def get_agent_position(self):
        return self._agent_position
    
    def get_initial_state_rewards(self):
        return self._initial_state_rewards
    
    def get_reward_values(self):
        return self._reward_values
    
    def get_states_count(self):
        return self._n_states
    
    def get_actions_count(self):
        return len(self.get_all_actions())
    
    def get_exits(self):
        return self._exits