from environment.player_type import PlayerType
from environment.round import Round
from game.game_outcome import GameOutcome
from game.game_printer import GamePrinter
from game.game_reward import GameReward


class GameRound:
    def __init__(self, agent_a, agent_b, agent_a_player=PlayerType.PLAYER_1):
        self._current_round = Round()
        self._agent_a = agent_a
        self._agent_b = agent_b
        self._agent_a_player = agent_a_player
        self._game_printer = GamePrinter()

    def play(self, is_verbose=True):
        while self._current_round.get_winner() == None:
            self._game_printer.print_agent_turn(self._get_current_agent(), self._current_round.current_player, is_verbose)
            x, y = self._get_current_agent().get_move(self._current_round.board_plays, self._current_round.current_player)
            self._current_round.make_move(x, y)
            self._game_printer.print_board(self._current_round, is_verbose)
            self._give_rewards()
        self._game_printer.print_agent_winner(self._get_winning_agent(), self._get_current_agent(), is_verbose) 
        return self._get_winning_agent()
    
    def _get_current_agent(self):
        return self._agent_a if self._current_round.current_player == self._agent_a_player else self._agent_b

    def _agent_b_player(self):
        return PlayerType.PLAYER_1 if self._agent_a_player == PlayerType.PLAYER_2 else PlayerType.PLAYER_2 

    def _get_winning_agent(self):
        if self._current_round.get_winner() == PlayerType.NO_PLAYER:
            return GameOutcome.DRAW
        return GameOutcome.AGENT_A_WIN if self._get_current_agent() == self._agent_a else GameOutcome.AGENT_B_WIN

    def _give_rewards(self):
        if self._current_round.get_winner() == None:
            # give rewards after the opponent has played
            self._get_current_agent().handle_reward(0, self._current_round.board_plays, self._current_round.current_player)
        self._agent_a.handle_reward(self._get_reward(self._agent_a), self._current_round.board_plays, self._agent_a_player)
        self._agent_b.handle_reward(self._get_reward(self._agent_b), self._current_round.board_plays, self._agent_b_player())

    def _get_reward(self, agent):
        if self._get_winning_agent() == GameOutcome.DRAW:
            return GameReward.DRAW_REWARD
        return GameReward.WIN_REWARD if agent == self._get_current_agent() else GameReward.LOSE_REWARD