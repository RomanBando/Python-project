from abc import abstractmethod

class Player:
    counter = 0

    def __init__(self) -> None:
        self.id = Player.counter
        self.can_move = True
        Player.counter += 1    
   
    @abstractmethod
    def make_turn(self):
        pass