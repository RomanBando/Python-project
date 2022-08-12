from abc import ABC, abstractmethod

class GameMode(ABC):
    """This class provides the logic of the selected game mode for the reversi game
    """
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process_move(self):
        """This method validates the player's move and redraws the cells of the board 
            if the move is valid

        Args:
            row,
            col,
            board (Board),
            player (Player)

        Returns:
            list: a list of cells on the board to redraw if the move is valid
            or an empty list if it wasn't
        """
        pass

    @abstractmethod
    def check_score(self):
        """This method returns current score of each player

        Args:
            player1 (Player),
            player2 (Player),
            board (Board)

        Returns:
            player1_score, player2_score: tuple (scores of both players)
        """
        pass

    @abstractmethod
    def check_winner(self):
        """This method checks who won the game

        Args:
            game (Game)

        Returns:
            None: if this was a draw
            game.player1: if player1 won
            game.player2: if player2 won
        """
        pass

    @abstractmethod
    def can_move(self):
        """This method checks if the player can move

        Args:
            board (Board),
            player (Player)
        """
        pass