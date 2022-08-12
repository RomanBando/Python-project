from model.player import Player

class HumanPlayer(Player):
    """This class represents human player and doesn't have the
        make_turn() method since this player makes turns by himself
    """
    def __init__(self) -> None:
        super().__init__()        