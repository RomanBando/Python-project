from model.player import Player

class AIPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_turn(self):
        """This method makes the move of the AI Player

        Args:
            game (Game),
            game_mode (GameMode)

        Returns:
            best_move: (row, col)
        """
        pass
    