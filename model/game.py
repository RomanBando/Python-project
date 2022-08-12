from model.game_mode import GameMode
from model.player import Player
from model.board import Board

class Game:
    """This class defines the main logic of the reversi game
    """
    def __init__(self, size, player1: Player, player2: Player, game_mode: GameMode) -> None:  
        if size < 1 or size > 99:
            raise ValueError('Size must be in range 1-99')
        else:
            self.board = Board(size)
            self.player1 = player1
            self.player2 = player2
            self.curr_player = player1
            self.game_mode = game_mode

            
            center = size // 2
            self.board.update_move(center - 1, center - 1, player1)
            self.board.update_move(center, center, player1)
            self.board.update_move(center - 1, center, player2)
            self.board.update_move(center, center - 1, player2)      

    def get_next_player(self):
        """This method finds which player will move next
        """
        if self.curr_player == self.player1:
            return self.player2
        else:
            return self.player1  

    def change_player(self):
        """This method switches the players
        """
        self.curr_player = self.get_next_player()

    def make_move(self, row, col):
        """This method makes the player move

        Args:
            row,
            col
        """
        self.board.update_move(row, col, self.curr_player)