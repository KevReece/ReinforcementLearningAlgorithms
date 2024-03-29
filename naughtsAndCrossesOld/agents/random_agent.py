import random
from agents.abstract_agent import AbstractAgent
from environment.board import Board
from environment.player_type import PlayerType


class RandomAgent(AbstractAgent):
    
    def __init__(self, name):
        self.name = name

    def get_move(self, board_plays, _):
        options = [
            (row, column) 
            for row in range(Board.ROWS) 
            for column in range(Board.COLUMNS) 
            if board_plays[row][column] == PlayerType.NO_PLAYER]
        return random.choice(options)
    
    def handle_reward(self, reward, board_plays, current_player):
        pass
    
    def __str__(self):
        return f"Random Agent {self.name}"