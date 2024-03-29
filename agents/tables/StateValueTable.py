class StateValueTable:
    def __init__(self, n_states):
        self.table = [0] * n_states

    def get_greedy_action_policy(self, action_to_next_state_dynamics, exit_dynamics):
        exit_actions = [action for action, next_state in enumerate(action_to_next_state_dynamics) if next_state in exit_dynamics]
        greedy_actions = exit_actions
        if not greedy_actions:
            actions_next_state_values = [
                self.table[next_state] if next_state is not None else float('-inf') 
                for next_state in action_to_next_state_dynamics
            ]
            max_next_state_value = max([next_state_value for next_state_value in actions_next_state_values])
            max_actions = [action for action, next_state_value in enumerate(actions_next_state_values) if next_state_value == max_next_state_value]
            greedy_actions = max_actions
        return [
            1/len(greedy_actions) if action in greedy_actions else 0 
            for action in range(len(action_to_next_state_dynamics))
        ]

    def print(self):
        print(self.table)