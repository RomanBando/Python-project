from model.AI_player import AIPlayer
from model.game_mode import GameMode
from model.game import Game

class SimpleAIPlayer(AIPlayer):
    def __init__(self) -> None:
        super().__init__()

    def make_turn(self, game: Game, game_mode: GameMode):
        best_move = []
        # we are looking for the longest series that process_move can return
        for i in range(game.board.size):
            for j in range(game.board.size):
                move = game_mode.process_move(i, j, game.board, game.curr_player)
                if len(move) > len(best_move):
                    best_move = move
        if len(best_move) > 0:
            return best_move[len(best_move) - 1]
        else:
            return best_move
