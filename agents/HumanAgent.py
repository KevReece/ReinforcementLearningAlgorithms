import sys
from agents.AbstractAgent import AbstractAgent
from environments.AbstractEnvironment import AbstractEnvironment


class HumanAgent(AbstractAgent):
    def __init__(self, environment: AbstractEnvironment):
        self.actions_count = environment.get_actions_count()
        self.environment = environment

    def get_action_policy(self, _):
        print("Human agent's turn")
        self.environment.print()
        sys.stdout.flush()
        user_action = None
        while user_action not in range(self.actions_count):
            user_input = input(f"Enter action (1 to {self.actions_count}) or 'exit': ")
            if user_input == "exit":
                sys.exit(0)
            try:
                user_action = int(user_input) - 1
            except ValueError:
                user_action = None
        return [
            1 if action == user_action else 0 
            for action in range(self.actions_count)
        ]