import unittest

from model.simple_AI_player import SimpleAIPlayer
from model.player import Player
from model.classic_mode import ClassicMode
from model.game import Game

class TestSimpleAIPlayer(unittest.TestCase):
    """This class contains various tests for the Simple AI Player class of the reversi game
    """
    def test_init(self):
        """Since all the players in the game are inherited from the Player abstract class,
            the init method is tested only once for the Simple Ai Player
        """
        player1 = SimpleAIPlayer()
        player2 = SimpleAIPlayer()
        self.assertEqual(player1.id, 0)
        self.assertEqual(player2.id, 1)
        self.assertTrue(player1.can_move)
        self.assertTrue(player2.can_move)

    def test_make_turn(self):
        game = Game(size=4, player1=Player(), player2=Player(), game_mode=ClassicMode())
        game.player1 = SimpleAIPlayer()
        cell = game.player1.make_turn(game, game.game_mode)
        self.assertEqual(cell, (0, 2))
        self.assertNotEqual(cell, (0, 3))
        game.make_move(1, 2)
        game.make_move(2, 1)
        cell = game.player1.make_turn(game, game.game_mode)
        self.assertEqual(cell, [])
