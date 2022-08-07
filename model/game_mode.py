from abc import ABC, abstractmethod

class GameMode(ABC):
    """This class provides the logic of the selected game mode for the reversi game
    """
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process_move(self):
        pass

    @abstractmethod
    def check_score(self):
        pass

    @abstractmethod
    def check_winner(self):
        pass