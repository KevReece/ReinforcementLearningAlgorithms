from environment.player_type import PlayerType
from game.game_round import GameRound
from game.game_printer import GamePrinter 


class GameSeries:
    def __init__(self, rounds_count, agent_a, agent_b):
        self.rounds_count = rounds_count
        self.agent_a = agent_a
        self.agent_b = agent_b
        self.agent_a_player = PlayerType.PLAYER_1
        self.game_printer = GamePrinter()
        
    def play(self):
        winning_agents = []
        for _ in range(self.rounds_count):
            game_round = GameRound(self.agent_a, self.agent_b, self.agent_a_player)
            winning_agent = game_round.play(is_verbose=False)
            winning_agents.append(winning_agent)
            self.agent_a_player = PlayerType.PLAYER_2 if self.agent_a_player == PlayerType.PLAYER_1 else PlayerType.PLAYER_1
        self.game_printer.print_series_outcomes(winning_agents)
        return winning_agents
