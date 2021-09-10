import utilities
import random

while True:
    #Welcome message
    print("Welcome to Tic Tac Toe!")
    utilities.game_instructions()


    #Game setup
    mode_choice = ""
    player1 = ""
    player2 = ""
    turn = ""
    utilities.game_mode()
    utilities.first_turn()

    #Start game
    letter = ""
    boxes = ""
    utilities.start_game()



