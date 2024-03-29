class AbstractAgent:
    def get_action_policy(self, state):
        pass

    def post_act_learning(self, state, action, reward, next_state):
        pass

    def post_episode_learning(self):
        pass

    def print(self):
        pass
