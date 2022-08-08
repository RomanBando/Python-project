from abc import ABC, abstractmethod
from model.board import Board

class BoardView(ABC):
    """The board of the reversi game
    """
    def __init__(self, board: Board) -> None:
        self.board = board

    @abstractmethod
    def draw_board(self):
        """This method draws the board
        """
        pass