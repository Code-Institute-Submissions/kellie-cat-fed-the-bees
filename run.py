from random import randint

SIZE = 8
NUM_BEES = 10

# Where computer places their bees randomly
PLAYER_BEE_HIVE = [[" "] * 8 for i in range(SIZE)]
# Where players guesses are displayed
PLAYER_VISIBLE_HIVE = [[" "] * 8 for i in range(SIZE)]


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


def computer_create_bees(hive):
    """
    Loop for computer to generate random coordinates for bees to find
    """
    for bee in range(NUM_BEES):
        bee_row, bee_column = randint(0, 7), randint(0, 7)
        hive[bee_row][bee_column] = "0"
        print(bee_row, bee_column)


def guess_bee_location(hive):
    guess_list = []
    for turn in range(5):
        while True:
            try:
                guess_row = int(input('Guess which row a bee is hiding '
                                      'on:\n'))
                if guess_row in range(0, 8):
                    break
            except ValueError:
                print('Guess not valid, try again')
        while True:
            try:
                guess_column = int(input('Guess which column a bee is hiding '
                                         'on:\n'))
                if guess_column in range(0, 8):
                    break
            except ValueError:
                print('Guess not valid, try again')
        return guess_row, guess_column
        guess_coordinates = guess_row, guess_column
        if guess_coordinates in guess_list:
            print("You already tried there, try again")
            turn -= 1
        guess_list.append(guess_coordinates)


def start_game():
    computer_create_bees(PLAYER_BEE_HIVE)
    print_hive(PLAYER_VISIBLE_HIVE)
    print('Introduction')
    print('Instructions')
    for turn in range(0, 5, 1):
        while True:
            print('Guess a bee location')
            print_hive(PLAYER_VISIBLE_HIVE)
            guess_row, guess_column = guess_bee_location(PLAYER_BEE_HIVE)
            if PLAYER_VISIBLE_HIVE[guess_row][guess_column] == "-":
                print("You guessed that one already, have another try.")
            elif PLAYER_BEE_HIVE[guess_row][guess_column] == "0":
                print("You fed the bee!")
                PLAYER_VISIBLE_HIVE[guess_row][guess_column] = "0"
                break
            else:
                print("MISS! The bees are still hungry")
                PLAYER_VISIBLE_HIVE[guess_row][guess_column] = "-"
                break
            turn += 1
    print_hive(PLAYER_VISIBLE_HIVE)
    print('Show results')


start_game()
