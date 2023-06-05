import tkinter as tk
from tkinter import *


# create the board class to set up the board, score texts,
class GameBoard(Tk):
    def __init__(self, grid_size):
        super().__init__()
        self.title('tic_tac_toe')
        self.grid_size = int(grid_size)
        self.config(height=900, width=900, background='cyan')
        self.buttons = []
        self.button_signs = []
        self.sign = ""  # will be updated in the player class sign attribute
        self.canvas = Canvas(width=100*self.grid_size, height=60*self.grid_size)
        self.canvas.grid(column=self.grid_size, row=2)
        # the following 3 texts need to be updated in the game class
        self.player_1_score = self.canvas.create_text(50, 50*self.grid_size, text="", font=("Arial", 12), fill='green')
        self.player_2_score = self.canvas.create_text(250, 50*self.grid_size, text="", font=("Arial", 12), fill='blue')
        self.new_game = tk.Button(self.canvas, command=self.new_game, text='New Game')
        self.button_window = self.canvas.create_window(150, 50*self.grid_size, anchor="center", window=self.new_game)

        # create the buttons of the game
        for row in range(self.grid_size):
            button_rows = []
            for column in range(self.grid_size):
                button = Button(command=lambda r=row, c=column: self.button_press(r, c))
                self.button_window = self.canvas.create_window(column * 110, row * 40, anchor="nw", window=button)
                button_rows.append(button)
            self.buttons.append(button_rows)

    def button_press(self, r, c):
        if self.game_on:
            self.set_sign()
            self.buttons[r][c].config(text=self.sign)
            self.turn_count += 1
            self.toggle_turn()
            if self.turn_count >= self.grid_size * 2 - 1:
                self.get_button_signs()
                self.eval_positions()
            # print(f'row- {r}, column-{c}')

    # function to get the button signs which will be evaluated in the Game class
    def get_button_signs(self):
        for button in self.buttons:
            row_signs = [i.cget('text') for i in button]
            self.button_signs.append(row_signs)
        # print(f'current button sign is {self.button_signs}')
        return self.button_signs

    def new_game(self):
        # print('new game')
        for rows in self.buttons:
            for btn in rows:
                btn.config(text="")
        self.turn_count = 0
        self.game_on = True

