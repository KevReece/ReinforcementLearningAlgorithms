from agents.helpers.PolicyFunctions import PolicyFunctions


class BellmansEquations:
    @staticmethod
    def evaluate_and_improve_policy_iteration(n_states, n_actions, discount, environment_probabilities, environment_rewards, max_evaluate_iterations=100, max_improve_iterations=100, min_evaluation_delta=1e-4):
        policy = [0] * n_states
        for iteration_index in range(max_improve_iterations):
            state_value_function = BellmansEquations._evaluate_policy(n_states, policy, max_evaluate_iterations, discount, min_evaluation_delta, environment_probabilities, environment_rewards)
            policy, is_stable = BellmansEquations._improve_policy(n_states, n_actions, policy, state_value_function, discount, environment_probabilities, environment_rewards)
            if is_stable:
                print(f'Policy improvement stopped at iteration {iteration_index}'); 
                break
        return policy

    @staticmethod
    def _evaluate_policy(n_states, policy, max_iterations, discount, min_evaluation_delta, environment_probabilities, environment_rewards):
        state_value_function = [0] * n_states
        for iteration_index in range(max_iterations):
            max_delta = 0
            for state in range(n_states):
                prior_state_value_function = state_value_function[state]
                action = policy[state]
                state_value_function[state] += BellmansEquations._action_value_update(state, action, state_value_function, environment_probabilities, environment_rewards, discount)
                max_delta = max(max_delta, abs(prior_state_value_function-state_value_function[state]))
            if max_delta < min_evaluation_delta: 
                print(f'Policy evaluation stopped at iteration {iteration_index}'); 
                break
        return state_value_function
    
    @staticmethod
    def _improve_policy(n_states, n_actions, policy, state_value_function, discount, environment_probabilities, environment_rewards):
        action_value_function = [[0] * n_actions for _ in range(n_states)]
        is_stable = True
        for state in range(n_states):
            for action in range(n_actions):
                action_value_function[state][action] = BellmansEquations._action_value_update(state, action, state_value_function, environment_probabilities, environment_rewards, discount)
            new_max_actions = PolicyFunctions.get_max_actions(action_value_function[state])
            if policy[state] != new_max_actions[0]:
                is_stable = False
            policy[state] = new_max_actions[0]
        return policy, is_stable
    
    @staticmethod
    def policy_value_iteration(n_states, n_actions, discount, environment_probabilities, environment_rewards, max_iterations=100, min_evaluation_delta=1e-4):
        state_value_function = [0] * n_states
        policy = [0] * n_states
        for iteration_index in range(max_iterations):
            max_delta = 0
            for state in range(n_states):
                prior_state_value_function = state_value_function[state]
                action_value_function = [
                    BellmansEquations._action_value_update(state, action, state_value_function, environment_probabilities, environment_rewards, discount)
                    for action in range(n_actions)
                ]
                state_value_function[state] = max(action_value_function)
                max_delta = max(max_delta, abs(prior_state_value_function-state_value_function[state]))
                policy[state] = action_value_function.index(max(action_value_function))
            if max_delta < min_evaluation_delta: 
                print(f'Stopped at iteration {iteration_index}'); 
                break
        return policy
    
    @staticmethod
    def _action_value_update(state, action, state_value_function, environment_probabilities, environment_rewards, discount):
        return sum([
            (next_state_reward_probability * (environment_rewards[reward_index] + discount * state_value_function[next_state]))
            for next_state, next_state_reward_probabilities in enumerate(environment_probabilities[state][action])
            for reward_index, next_state_reward_probability in enumerate(next_state_reward_probabilities)
        ])