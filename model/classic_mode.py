from model.game import Game
from model.board import Board
from model.player import Player
from model.game_mode import GameMode


class ClassicMode(GameMode):
    """This class provides the logic for the classic game mode of the reversi game
    """
    def __init__(self) -> None:
        pass

    def process_move(self, row, col, board: Board, player: Player):
        """This method validates the player's move and redraws the cells of the board 
            if the move is valid

        Args:
            row,
            col,
            board (Board),
            player (Player)

        Returns:
            list: a list of cells on the board to redraw if the move is valid
            or an empty list if it wasn't
        """
        if board.size <= row or board.size <= col:
            return []
            
        if board.get_move(row, col) != Board.EMPTY_CELL:
            return []

        result = []
        # checking the box around input
        for i in range(-1,2,1):
            if row + i == -1 or  row + i == board.size:
                continue

            for j in range(-1,2,1):
                if col + j == -1 or  col + j == board.size:
                    continue

                if i != 0 or j != 0:
                    cells = []
                    k = 1

                    while True:
                        x = row + i * k
                        y = col + j * k
                        if x < 0 or y < 0 or x >= board.size or y >= board.size:
                            break
                        cell = board.get_move(x, y)
                        # we found empty cell
                        if cell == None:
                            break
                        # we found enemy cell
                        elif cell != player:
                            cells.append((x, y))
                        # next piece is our piece
                        elif k == 1:
                            break
                        # otherwise we found a line of 3 or more pieces
                        else:
                            result.extend(cells)
                            break
                        k += 1
  
        if len(result) > 0:
            result.append((row, col))                
        return result

    def check_score(self, player1, player2, board: Board):
        """This method returns current score of each player

        Args:
            player1 (Player),
            player2 (Player),
            board (Board)

        Returns:
            player1_score, player2_score: tuple (scores of both players)
        """
        player1_score = 0
        player2_score = 0

        for i in range(board.size):
            for j in range(board.size):
                cell = board.get_move(i, j)

                if cell == player1:
                    player1_score += 1
                elif cell == player2:
                    player2_score += 1

        return player1_score, player2_score 

    def check_winner(self, game: Game):
        """This method checks who won the game

        Args:
            game (Game)

        Returns:
            None: if this was a draw
            game.player1: if player1 won
            game.player2: if player2 won
        """
        scores = self.check_score(game.player1, game.player2, game.board)
                
        if scores[0] == scores[1]:
            return None
        elif scores[0] > scores[1]:
            return game.player1
        else:
            return game.player2

    def can_move(self, board: Board, player: Player):
        """This method checks if the player can move

        Args:
            board (Board)
            player (Player)
        """
        for i in range(board.size):
            for j in range(board.size):
                if len(self.process_move(i, j, board, player)) > 0:
                    return True

        return False