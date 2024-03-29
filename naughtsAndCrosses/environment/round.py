import numpy as np
from environment.board import Board
from environment.player_type import PlayerType


class Round:
    def __init__(self):
        self.board_plays = np.zeros((Board.ROWS, Board.COLUMNS), dtype=int)
        self.board_play_order = np.zeros((Board.ROWS, Board.COLUMNS), dtype=int)
        self.current_player = PlayerType.PLAYER_1
        self.current_turn = 1

    def make_move(self, x, y):
        if self.board_plays[x][y] == PlayerType.NO_PLAYER:
            self.board_plays[x][y] = self.current_player
            self.board_play_order[x][y] = self.current_turn
            if self.get_winner() == None:
                self.current_player = PlayerType.PLAYER_1 if self.current_player == PlayerType.PLAYER_2 else PlayerType.PLAYER_2
                self.current_turn += 1
            return True
        else:
            return False

    def get_winner(self):
        for i in range(Board.ROWS):
            player_at_intersection = self.board_plays[i][i]
            if player_at_intersection == PlayerType.NO_PLAYER:
                continue
            is_matching_row = self.board_plays[i][0] == self.board_plays[i][1] == self.board_plays[i][2]
            is_matching_column = self.board_plays[0][i] == self.board_plays[1][i] == self.board_plays[2][i]
            if is_matching_row or is_matching_column:
                return player_at_intersection
        player_at_centre = self.board_plays[1][1]
        if player_at_centre == PlayerType.NO_PLAYER:
            return None
        is_matching_diagonal = self.board_plays[0][0] == self.board_plays[1][1] == self.board_plays[2][2]
        is_matching_inverse_diagonal = self.board_plays[0][2] == self.board_plays[1][1] == self.board_plays[2][0]
        if is_matching_diagonal or is_matching_inverse_diagonal:
            return player_at_centre
        is_board_full = all([x != 0 for row in self.board_plays for x in row])
        return PlayerType.NO_PLAYER if is_board_full else None
