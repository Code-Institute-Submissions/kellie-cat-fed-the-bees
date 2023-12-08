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


def start_game():
    print('Check start game')
    print_hive(PLAYER_VISIBLE_HIVE)


start_game()
