import sys
from agents.TemporalDifferenceNStepsToExpectedSarsaAgent import TemporalDifferenceNStepsToExpectedSarsaAgent
from environments.AbstractEnvironment import AbstractEnvironment


class MonteCarloAgent(TemporalDifferenceNStepsToExpectedSarsaAgent):
    def __init__(self, environment: AbstractEnvironment, learning_rate=0.1, discount_factor=0.999, exploration_rate=0.2):
        super().__init__(environment, learning_rate, discount_factor, exploration_rate, n_steps=sys.maxsize)