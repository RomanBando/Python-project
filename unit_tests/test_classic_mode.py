import unittest

from model.game import Game
from model.player import Player
from model.classic_mode import ClassicMode

class TestClassicMode(unittest.TestCase):
    """This class contains various tests for the Classic Mode of the reversi game
    """
    def test_process_move(self):
        game = Game(size=4, player1=Player(), player2=Player(), game_mode=ClassicMode())
        moves = game.game_mode.process_move(0, 2, game.board, game.player1)
        self.assertEqual(moves, [(1, 2), (0, 2)])

        game.curr_player = game.player1
        game.make_move(1, 2)
        game.change_player()
        game.make_move(0, 2)
        moves = game.game_mode.process_move(3, 2, game.board, game.player2)
        self.assertEqual(moves, [(2, 2), (1, 2), (3, 2)])

    def test_check_score(self):
        game = Game(size=4, player1=Player(), player2=Player(), game_mode=ClassicMode())
        scores = game.game_mode.check_score(game.player1, game.player2, game.board)
        self.assertEqual(scores[0], 2)
        self.assertEqual(scores[1], 2)

        game.curr_player = game.player1
        game.make_move(1, 2)
        scores = game.game_mode.check_score(game.player1, game.player2, game.board)
        self.assertEqual(scores[0], 3)
        self.assertEqual(scores[1], 1)

    def test_check_winner(self):
        game = Game(size=4, player1=Player(), player2=Player(), game_mode=ClassicMode())
        winner = game.game_mode.check_winner(game)
        self.assertEqual(winner, None)

        game.curr_player = game.player1
        game.make_move(1, 2)
        winner = game.game_mode.check_winner(game)
        self.assertEqual(winner, game.player1)

    def test_can_move(self):
        game = Game(size=3, player1=Player(), player2=Player(), game_mode=ClassicMode())
        self.assertTrue(game.game_mode.can_move(game.board, game.player1))
        self.assertTrue(game.game_mode.can_move(game.board, game.player2))
        game.curr_player = game.player1
        game.make_move(1, 0)
        game.make_move(1, 2)
        game.make_move(2, 0)
        game.make_move(2, 1)
        game.make_move(2, 2)

        # the board looks like this:
        # X O .
        # X X X
        # X X X
        # so the first player can move and the second can't move

        self.assertTrue(game.game_mode.can_move(game.board, game.player1))
        self.assertFalse(game.game_mode.can_move(game.board, game.player2))