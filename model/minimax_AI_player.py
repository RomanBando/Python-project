from copy import copy
import math

from model.AI_player import AIPlayer
from model.board import Board
from model.game_mode import GameMode
from model.game import Game
from model.player import Player

class MinimaxAIPlayer(AIPlayer):
    """This class represents a minimax algorithm for AI player
    """
    def __init__(self, max_depth=3) -> None:
        super().__init__()
        self.max_depth = max_depth

    def find_moves(self, board: Board, game_mode: GameMode, player: Player):
        """This method finds all possible moves for the player

        Args:
            board (Board)
            game_mode (GameMode)
            player (Player)

        Returns:
            possible_moves: a list of all possible moves
        """
        possible_moves = []
        
        for i in range(board.size):
            for j in range(board.size):
                move = game_mode.process_move(i, j, board, player)

                if len(move) > 0:
                    possible_moves.append((i, j))
        
        return possible_moves
        
    def make_turn(self, game: Game, game_mode: GameMode):
        """This method selects the best move the Minimax Ai Player can do

        Args:
            game (Game)
            game_mode (GameMode)

        Returns:
            best_move: (row, col)
        """
        # possible_moves = self.find_moves(game.board, game_mode, game.curr_player)
        max_value = -math.inf
        best_move = None
        curr_player, opponent = game.curr_player, game.get_next_player()

        # for move in possible_moves:
        #     (row, col) = move
        #     new_board = copy(game.board)
        #     new_board.update_move(row, col, curr_player)
        #     print(new_board.mat)
        #     print((row, col), '*')


        for i in range(game.board.size):
            for j in range(game.board.size):
                cells = game_mode.process_move(i, j, game.board, curr_player)

                if len(cells) > 0:
                    new_board = copy(game.board)
                    for (row, col) in cells:
                        new_board.update_move(row, col, curr_player)
                    board_value = self.minimax(0, new_board, curr_player, opponent, game_mode)

                    if board_value > max_value:
                        best_move = (i, j)
        
        return best_move


    def minimax(self, depth, board: Board, max_player: Player, min_player: Player, game_mode: GameMode):
        """Minimax algorithm for the AI player

        Args:
            depth
            board (Board)
            max_player
            min_player
            game_mode (GameMode)

        Returns:
            max/min(values): the value for the move
        """
        # condition for the terminal state
        print(depth, max_player.id)
        if depth == self.max_depth:
            (max_player_score, min_player_score) = game_mode.check_score(max_player, min_player, board)
            if max_player_score > min_player_score:
                return 1
            elif max_player_score < min_player_score:
                return -1
            else:
                return 0
        
        values = []
        moves = self.find_moves(board, game_mode, max_player)
        print(moves)

        # for (row, col) in moves:
        #     new_board = copy(board)
        #     new_board.update_move(row, col, max_player)
        #     board_value = self.minimax(depth + 1, new_board, min_player, max_player, game_mode)
        #     values.append(board_value)
 
        for i in range(board.size):
            for j in range(board.size):
                cells = game_mode.process_move(i, j, board, max_player)

                if len(cells) > 0:
                    new_board = copy(board)
                    for (row, col) in cells:
                        new_board.update_move(row, col, max_player)
                    board_value = self.minimax(depth + 1, new_board, min_player, max_player, game_mode)
                    values.append(board_value)

        if max_player == self:
            return max(values)
        else:
            return min(values)