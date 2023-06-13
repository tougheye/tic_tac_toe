from gameboard import GameBoard


# creating the player class that will be initiated in main.py and input in Game class
# this class will have the player attributes of score, sign, and turn
# Create the game class to update scores, manage turns, and evaluate the positions
# this class has an inheritance from GameBoard class.

class Game(GameBoard):
    def __init__(self, sign_1, sign_2, grid_size):
        super().__init__(int(grid_size))
        self.player_1_sign = sign_1
        self.player_2_sign = sign_2
        self.player_1_turn = False
        self.player_2_turn = False
        self.turn_count = 0
        self.score_1 = 0
        self.score_2 = 0
        self.pos_matrix = None
        self.game_on = False
        self.winning_sign = ""

    # function to set the sign of the game. It is called in the
    # button_press function in GameBoard class
    def set_sign(self):
        if self.player_1_turn:
            self.sign = self.player_1_sign
        elif self.player_2_turn:
            self.sign = self.player_2_sign
        else:
            self.player_1_turn = True
            self.sign = self.player_1_sign

    # the toggle_turn function changes the turn between player 1 and 2. it is called
    # in the button_press class
    def toggle_turn(self):
        if self.player_1_turn:
            self.player_1_turn = False
            self.player_2_turn = True

        elif self.player_2_turn:
            self.player_2_turn = False
            self.player_1_turn = True

    # Function to check if player 1 wins which switches the result_1 variable to True
    def player_wins(self):
        got_result = False
        current_rows = self.button_signs[-self.grid_size:]
        curr_main_diag = []
        current_columns = list(map(list, zip(*current_rows)))
        curr_other_diag = []

        # check rows first and append the diagonals
        for row in current_rows:
            curr_main_diag.append(row[current_rows.index(row)])
            if all(x == row[0] for x in row):
                self.winning_sign = row[0]
                got_result = True

        # check the main diagonal
        if all(x == curr_main_diag[0] for x in curr_main_diag):
            self.winning_sign = curr_main_diag[0]
            got_result = True

        # check columns first and append the other diagonals
        for col in current_columns:
            curr_other_diag.append(col[current_columns.index(col)])
            if all(x == col[0] for x in col):
                self.winning_sign = col[0]
                got_result = True

        # check the other diagonal
        if all(x == curr_other_diag[0] for x in curr_other_diag):
            self.winning_sign = curr_other_diag[0]
            got_result = True
        return got_result

    # Function to check if player 2 wins which switches the result_2 variable to True
    # function to evaluate if either player won by using player_1_wins and player_2_wins functions
    # if neither player wins, in the else statement it simply updates that the game tied
    def eval_positions(self):
        if self.player_wins():
            self.game_on = False
            if self.winning_sign == self.player_1_sign:
                self.score_1 += 1
                self.canvas.itemconfig(self.player_1_score,
                                       text=f'{self.player_1_sign}: {self.score_1}')
                self.canvas.itemconfig(self.player_won, text=f'{self.player_1_sign} won!!!',
                                       font=("Arial", 48), fill='green')  # update the screen to pop up the winner
            elif self.winning_sign == self.player_2_sign:
                self.score_2 += 1
                self.canvas.itemconfig(self.player_2_score,
                                       text=f'{self.player_2_sign}: {self.score_2}')
                self.canvas.itemconfig(self.player_won, text=f'{self.player_2_sign} won!!!', font=("Arial", 48),
                                       fill='blue')  # update the screen to pop up the winner
        # to check if the game tied
        elif not self.player_wins() and self.turn_count == self.grid_size * self.grid_size:
            self.game_on = False
            self.canvas.itemconfig(self.player_won, text='Game Tied :(', font=("Arial", 48),
                                   fill='grey')

    # the following function is called in the main.py.
    # it updates the player scores on the GameBoard canvass, and sets the game_on True
    def start_game(self):
        self.canvas.itemconfig(self.player_1_score, text=f'{self.player_1_sign} : {self.score_1}')
        self.canvas.itemconfig(self.player_2_score, text=f'{self.player_2_sign} : {self.score_2}')
        self.game_on = True
