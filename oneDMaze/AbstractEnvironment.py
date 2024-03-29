class AbstractEnvironment:
    def __init__(self):
        pass

    def move(self, direction: int) -> tuple[int, int]:
        '''Move the agent in the specified direction and return the reward and the new position state.'''
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

    def get_agent_position(self) -> int:
        '''Returns the current position state of the agent.'''
        pass
    
    def get_initial_state_rewards(self) -> dict[int, int]:
        '''Returns the initial rewards of each state. The keys are the state positions and the values are the rewards.'''
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

    def get_exits(self) -> list[int]:
        '''Returns the exit position states.'''
        pass