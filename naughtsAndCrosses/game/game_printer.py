from environment.board import Board
from environment.player_type import PlayerType
from game.game_outcome import GameOutcome


class GamePrinter():
    @staticmethod
    def print_board(round, is_verbose):
        if not is_verbose:
            return
        row_strings = []
        play_order_to_string = lambda order: str(order) if order > 0 else " "
        for row in range(Board.ROWS):
            row_state_string = " | ".join([GamePrinter._player_to_string_lookup()[round.board_plays[column][row]] for column in range(Board.COLUMNS)])
            row_play_order_string = " | ".join([play_order_to_string(round.board_play_order[column][row]) for column in range(Board.COLUMNS)])
            row_strings.append(f"{row_state_string}    {row_play_order_string}")
        grid_string = "\n---------    ---------\n".join(row_strings)
        print(grid_string)

    @staticmethod
    def print_agent_turn(current_agent, current_player, is_verbose):
        if not is_verbose:
            return
        print(f"{current_agent}'s turn as {GamePrinter._player_to_string_lookup()[current_player]}")

    @staticmethod
    def print_agent_winner(winning_agent, current_agent, is_verbose):
        if not is_verbose:
            return
        if winning_agent == GameOutcome.DRAW:
            print("It's a draw!")
        else:
            print(f"{current_agent} wins!")

    @staticmethod
    def print_series_outcomes(winning_agents):
        # TODO: overlaid line graph per outcome
        pass

    @staticmethod
    def _player_to_string_lookup():
        return {PlayerType.NO_PLAYER: " ", PlayerType.PLAYER_1: "X", PlayerType.PLAYER_2: "O"}
