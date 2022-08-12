import unittest

from view.board_console_view import BoardConsoleView
from model.board import Board

class TestBoardConsoleView(unittest.TestCase):
    """This class contains test for the Board Console View class of the reversi game
        and doesn't include ui tests
    """
    def test_init(self):
        board = BoardConsoleView(Board(2))
        expected_board = Board(2)
        self.assertEqual(board, expected_board)