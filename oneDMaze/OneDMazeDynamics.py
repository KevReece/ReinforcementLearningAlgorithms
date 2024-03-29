from OneDMazeEnvironment import OneDMazeEnvironment


class OneDMazeDynamics:
    @staticmethod
    def build_environment_probabilities(environment: OneDMazeEnvironment):
        reward_dynamics = environment.get_initial_state_rewards()
        environment_probabilities = [
            [
                [
                    [
                        OneDMazeDynamics._get_environment_probability(state, action, next_state, reward, reward_dynamics)
                        for reward in environment.get_reward_values()
                    ]
                    for next_state in range(environment.get_states_count())
                ]
                for action in range(environment.get_actions_count())
            ]
            for state in range(environment.get_states_count())
        ]
        return environment_probabilities
    

    @staticmethod
    def _get_environment_probability(state, action, next_state, reward, reward_dynamics):
        if (action == 0 and next_state != state - 1):
            return 0
        if (action == 1 and next_state != state + 1):
            return 0
        if (reward == 0):
            return int(next_state not in reward_dynamics)
        return int(next_state in reward_dynamics and reward_dynamics[next_state] == reward)

    @staticmethod
    def get_action_to_next_state_dynamics(state: int):
        return [state-1, state+1]
    