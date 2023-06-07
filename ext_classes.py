from gameboard import GameBoard
import numpy as np          # to use the matrix properties to evaluate the GameBoard positions

# creating the player class that will be initiated in main.py and input in Game class
# this class will have the player attributes of score, sign, and turn
class Player:
    def __init__(self, sign):
        self.sign = sign
        self.turn = False
        self.score = 0


# Create the game class to update scores, manage turns, and evaluate the positions
# this class has an inheritance from GameBoard class.
class Game(GameBoard):
    def __init__(self, player_1, player_2, grid_size):
        super().__init__(int(grid_size))
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn_count = 0
        self.score_1 = 0
        self.score_2 = 0
        self.pos_matrix = None
        self.game_on = False

    # function to set the sign of the game. It is called in the
    # button_press function in GameBoard class
    def set_sign(self):
        if self.player_1.turn:
            self.sign = self.player_1.sign
        elif self.player_2.turn:
            self.sign = self.player_2.sign
        else:
            self.player_1.turn = True
            self.sign = self.player_1.sign

    # the toggle_turn function changes the turn between player 1 and 2. it is called
    # in the button_press class
    def toggle_turn(self):
        print(self.turn_count)
        if self.player_1.turn:
            self.player_1.turn = False
            self.player_2.turn = True

        elif self.player_2.turn:
            self.player_2.turn = False
            self.player_1.turn = True

    # Function to check if player 1 wins which switches the result_1 variable to True
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

    # Function to check if player 2 wins which switches the result_2 variable to True
    def player_2_wins(self):
        result_2 = False
        # check the 2 diagonals first
        if np.all(np.diag(self.pos_matrix[-self.grid_size:]) == self.player_2.sign): # take the most recent version of position matrix
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

    # function to evaluate if either player won by using player_1_wins and player_2_wins functions
    # if neither player wins, in the else statement it simply updates that the game tied
    def eval_positions(self):
        self.pos_matrix = np.matrix(self.button_signs)
        if self.player_1_wins():
            print()
            self.game_on = False
            self.canvas.itemconfig(self.player_1_score,
                                   text=f'{self.player_1.sign}: {self.score_1}')
            self.canvas.itemconfig(self.player_won, text=f'{self.player_1.sign} won!!!', font=("Arial", 48),
                                   fill='green')  # update the screen to pop up the winner
        elif self.player_2_wins():
            print(f'{self.player_2.sign} won!!!')
            self.game_on = False
            self.canvas.itemconfig(self.player_2_score,
                                   text=f'{self.player_2.sign}: {self.score_2}')
            self.canvas.itemconfig(self.player_won, text=f'{self.player_2.sign} won!!!', font=("Arial", 48),
                                   fill='blue')  # update the screen to pop up the winner
        else:
            if not np.equal(self.pos_matrix[-self.grid_size:], '').any():
                self.canvas.itemconfig(self.player_won, text='Game Tied :(', font=("Arial", 48),
                                       fill='grey')

    # the following function is called in the main.py.
    # it updates the player scores on the GameBoard canvass, and sets the game_on True
    def start_game(self):
        self.canvas.itemconfig(self.player_1_score, text=f'{self.player_1.sign} : {self.score_1}')
        self.canvas.itemconfig(self.player_2_score, text=f'{self.player_2.sign} : {self.score_2}')
        self.game_on = True
