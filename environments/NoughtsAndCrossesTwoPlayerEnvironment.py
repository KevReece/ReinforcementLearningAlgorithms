import numpy as np
from environments.AbstractEnvironment import AbstractEnvironment


class NoughtsAndCrossesTwoPlayerEnvironment():
    class Actions:
        TopLeft = 0
        TopMiddle = 1
        TopRight = 2
        MiddleLeft = 3
        MiddleMiddle = 4
        MiddleRight = 5
        BottomLeft = 6
        BottomMiddle = 7
        BottomRight = 8

    class Rewards:
        Win = 10
        Draw = 1
        Lose = 0

    class Winner:
        Draw = 0
        X = 1
        O = 2

    class Player:
        X = 1
        O = 2

    class Board:
        Width = 3
        Height = 3

    COUNT_SQUARE_STATES = 3

    def __init__(self):
        self._first_turn_player = self.Player.X
        self._win_states = self._calculate_win_states()
        self.reset()

    def act(self, action: int):
        current_state = self._board_to_state(self._current_board)
        next_state = self.get_action_next_states(current_state)[action]
        if (next_state == None):
            return self._board_to_state(self._current_board)
        self._current_board = self._state_to_board(next_state)
        if not self.is_done():
            self._current_turn_player = self.Player.X if self._current_turn_player == self.Player.O else self.Player.O
        return self._board_to_state(self._current_board)

    def calculate_reward(self, player):
        return self._calculate_reward(self._current_board, player)

    def is_done(self):
        return self._board_to_state(self._current_board) in self._win_states
    
    def print(self):
        row_strings = []
        player_to_string_lookup = {self.Player.X: "X", self.Player.O: "O"}
        for y in range(self.Board.Height):
            row_state_string = " | ".join([
                player_to_string_lookup[self._current_board[x][y]] if self._current_board[x][y] != None else " "
                for x in range(self.Board.Width)
            ])
            row_strings.append(row_state_string)
        board_string = "\n---------\n".join(row_strings)
        print(board_string)

    def reset(self):
        self._current_board = [[None, None, None], [None, None, None], [None, None, None]]
        self._first_turn_player = self.Player.X if self._first_turn_player == self.Player.O else self.Player.X
        self._current_turn_player = self._first_turn_player

    def get_current_turn_player(self):
        return self._current_turn_player

    def get_all_actions(self):
        return [
            self.Actions.TopLeft,
            self.Actions.TopMiddle,
            self.Actions.TopRight,
            self.Actions.MiddleLeft,
            self.Actions.MiddleMiddle,
            self.Actions.MiddleRight,
            self.Actions.BottomLeft,
            self.Actions.BottomMiddle,
            self.Actions.BottomRight
        ]
    
    def get_state(self):
        return self._board_to_state(self._current_board)
    
    def get_initial_state_rewards(self, player):
        return {
            win_state: self._calculate_reward(self._state_to_board(win_state), player) 
            for win_state in self._win_states.keys()
        }
    
    def get_reward_values(self):
        return [self.Rewards.Lose, self.Rewards.Draw, self.Rewards.Win]
    
    def get_states_count(self):
        return self.COUNT_SQUARE_STATES ** (self.Board.Width * self.Board.Height)
    
    def get_actions_count(self):
        return len(self.get_all_actions())
    
    def get_exit_states(self):
        return [state for state in self._win_states]

    def get_action_next_states(self, state):
        board = self._state_to_board(state)
        player = self._current_turn_player
        return[
            self._board_to_state(self._get_action_next_board(board, action, player))
            for action in self.get_all_actions()
        ]
    
    def get_outcome_probabilities(self, state, action, player):
        next_state = self.get_action_next_states(state)[action]
        if next_state == None:
            return []
        reward = self._calculate_reward(self._state_to_board(next_state), player)
        reward_index = self.get_reward_values().index(reward)
        return [(next_state, reward_index, 1)]

    def _get_action_next_board(self, board, action, player):
        next_board = [column.copy() for column in board]
        action_position = self._action_to_position(action)
        if (next_board[action_position[0]][action_position[1]] != None):
            return None
        next_board[action_position[0]][action_position[1]] = player
        return next_board

    def _action_to_position(self, action):
        return (action % self.Board.Width, action // self.Board.Width)

    def _calculate_reward(self, board, player):
        state = self._board_to_state(board)
        if state not in self._win_states:
            return 0
        winner = self._win_states[state]
        if winner == self.Winner.Draw:
            return self.Rewards.Draw
        return self.Rewards.Win if winner == player else self.Rewards.Lose

    def _calculate_win_states(self):
        win_states = {}
        for state in range(self.get_states_count()):
            board = self._state_to_board(state)
            for i in range(self.Board.Width):
                player_at_intersection = board[i][i]
                if player_at_intersection == None:
                    continue
                is_matching_row = board[i][0] == board[i][1] == board[i][2]
                is_matching_column = board[0][i] == board[1][i] == board[2][i]
                if is_matching_row or is_matching_column:
                    win_states[state] = player_at_intersection
                    break
            if state in win_states:
                continue
            player_at_centre = board[1][1]
            if player_at_centre == None:
                continue
            is_matching_diagonal = board[0][0] == board[1][1] == board[2][2]
            is_matching_inverse_diagonal = board[0][2] == board[1][1] == board[2][0]
            if is_matching_diagonal or is_matching_inverse_diagonal:
                win_states[state] = player_at_centre
            is_board_full = all([x != None for row in board for x in row])
            if is_board_full:
                win_states[state] = self.Winner.Draw
        return win_states

    def _state_to_board(self, state):
        if state == None:
            return None
        board = [[None, None, None], [None, None, None], [None, None, None]]
        for y in range(self.Board.Height):
            for x in range(self.Board.Width):
                if state == 0:
                    break
                state, square_state = divmod(state, self.COUNT_SQUARE_STATES)
                if square_state != 0:
                    board[x][y] = square_state
        return board
    
    def _board_to_state(self, board):
        if board == None:
            return None
        square_states = [
            board[x][y] or 0 
            for x in range(self.Board.Width) 
            for y in range(self.Board.Height)
        ]
        square_states_string = "".join(reversed([str(square_state) for square_state in square_states]))
        return int(square_states_string, self.COUNT_SQUARE_STATES)