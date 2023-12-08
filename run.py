from random import randint

SIZE = 8
NUM_BEES = 5

# Where computer places their bees randomly
PLAYER_BEE_HIVE = [[" "] * 8 for i in range(SIZE)]
# Where players guesses are displayed
PLAYER_VISIBLE_HIVE = [[" "] * 8 for i in range(SIZE)]
# Where computer guesses are displayed and where player inputs their bees
COMPUTER_VISIBLE_HIVE = [[" "] * 8 for i in range(SIZE)]


def print_hive(hive):
    """
    Displays the hive
    """
    print("  0  1  2  3  4  5  6  7")
    print("  -----------------------")
    row_number = 0
    for row in hive:
        print(row_number, "| ".join(row))
        row_number += 1


def input_bee_location(hive):
    """
    Ask for input of row and column
    """
    while True:
        try:
            bee_row = input("Enter the row of where you'd like to place a "
                            "bee: ")
            if bee_row in '01234567':
                bee_row = int(bee_row)
                break
        except ValueError:
            print('Enter a valid number 0 - 7')
    while True:
        try:
            bee_column = input("Enter the column of where you'd like to place "
                               "a bee: ")
            if bee_column in '01234567':
                bee_column = int(bee_column)
                break
        except ValueError:
            print('Try again')
    return bee_row, bee_column


def player_create_bees(hive):
    """
    Loop to make bees for human player to place in computer hive
    """
    for bee in range(NUM_BEES):
        bee_row, bee_column = input_bee_location(hive)
        while hive[bee_row][bee_column] == '0':
            print('There is already a bee hiding there, choose another')
            bee_row, bee_column = input_bee_location(hive)
        hive[bee_row][bee_column] = '0'
    print('This is where your bees are hiding')
    print_hive(hive)


def computer_create_bees(hive):
    """
    Loop for computer to generate random coordinates for bees to find
    """
    for bee in range(NUM_BEES):
        bee_row, bee_column = randint(0, 7), randint(0, 7)
        while hive[bee_row][bee_column] == "X":
            bee_row, bee_column = input_bee_location()
        hive[bee_row][bee_column] = "X"


def guess_bee_location(hive):
    for turn in range(5):
        while True:
            try:
                guess_row = int(input('Guess which row a bee is hiding on:'))
                if guess_row in range(0, 7):
                    break
            except ValueError:
                print('Guess not valid, try again')
        while True:
            try:
                guess_column = int(input('Guess which column a bee is hiding '
                                         'on:'))
                if guess_column in range(0, 7):
                    break
            except ValueError:
                print('Guess not valid, try again')
        return guess_row, guess_column


def start_game():
    computer_create_bees(PLAYER_BEE_HIVE)
    print_hive(PLAYER_VISIBLE_HIVE)
    player_create_bees(COMPUTER_VISIBLE_HIVE)
    while True:
        """
        Player's turn
        """
        while True:
            print('Guess a bee location')
            print_hive(PLAYER_VISIBLE_HIVE)
            guess_row, guess_column = guess_bee_location(PLAYER_BEE_HIVE)
            if PLAYER_VISIBLE_HIVE[guess_row][guess_column] == "-":
                print("You guessed that one already.")
            elif PLAYER_BEE_HIVE[guess_row][guess_column] == "X":
                print("Hit")
                PLAYER_VISIBLE_HIVE[guess_row][guess_column] = "X"
                break
            else:
                print("MISS!")
                PLAYER_VISIBLE_HIVE[guess_row][guess_column] = "-"
                break


start_game()
