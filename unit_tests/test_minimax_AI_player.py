import unittest

from model.minimax_AI_player import MinimaxAIPlayer
from model.player import Player
from model.classic_mode import ClassicMode
from model.game import Game

class TestMinimaxAIPlayer(unittest.TestCase):
    """This class contains various tests for the Simple AI Player class of the reversi game.
        Since all the players in the game are inherited from the Player abstract class,
        the init method is tested only once for the Simple Ai Player
    """
    def test_make_turn(self):
        game = Game(size=8, player1=Player(), player2=Player(), game_mode=ClassicMode())
        game.player2 = MinimaxAIPlayer(5)
        game.curr_player = game.player1
        game.make_move(2, 4)
        game.make_move(3, 2)
        game.make_move(3, 3)
        game.make_move(3, 4)
        game.make_move(4, 2)
        game.make_move(4, 3)
        game.make_move(5, 3)
        game.curr_player = game.player2
        game.make_move(4, 4)
        game.make_move(4, 5)
        game.make_move(5, 2)
        game.make_move(6, 1)
        # the board now looks like this:
        #   1 2 3 4 5 6 7 8
        # 1 . . . . . . . .
        # 2 . . . . . . . .
        # 3 . . . . X . . .
        # 4 . . X X X . . .
        # 5 . . X X O O . .
        # 6 . . O X . . . .
        # 7 . O . . . . . .
        # 8 . . . . . . . .
        
        cell = game.player2.make_turn(game, game.game_mode)
        # and minimax suppose the best move is 7, 3 (6, 2)
        self.assertEqual(cell, (6, 2))