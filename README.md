A demonstration of fundamental reinforcement learning algorithms applied to different problems

Problem environments
---

- Simple 1D maze
- Simple 2D maze
- Noughts and Crosses

Agent algorithms
---

**Dynamic Programming** (PolicyIterationAgent, ValueIterationAgent): depends on the environment model. Doesn't scale well, even to Noughts and Crosses, but has very low bias and variance. ValueIterationAgent is more efficient.

**Temporal Difference Learning** (StateValueTemporalDifferenceZeroAgent, QLearningAgent, DoubleQLearningAgent, SarsaAgent, ExpectedSarsaAgent, TemporalDifferenceNStepsToExpectedSarsaAgent, MonteCarloAgent): Scales to medium problems, with some bias and variance. TemporalDifferenceNStepsToExpectedSarsaAgent performs best in keeping low bias, with good variance.

**Policy Gradient Learning** (ReinforceAgent, ActorCriticAgent): Scales to large problems, with high bias and variance. ActorCriticAgent is more efficient. To scale to large problems the algorithms should be extended with parameters decoupled from environment states.

**RandomAgent**: for training/testing of two-player environments.

**HumanAgent**: for interactive play in two-player environments.

### Further algorithms

- Tree search algorithms (e.g. Monte Carlo Tree Search)
- Eligibility traces (e.g. TD(lambda))
- Neural network algorithms (e.g. extend the policy gradient learning algorithms to train neural networks instead of Q tables)
- Continuous action and space algorithms

Note: a larger scale environment is needed to demonstrate the scaling of the algorithms (e.g. a more complex maze, or a more complex game).

Prerequisites
---

- install python 3.12
- install poetry
- set poetry python version: e.g. `poetry env use C:/Python312/python.exe`
- install poetry dependencies: `poetry install --no-root`

Run
---

Use the Python notebooks per problem environment, found in the root.