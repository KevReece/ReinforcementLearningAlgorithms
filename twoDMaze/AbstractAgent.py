class AbstractAgent:
    def get_action_policy(self, state) -> list[float]:
        '''Returns a list of weights for each action'''
        pass

    def post_act_learning(self, state, action, reward, next_state) -> None:
        '''Update the agent based on the action context'''
        pass

    def post_episode_learning(self) -> None:
        '''Update the agent based on the episode context'''
        pass

    def print(self) -> None:
        pass
