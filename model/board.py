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
        return self.mat[row][col]

    def update_move(self, row, col, player: Player):
        self.mat[row][col] = player