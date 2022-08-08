from view.game_view import GameView
from model.game import Game

class GameController:
    """This is the controller for the reversi game
    """
    def __init__(self, view: GameView, model: Game) -> None:
        self.view = view
        self.model = model

    def run_game(self):    
        """This method runs the reversi game
        """
        while True:
            self.view.draw_board()
            
            # every iteration we need to check if the players can move
            if not self.model.game_mode.can_move(self.model.board, self.model.curr_player):
                self.model.curr_player.can_move = False
                self.view.pass_turn()
                self.model.change_player()
                
                # if next player can't move too (from some previous iterations)
                if self.model.curr_player.can_move == False:
                    (player1_score, player2_score) = self.model.game_mode.check_score(self.model.player1, self.model.player2, self.model.board)
                    self.view.display_winner(player1_score, player2_score)
                    break
                continue    
            else: 
                self.model.curr_player.can_move = True
            
            row, col = self.view.make_turn()
            cells = self.model.game_mode.process_move(row, col, self.model.board, self.model.curr_player)
            a = map(lambda x: (x[0]+1, x[1]+1), cells )
            print(list(a))
            if len(cells) == 0:
                continue 

            for (x, y) in cells:
                self.model.make_move(x, y)
        
            self.model.change_player()

        # cells = []

        # while len(cells) == 0:
        #     try:   
        #         row, col = self.view.make_turn()
        #         cells = self.model.game_mode.process_move(row, col, self.model)
        #         # a = map(lambda x: (x[0]+1, x[1]+1), cells )
        #         # print(list(a))
        #         if len(cells) == 0:
        #             raise TypeError
        #     except TypeError:
        #         self.view.invalid_move()
        #         continue
        #     else:    
        #         for (x,y) in cells:
        #             self.model.make_move(x, y)
        #         self.model.change_player()