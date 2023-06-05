from ext_classes import Player, Game


player_1 = Player('X')
player_2 = Player('O')

grid_size = input('Please enter the grid size: ')

game = Game(player_1, player_2, grid_size=grid_size)
game.start_game()




game.mainloop()
