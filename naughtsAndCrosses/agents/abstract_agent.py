class AbstractAgent:
    def get_move(self, board_plays, current_player):
        raise NotImplementedError("This method should be implemented by the agent subclass")
    
    def handle_reward(self, reward, board_plays, current_player):
        raise NotImplementedError("This method should be implemented by the agent subclass")

    def __str__(self):
        raise NotImplementedError("This method should be implemented by the agent subclass")
    