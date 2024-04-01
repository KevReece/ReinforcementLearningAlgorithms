class AbstractEnvironment:
    def __init__(self):
        pass

    def act(self, action: int) -> tuple[int, int]:
        '''Apply the agent using specified action index, then return the reward and the new state.'''
        pass

    def is_done(self) -> bool:
        '''Returns if the agent is in an exit position state.'''
        pass
    
    def print(self) -> None:
        pass

    def reset(self) -> None:
        pass

    def get_all_actions(self) -> list[int]:
        '''Returns a list of all possible actions.'''
        pass

    def get_agent_state(self) -> int:
        '''Returns the current state of the agent.'''
        pass
    
    def get_initial_state_rewards(self) -> dict[int, int]:
        '''Returns the initial rewards of each state. The keys are the states and the values are the rewards.'''
        pass
    
    def get_reward_values(self) -> list[int]:
        '''Returns the possible reward values.'''
        pass

    def get_states_count(self) -> int:
        '''Returns the number of states.'''
        pass

    def get_actions_count(self) -> int:
        '''Returns the number of actions.'''
        pass

    def get_exit_states(self) -> list[int]:
        '''Returns the exit states.'''
        pass

    def get_outcome_probabilities(self, state: int, action: int) -> list[tuple[int, int, float]]:
        '''Returns the probabilities of transitioning from state using action to next_state and reward.'''
        pass

    def get_action_next_states(self, state: int) -> list[int]:
        '''Returns the next states given all possible action from a state.'''
        pass