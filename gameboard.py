import tkinter as tk
from tkinter import *


# create the board class to set up the board, score texts, toggle turns,
class GameBoard(Tk):
    def __init__(self, grid_size):
        super().__init__()
        self.title('tic_tac_toe')
        self.grid_size = int(grid_size)
        self.config(height=900, width=900, background='cyan')
        self.buttons = []
        self.button_signs = []  # the list will be updated by get_button_signs function
        self.sign = ""  # will be updated in the player class sign attribute
        self.canvas = Canvas(width=80 + 100 * self.grid_size, height=100 + 60 * self.grid_size)
        self.canvas.grid(column=self.grid_size, row=3)
        # the following 3 texts need to be updated in the game class
        # the player scores texts to be updated based on the game result
        self.player_1_score = self.canvas.create_text(
            50, 50 * self.grid_size, text="",
            font=("Arial", 18), fill='green')
        self.player_2_score = self.canvas.create_text(
            250, 50 * self.grid_size, text="",
            font=("Arial", 18), fill='blue')
        # New game button to reset the board
        self.new_game = tk.Button(
            self.canvas, command=self.new_game, text='New Game')
        # placing the new_game button on canvas
        self.button_window = self.canvas.create_window(
            150, 50 * self.grid_size, anchor="center",
            window=self.new_game)
        # Declare the winner once a game is over
        self.player_won = self.canvas.create_text(
            200, 70 * self.grid_size, anchor='center', text="WHO WILL BE THE WINNER?",
            font=("Arial", 24), fill='red')

        # create the buttons for the grid
        for row in range(self.grid_size):
            button_rows = []
            for column in range(self.grid_size):
                # buttons will activate the button_press function
                button = Button(command=lambda r=row, c=column: self.button_press(r, c))
                self.button_window = self.canvas.create_window(
                    column * 110, row * 40, anchor="nw", window=button)
                button_rows.append(button)
            self.buttons.append(button_rows)

    # the button press function will update the sign every time a box is clicked
    # it also tracks the number of turns after each click.
    # based on the grid size, it will evaluate the board's position by calling eval_positions function
    def button_press(self, r, c):
        if self.game_on:
            self.set_sign()
            self.buttons[r][c].config(text=self.sign)
            self.turn_count += 1
            self.toggle_turn()
            if self.turn_count >= self.grid_size * 2 - 1:
                self.get_button_signs()
                self.eval_positions()

    # function to get the button signs which will be evaluated in the Game class
    def get_button_signs(self):
        for button in self.buttons:
            row_signs = [i.cget('text') for i in button]
            self.button_signs.append(row_signs)
        return self.button_signs

    def new_game(self):
        for rows in self.buttons:
            for btn in rows:
                btn.config(text="")
        self.turn_count = 0
        self.game_on = True
