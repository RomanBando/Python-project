from abc import abstractmethod

class Player:
    counter = 0

    def __init__(self) -> None:
        self.id = Player.counter
        self.can_move = True
        Player.counter += 1    
   
    @abstractmethod
    def make_turn(self):
        """This method makes the move of the Player

        Args:
            game (Game),
            game_mode (GameMode)

        Returns:
            best_move: (row, col)
        """
        pass