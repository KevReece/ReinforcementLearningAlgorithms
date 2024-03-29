import math


class SoftmaxFunctions:
    @staticmethod
    def actions_softmax(state_q, temperature):
        action_exponentials = [math.exp(q / temperature) for q in state_q]
        exponentials_sum = sum(action_exponentials)
        return [action_exponential / exponentials_sum for action_exponential in action_exponentials]

    @staticmethod
    def action_softmax(state_q, action, temperature):
        softmaxed_actions = SoftmaxFunctions.actions_softmax(state_q, temperature)
        return softmaxed_actions[action]