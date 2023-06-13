from ext_classes import Game


sign_1 = input("Enter player 1 sign: ")
sign_2 = input("Enter player 2 sign: ")

# The game grid size can be adjusted
grid_size = input('Please enter the grid size: ')

game = Game(sign_1, sign_2, grid_size=grid_size)
game.start_game()           #to start the game by turning game_on = True

game.mainloop()
