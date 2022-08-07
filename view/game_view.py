from abc import ABC, abstractmethod
from model.game import Game

class GameView(ABC):
    """The game view of the reversi game
    """
    def __init__(self, game: Game) -> None:
        self.game = game

    @abstractmethod
    def draw_board(self):
        """This method draws the board in the console
        """
        pass

    @abstractmethod
    def make_turn(self):
        """This method gets the turn from player
        """
        pass

    @abstractmethod
    def pass_turn(self):
        """This method prints corresponding message if the player can't move
        """
        pass

    @abstractmethod
    def invalid_move(self):
        """This method prints corresponding message if the player enters the 
            invalid move
        """
        pass
    
    @abstractmethod
    def display_winner(player):
        """This method informs which player won the game or if it was a draw
        """
        pass