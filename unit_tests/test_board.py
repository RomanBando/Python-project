import unittest

from model.board import Board
from model.player import Player

class TestBoard(unittest.TestCase):
    """This class contains various tests for the Board class of the reversi game
    """
    def test_init(self):
        board = Board(1)
        expected_board = [[None]]
        self.assertEqual(board.mat, expected_board)

        board = Board(2)
        expected_board = [[None, None], [None, None]]
        self.assertEqual(board.mat, expected_board)

    def test_get_move(self):
        board = Board(8)
        player = Player()
        board.mat[4][4] = player
        moved = board.get_move(4, 4)
        self.assertEqual(moved, player)
        self.assertNotEqual(moved, None)

    def test_update_move(self):
        board = Board(6)
        player = Player()
        board.update_move(3, 4, player)
        self.assertEqual(board.mat[3][4], player)
        self.assertNotEqual(board.mat[5][5], player)

    def test_copy(self):
        board = Board(5)
        new_board1 = board.copy()
        new_board2 = board.copy()
        self.assertNotEqual(board, new_board1)
        self.assertNotEqual(board, new_board2)
        self.assertNotEqual(new_board1, new_board2)