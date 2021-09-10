## -- GAME SETUP -- ##
import random


# explains the basic game instructions to the user(s)
def game_instructions():
    print("\nGame Instructions: Player X will go first, followed by Player O.\nThe grid is numbered as seen below.")

    # prints the example game board, with numbers 1-9
    print_positions()

    print(
        "\nOn your turn, enter the number of an open box to place your mark.\nThe first player to get three marks in "
        "a row is the winner!")

    # included to break up the script for user-readability
    input("Press enter to continue...")
    print("-----------------------------------------------------------------------")


# creates the game board
def print_board(board_list):
    print('''
   {} | {} | {}
  -----------
   {} | {} | {}
  -----------
   {} | {} | {}
   '''.format(*board_list))


# inserts the numbers 1-9 within game board for user selection purposes
def print_positions():
    print_board(range(1, 10))


# allows the user to choose to either play with a friend or against the computer
def game_mode():
    # global variables
    global player1
    global player2

    while True:
        # user chooses game mode by typing in either the letter 'f' or 'c'
        version_choice = input("Would you like to play with a friend (f) or against the computer (c)?: ").lower()

        # if the user would like to play with a friend
        if version_choice == "f":
            print("\nYou have chosen to play with a friend! Let's randomly choose who will go first!")

            # user input name of first player
            player1 = str(input("\nPlayer 1: What is your first name?: "))
            # user input name of second player
            player2 = str(input("\nPlayer 2: What is your first name?: "))
            break

        # if the user would like to play against the computer
        elif version_choice == "c":
            print("\nYou have chosen to play against the computer! Let's randomly choose who will go first!")

            # user input their name
            player1 = str(input("\nWhat is your first name?: "))
            # second player is computer
            player2 = "Computer"
            break

        # exception handling - if the user did not choose either friend or computer
        else:
            print("\nPlease enter a valid choice:")
            continue


# randomly decide which player will go first
def first_turn():
    # global variables
    global turn
    global player1
    global player2
    global current_player

    # creates a list of who is playing based on user input
    player_list = [player1, player2]

    # randomly chooses one of the names from the list to see who goes first
    turn = random.choice(player_list)

    # prints out name and message detailing who is first to go
    print("\n{} will be Player X and will go first. Good luck!".format(turn))

    # included to break up the script for user-readability
    input("\nPress enter to START...")
    print("-----------------------------------------------------------------------")

    # reassign players to alternate turns properly - fist to go is player1
    if turn == player1:
        current_player = player1

    else:
        current_player = player2


# starts the game
def start_game():
    # global variables
    global letter
    global board
    global player1
    global player2
    global current_player
    global index
    global box_choice
    global game_status

    # player who goes first is assigned letter "X"
    letter = "X"

    # the board starts out completely empty with no markers placed yet
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # the game has been started
    game_status = "started"

    while game_status == "started":

        # the current board is printed so users can decide their next move
        print_board(board)

        # current player inputs the box number of their chosen move
        try:

            # if it is the computer's turn
            if current_player == "Computer":
                box_choice = random.randint(1, 9)

            # if it is a user's turn
            else:
                box_choice = int(input((
                    "\nPlayer {}: {}, it is your turn. What is the number of the box you would like to mark? ".format(
                        letter, current_player))))

            # if a valid box number is entered by user or computer
            if 0 < box_choice < 10:

                # chosen box number is converted to index position in board list
                index = box_choice - 1

                while True:
                    # if the box is a valid choice and has not been marked yet
                    if board[index] == " ":

                        # included to break up the script for user-readability
                        print("-------------------------------------------------------------------------------")
                        print("-------------------------------NEXT PLAYER'S TURN------------------------------")
                        print("-------------------------------------------------------------------------------")

                        # replaces chosen box with current player's assigned letter (X or O)
                        board[index] = letter

                        # check to see if there is a winner or draw
                        end_game()

                        # changes current player to next player's turn
                        if current_player == player1:
                            current_player = player2
                        else:
                            current_player = player1

                        # changes current marker to next player's letter
                        if letter == "X":
                            letter = "O"
                        else:
                            letter = "X"
                        break

                    # exception handling - if the user picked a box that has been marked already
                    else:
                        print("-------------------------------------------------------------------------------")
                        print(
                            "\nSorry Player {}: {}, this box has been marked already. Please enter a different choice.".format(
                                letter, current_player))
                        break

            # exception handling - if the user did not provide a number between 1 and 9
            else:
                print("-------------------------------------------------------------------------------")
                print("\nPlease try again by entering a valid number between 1-9: ")
                continue

        # exception handling - if the user did not provide a valid input
        except ValueError:
            print("-------------------------------------------------------------------------------")
            print("\nPlease enter a valid number.")
            continue

        # the game is over
        end_game()
        if game_status == "complete":
            break
        else:
            continue


# checks to see if winner or draw -- if so, ends the game
def end_game():
    # global variables
    global game_status

    while game_status == "started":

        # checks to see if Player X has 3 in a row (horizontal, vertical, diagonals)
        if board[0] == board[1] == board[2] == "X" or \
                board[3] == board[4] == board[5] == "X" or \
                board[6] == board[7] == board[8] == "X" or \
                board[0] == board[3] == board[6] == "X" or \
                board[1] == board[4] == board[7] == "X" or \
                board[2] == board[5] == board[8] == "X" or \
                board[0] == board[4] == board[8] == "X" or \
                board[6] == board[4] == board[2] == "X":

            # prints the winning message and game board for user
            print("Congratulations! Player X: {} is the winner!".format(current_player))
            print_board(board)

            # changes game_status to complete
            game_status = "complete"

            # asks the user to play again
            play_again()
            break

        # checks to see if Player O has 3 in a row (horizontal, vertical, diagonals)
        elif board[0] == board[1] == board[2] == "O" or \
                board[3] == board[4] == board[5] == "O" or \
                board[6] == board[7] == board[8] == "O" or \
                board[0] == board[3] == board[6] == "O" or \
                board[1] == board[4] == board[7] == "O" or \
                board[2] == board[5] == board[8] == "O" or \
                board[0] == board[4] == board[8] == "O" or \
                board[6] == board[4] == board[2] == "O":

            # prints the winning message and game board for user
            print("Congratulations! Player O: {} is the winner!".format(current_player))
            print_board(board)

            # changes game_status to complete
            game_status = "complete"

            # asks the user to play again
            play_again()
            break

        # checks to see if all boxes have been filled
        elif board[0] != " " and \
                board[1] != " " and \
                board[2] != " " and \
                board[3] != " " and \
                board[4] != " " and \
                board[5] != " " and \
                board[6] != " " and \
                board[7] != " " and \
                board[8] != " ":

            # ends the game and declares there is a draw
            print("Congratulations! It is a tie!")
            print_board(board)

            # changes game_status to complete
            game_status = "complete"

            # asks the user to play again
            play_again()
            break

        # continues the game
        else:
            break


# asks the user if they want to play again
def play_again():

    while True:
        try:
            # user chooses to play again or not by typing in either the letter 'y' or 'n'
            answer = input("\nWould you like to play again? Enter (y) for yes or (n) for no: ").lower()

            while answer == "y" or answer == "n":
                # if the user wants to play again - program starts over
                if answer == "y":
                    print("\nGreat! Let's play again!")
                    print("-------------------------------------------------------------------------------")
                    execute()
                    break

                # if the user does not want to play again - program ends
                else:
                    print("\nThanks for playing!")
                    quit()
            


        # exception handling - if the user did not choose either yes or no
        except ValueError:
            print("\nPlease enter either 'y' or 'n'.")
            continue


## -- GAME EXECUTION --##

def execute():
    while True:
        # welcome message
        print("Welcome to Tic Tac Toe!")
        game_instructions()

        # game setup
        mode_choice = ""
        player1 = ""
        player2 = ""
        turn = ""
        game_mode()
        first_turn()

        # start game
        letter = ""
        boxes = ""
        start_game()

execute()
