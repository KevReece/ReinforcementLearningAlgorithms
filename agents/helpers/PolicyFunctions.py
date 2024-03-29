class PolicyFunctions:
    @staticmethod
    def combine_policy_with_exploratory_policy(action_policy, exploration_rate):
        exploratory_action_policy_part = [exploration_rate/len(action_policy)] * len(action_policy)
        action_policy_part = [action_policy[action] * (1 - exploration_rate) for action in range(len(action_policy))]
        return [exploratory_action_policy_part[action] + action_policy_part[action] for action in range(len(action_policy))]

    @staticmethod
    def get_max_actions(state_action_value_function):
        max_q = max(state_action_value_function)
        max_actions = [action for action, q in enumerate(state_action_value_function) if q == max_q]
        return max_actions
    
    @staticmethod
    def single_action_as_action_probabilities(chosen_action, n_actions):
        return [
            1 if action == chosen_action else 0 
            for action in range(n_actions)
        ]