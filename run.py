from random import randint

# Where computer places their bees randomly
PLAYER_BEE_HIVE = [[" "] * 8 for i in range(8)]
# Where players guesses are displayed
PLAYER_VISIBLE_HIVE = [[" "] * 8 for i in range(8)]
# Where computer guesses are displayed and where player inputs their bees
COMPUTER_VISIBLE_HIVE = [[" "] * 8 for i in range(8)]


def print_hive(hive):
    print("  0  1  2  3  4  5  6  7")
    print("  -----------------------")
    row_number = 0
    for row in hive:
        print(row_number, "| ".join(row))
        row_number += 1


def input_bee_location(hive):
    while True:
        try:
            bee_row = input("Enter the row of where you'd like to place a bee: ")
            if bee_row in '01234567':
                bee_row = int(bee_row)
                break
        except ValueError:
            print('Enter a valid number 0 - 7')
    while True:
        try:
            bee_column = input("Enter the column of where you'd like to place a bee: ")
            if bee_column in '01234567':
                bee_column = int(bee_column)
                break
        except ValueError:
            print('Try again')
    return bee_row, bee_column


def player_create_bees(hive):
    for bee in range(5):
        bee_row, bee_column = input_bee_location(hive)
        while hive[bee_row][bee_column] == '0':
            print('There is already a bee hiding there, choose another')
            bee_row, bee_column = input_bee_location(hive)
        hive[bee_row][bee_column] = '0'
    print('This is where your bees are hiding')
    print_hive(hive)


def start_game():
    print('Check start game')
    print_hive(PLAYER_VISIBLE_HIVE)
    player_create_bees(COMPUTER_VISIBLE_HIVE)


start_game()
