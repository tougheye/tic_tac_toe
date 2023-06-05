from gameboard import GameBoard
import numpy as np


class Player:
    def __init__(self, sign):
        self.sign = sign
        self.turn = False
        self.score = 0

    def turn_on(self):
        self.turn = True
        self.game.game_board.sign = self.sign

    def button_press(self, r, c):
        self.buttons[r][c].config(text=self.sign)
        print(f'row- {r}, column-{c}')


# Create the game class to update scores, manage rules and turns
class Game(GameBoard):
    def __init__(self, player_1, player_2, grid_size ):
        super().__init__(int(grid_size))
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn_count = 0
        self.score_1 = 0
        self.score_2 = 0
        self.pos_matrix = None
        self.game_on = False


    def set_sign(self):
        if self.player_1.turn:
            self.sign = self.player_1.sign
            # print(self.sign)

        elif self.player_2.turn:
            self.sign = self.player_2.sign
            # print(self.sign)

        else:
            self.player_1.turn = True
            self.sign = self.player_1.sign
            # print(self.sign)

    def toggle_turn(self):
        print(self.turn_count)
        if self.player_1.turn:
            self.player_1.turn = False
            self.player_2.turn = True

        elif self.player_2.turn:
            self.player_2.turn = False
            self.player_1.turn = True

    def player_1_wins(self):
        result_1 = False
        # check the 2 diagonals first
        if np.all(np.diag(self.pos_matrix[-self.grid_size:]) == self.player_1.sign):
            self.score_1 += 1
            result_1 = True
        elif np.all(np.diag(np.fliplr(self.pos_matrix[-self.grid_size:])) == self.player_1.sign):
            self.score_1 += 1
            result_1 = True
        # check the 2 columns
        for i in range(self.grid_size):
            if np.all(self.pos_matrix[-self.grid_size:][:, i] == self.player_1.sign) or \
                    np.all(self.pos_matrix[-self.grid_size:][i, :] == self.player_1.sign):
                self.score_1 += 1
                result_1 = True
                break
        return result_1

    def player_2_wins(self):
        result_2 = False
        # check the 2 diagonals first
        if np.all(np.diag(self.pos_matrix[-self.grid_size:]) == self.player_2.sign):
            self.score_2 += 1
            result_2 = True
        elif np.all(np.diag(np.fliplr(self.pos_matrix[-self.grid_size:])) == self.player_2.sign):
            self.score_2 += 1
            result_2 = True
        # check the 2 columns
        for i in range(self.grid_size):
            if np.all(self.pos_matrix[-self.grid_size:][:, i] == self.player_2.sign) or \
                    np.all(self.pos_matrix[-self.grid_size:][i, :] == self.player_2.sign):
                self.score_2 += 1
                result_2 = True
                break
        return result_2

    # function to evaluate if either player won
    def eval_positions(self):
        # player_1 =
        # player_2 = str(self.score_2)
        self.pos_matrix = np.matrix(self.button_signs)
        # print(f'current pos_matrix is \n{self.pos_matrix[-3:]}\n'
        #       f'current flip pos matrix is \n{np.fliplr(self.pos_matrix[-3:])}')          #test print
        if self.player_1_wins():
            print(f'{self.player_1.sign} won!!!')   # need to update the screen to pop up the message
            self.game_on = False
            self.canvas.itemconfig(self.player_1_score, text=f'{self.player_1.sign}: {self.score_1}')
        elif self.player_2_wins():
            print(f'{self.player_2.sign} won!!!')
            self.game_on = False
            self.canvas.itemconfig(self.player_2_score, text=f'{self.player_2.sign}: {self.score_2}')
        else:
            print('keep playing')


    def start_game(self):
        self.canvas.itemconfig(self.player_1_score, text=f'{self.player_1.sign} : {self.score_1}')
        self.canvas.itemconfig(self.player_2_score, text=f'{self.player_2.sign} : {self.score_2}')
        self.game_on = True


