from model.game import Game
from view.game_console_view import GameConsoleView
from model.human_player import HumanPlayer
from model.simple_AI_player import SimpleAIPlayer
from model.minimax_AI_player import MinimaxAIPlayer
from controller.game_controller import GameController
from model.classic_mode import ClassicMode

model = Game(size=2, player1=HumanPlayer(), player2=MinimaxAIPlayer(3), game_mode=ClassicMode())
view = GameConsoleView(model)
controller = GameController(view, model)
controller.run_game()