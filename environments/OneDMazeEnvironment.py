from environments.AbstractEnvironment import AbstractEnvironment


class OneDMazeEnvironment(AbstractEnvironment):
    class Actions:
        Left = 0
        Right = 1

    def __init__(self, initial_agent_position=0, n_states=5, exits=[4], initial_state_rewards={4: 10}):
        self._initial_agent_position = initial_agent_position
        self._n_states = n_states
        self._exits = exits
        self._initial_state_rewards = initial_state_rewards
        self.reset()

    def act(self, action: int):
        reward = 0
        new_position = self._agent_position
        if action == self.Actions.Left and self._agent_position > 0:
            new_position -= 1
        elif action == self.Actions.Right and self._agent_position < self._n_states - 1:
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
        self._agent_position = self._initial_agent_position
        self._state_rewards = self._initial_state_rewards.copy()

    def get_all_actions(self):
        return [self.Actions.Left, self.Actions.Right]
    
    def get_agent_state(self):
        return self._agent_position
    
    def get_initial_state_rewards(self):
        return self._initial_state_rewards
    
    def get_reward_values(self):
        return [0] + [reward for reward in self._initial_state_rewards.values()]
    
    def get_states_count(self):
        return self._n_states
    
    def get_actions_count(self):
        return len(self.get_all_actions())
    
    def get_exit_states(self):
        return self._exits
    
    def get_outcome_probabilities(self, state, action):
        next_state = self.get_action_next_states(state)[action]
        if next_state == None:
            return []
        reward = 0
        if next_state in self._initial_state_rewards:
            reward = self._initial_state_rewards[next_state]
        reward_index = self.get_reward_values().index(reward)
        return [(next_state, reward_index, 1)]

    def get_action_next_states(self, state):
        return [
            state-1 if state > 0 else None, 
            state+1 if state < self._n_states - 1 else None
        ]