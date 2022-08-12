from typing import Optional 
from datetime import datetime

from view.game_view import GameView
from view.board_console_view import BoardConsoleView
from model.game import Game
from model.player import Player
from model.human_player import HumanPlayer


class GameConsoleView(GameView):
    """Game view of the reversi game for the console output
    """
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.board_view = BoardConsoleView(game.board)

    def draw_board(self):
        """This method draws the board
        """
        self.board_view.draw_board()
        scores = self.game.game_mode.check_score(self.game.player1, self.game.player2, self.game.board)
        print(f'Player 1 score: {scores[0]}, Player 2 score: {scores[1]}')
        print(f'Player {self.game.curr_player.id + 1} turn')

    def make_turn(self):
        """This method gets the turn from player
        """
        if isinstance(self.game.curr_player, HumanPlayer):
            while True:
                try:
                    s = input('Enter your move (row, col): ').split(',')
                    if len(s) != 2:
                        raise ValueError
                    row, col = int(s[0]) - 1 , int(s[1]) - 1
                    if not isinstance(row, int) or not isinstance(col, int):
                        raise ValueError
                    else:
                        return row, col
                except ValueError:
                    print('Row and col must be two integers, separated by comma')
        else:
            return self.game.curr_player.make_turn(self.game, self.game.game_mode) 

    def pass_turn(self):
        """This method prints corresponding message if the player can't move
        """
        if self.game.curr_player.can_move == False:
            print(f'Player {self.game.curr_player.id + 1} can\'t move')

    def invalid_move(self):
        """This method prints corresponding message if the player enters the 
            invalid move
        """
        print('Invalid move')
    
    def invalid_size(self):
        """This method prints corresponding message if the board size is incorrect
        """
        print('Invalid board size(must be in range 1-99)')

    def display_winner(self, player1_score, player2_score, file_path='reversi_scores.txt'):
        """This method prints which player won the game or if it was a draw and saves the final result
            in the file

        Args:
            player1_score,
            player2_score,
            file_path (str, optional): Defaults to 'reversi_scores.txt'.
        """
        today = datetime.today()
        new_format = today.strftime('%d-%m-%Y %H:%M')  
        s = ''
        winner = None

        if player1_score > player2_score:
            winner = self.game.player1
        elif player1_score < player2_score:
            winner = self.game.player2

        if winner:
            print(f'Player {winner.id + 1} wins')
            s += f'{new_format} '
            s += f'Player {winner.id + 1} won '
            s += f'Score Player1/Player2: '
            s += f'{player1_score}/{player2_score}\n'
            with open(file_path, 'a') as f:
                f.write(s)
        else:
            print('It\'s a draw')
            s += f'{new_format} Draw '
            s += f'Score Player1/Player2: '
            s += f'{player1_score}/{player2_score}\n'
            with open(file_path, 'a') as f:
                f.write(s)
