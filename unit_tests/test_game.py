import unittest

from model.game import Game
from model.game_mode import GameMode
from model.player import Player

class TestGame(unittest.TestCase):
    """This class contains various tests for the Game class of the reversi game
    """
    def test_init(self):
        game = Game(size=4, player1=Player(), player2=Player(), game_mode=GameMode)
        expected_board = [[None, None, None, None], [None, game.player1, game.player2, None],
                            [None, game.player2, game.player1, None], [None, None, None, None]]
        self.assertEqual(game.board.mat, expected_board)
        with self.assertRaises(ValueError):
            game = Game(size=0, player1=Player(), player2=Player(), game_mode=GameMode)

    def test_change_player(self):
        game = Game(size=8, player1=Player(), player2=Player(), game_mode=GameMode)
        game.curr_player = game.player2
        game.change_player()
        self.assertEqual(game.curr_player, game.player1)
        self.assertNotEqual(game.curr_player, game.player2)
        game.change_player()
        self.assertEqual(game.curr_player, game.player2)
        self.assertNotEqual(game.curr_player, game.player1)

    def test_make_move(self):
        game = Game(size=6, player1=Player(), player2=Player(), game_mode=GameMode)
        self.assertEqual(game.board.mat[0][1], None)
        game.curr_player = game.player2
        game.make_move(0, 1)
        self.assertEqual(game.board.mat[0][1], game.player2)
        self.assertNotEqual(game.board.mat[0][1], game.player1)