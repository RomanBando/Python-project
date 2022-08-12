from view.board_view import BoardView
from model.board import Board

class BoardConsoleView(BoardView):
    """The board of the reversi game for the console output
    """
    symbols = {0: 'X', 1: 'O'}
    
    def __init__(self, board: Board) -> None:
        super().__init__(board)

    def print_cell(self, cell) :
        """This method prints the cells on the board

        Args:
            cell
        """
        if self.board.size > 9 and len(str(cell)) < 2:
            print(f' {cell}  ', end='')
        else: 
            print(f' {cell} ', end='')

    def draw_board(self):
        """This method draws the board
        """
        board_size = self.board.size
        self.print_cell(' ')

        for i in range(board_size):
            self.print_cell(i + 1)
        print()

        for i in range(board_size):
            self.print_cell(i + 1)

            for j in range(board_size):
                cell = self.board.get_move(i, j)

                if cell == None:
                    self.print_cell('.')
                else:
                    self.print_cell(self.symbols[cell.id])
            print()

    def __eq__(self, other) -> bool:
        return self.board.mat == other.mat