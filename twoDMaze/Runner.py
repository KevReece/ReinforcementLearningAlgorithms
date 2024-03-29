import random
from AbstractAgent import AbstractAgent
from AbstractEnvironment import AbstractEnvironment


class Runner:
    def __init__(self, agent: AbstractAgent, max_steps_per_episode=10000):
        self.agent = agent
        self.max_steps_per_episode = max_steps_per_episode

    def run(self, environment:AbstractEnvironment, n_episodes=10, verbose=False, learn=True):
        for episode_index in range(n_episodes):
            if verbose:
                print('Episode:', episode_index+1)
            environment.reset()
            for step_index in range(self.max_steps_per_episode):
                state = environment.get_agent_state()
                action_policy = self.agent.get_action_policy(state)
                action = random.choices(environment.get_all_actions(), action_policy)[0]
                reward, next_state = environment.act(action)
                if learn:
                    self.agent.post_act_learning(state, action, reward, next_state)
                if verbose:
                    print('Step:', step_index+1)
                    environment.print()
                if environment.is_done():
                    break
            if learn:
                self.agent.post_episode_learning()
