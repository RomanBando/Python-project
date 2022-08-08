from model.player import Player
from typing import Optional

class Board:
    """This class represents the boardstate of the reversi board
    """
    EMPTY_CELL = None

    def __init__(self, size) -> None:
        self.size = size

        # Allocate the board with empty squares
        self.mat = [[self.EMPTY_CELL] * size for _ in range(size)]
        

    def get_move(self, row, col) -> Optional[Player]:
        """This method gets the move from the player
            and returns the state of the indicated board cell  

        Args:
            row
            col 
        """
        return self.mat[row][col]

    def update_move(self, row, col, player: Player):
        """This method updates the cell on the board

        Args:
            row
            col
            player (Player)
        """
        self.mat[row][col] = player

    def copy(self):
        """This method copies the board
        """
        new_board = Board(self.size)
        
        for i in range(self.size):
            for j in range(self.size):
                new_board.update_move(i, j, self.mat[i][j])

        return new_board