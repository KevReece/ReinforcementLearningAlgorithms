from environments.AbstractEnvironment import AbstractEnvironment


class DynamicsFunctions:
    @staticmethod
    def build_environment_probabilities(environment: AbstractEnvironment):
        environment_probabilities = [
            [
                [
                    [
                        environment.get_probability_of_next_state_and_reward_given_state_and_action(state, action, next_state, reward)
                        for reward in environment.get_reward_values()
                    ]
                    for next_state in range(environment.get_states_count())
                ]
                for action in range(environment.get_actions_count())
            ]
            for state in range(environment.get_states_count())
        ]
        return environment_probabilities
    