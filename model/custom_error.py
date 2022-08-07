class CustomError(Exception):
    """Base class for exceptions of reversi game"""
    pass

class InputTurnError(ValueError):
    """Exception for invalid input of row/col"""
    def __init__(self, message='Row and col must be two integers, separated by comma') -> None:
        super().__init__(message)

class InvalidMove(CustomError):
    """Exception for invalid input of row/col"""
    def __init__(self, message='Invalid move') -> None:
        super().__init__(message)
