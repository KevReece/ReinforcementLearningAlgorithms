class QTable:
    def __init__(self, n_states, n_actions):
        self.table = [[0] * n_actions for _ in range(n_states)]

    def get_greedy_action_policy(self, state):
        action_values = self.table[state]
        max_q_actions = [
            action 
            for action, q in enumerate(action_values) 
            if q == max(action_values)
        ]
        return [
            1/len(max_q_actions) if action in max_q_actions else 0 
            for action in range(len(action_values))
        ]
    
    def print(self):
        for state, actions in enumerate(self.table):
            print('State', state, '->', actions)