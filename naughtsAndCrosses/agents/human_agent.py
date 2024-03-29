from agents.abstract_agent import AbstractAgent
from environment.player_type import PlayerType


class HumanAgent(AbstractAgent):
    def __init__(self, name):
        self.name = name

    def get_move(self, board_plays, _):
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        while board_plays[x][y] != PlayerType.NO_PLAYER:
            print("Invalid move, please try again")
            x = int(input("Enter the X position [0,1,2]: "))
            y = int(input("Enter the Y position [0,1,2], and 0 is at the top: "))
        return x, y
    
    def handle_reward(self, reward, board_plays, current_player):
        pass

    def __str__(self):
        return f"Human {self.name}"