from random import randint

import pyfiglet

import colorama
from colorama import Fore, Back

SIZE = 8
NUM_BEES = 10
TURNS = 5

# Where computer places their bees randomly
PLAYER_BEE_HIVE = [[" "] * 8 for i in range(SIZE)]
# Where players guesses are displayed
PLAYER_VISIBLE_HIVE = [[" "] * 8 for i in range(SIZE)]


def print_intro():
    title_art = pyfiglet.figlet_format('FREE THE BEES', font="bubble")
    print(Fore.YELLOW + (title_art) + Fore.RESET)
    input("Press enter to start the game...\n")
    print("In a dystopian time, bees are hungry and can't escape their hive")
    print('You have stumbled across a beehive and want to help')
    print('Try to give the bees nectar without destroying their home')
    print(f'The hive is {SIZE} squares long and high')
    print(f'There are {NUM_BEES} bees to find in each hive')
    print('Feed as many bees as you can so they can survive!')
    print(f'You only have {TURNS} drops of nectar to give them')
    print('Feed the bees by guessing a coordinate you think they are at')
    print('When prompted, input a number for x-axis (horizontal rows) first')
    print('Then a number for the y-axis (vertical columns)')


def get_player_name():
    while True:
        player = input("Please tell us your name so the bees can say "
                       "thanks!\n")
        if len(player) >= 2 and not player.isnumeric():
            print(f'Thanks for helping the bees, {player}!')
            break
        elif len(player) <= 2:
            print(f"The bees are friends, {player}, tell them your full name")
        else:
            print("That name is not valid, please enter a name with letters,"
                  " or characters, bees don't like strangers!")


def print_hive(hive):
    """
    Displays the hive
    """
    print("  1  2  3  4  5  6  7  8")
    print(Fore.YELLOW + "  -----------------------" + Fore.RESET)
    row_number = 1
    for row in hive:
        print(row_number, Fore.YELLOW + "| ".join(row) + Fore.RESET)
        row_number += 1


def computer_create_bees(hive):
    """
    Loop for computer to generate random coordinates for bees to find
    """
    for bee in range(NUM_BEES):
        bee_row, bee_column = randint(0, 7), randint(0, 7)
        hive[bee_row][bee_column] = "X"
        print(bee_row, bee_column)


def guess_bee_location(hive):
    turn = 0
    if turn in range(TURNS):
        while True:
            try:
                guess_row = int(input('Guess which row a bee is hiding '
                                      'on:\n')) - 1
                if guess_row in range(0, 8):
                    break
                elif guess_row not in range(0, 8):
                    print("That is outside the hive. Pick a number from 1-8")
            except ValueError:
                print("That's not an appropriate choice, please select a "
                      "valid row by picking a number from 1-8, then enter")

        while True:
            try:
                guess_column = int(input('Guess which column a bee is hiding '
                                         'on:\n')) - 1
                if guess_column in range(0, 8):
                    break
                elif guess_column not in range(0, 8):
                    print("That is outside the hive. Pick a number from 1-8")
            except ValueError:
                print("That's not an appropriate choice, please select a "
                      "valid column by picking a number from 1-8, then enter")
        return guess_row, guess_column


def start_game():
    success = 0
    computer_create_bees(PLAYER_BEE_HIVE)

    print_intro()

    get_player_name()

    for turn in range(0, TURNS, 1):
        while True:
            print('Guess a bee location on the hive below...')
            print_hive(PLAYER_VISIBLE_HIVE)
            guess_row, guess_column = guess_bee_location(PLAYER_BEE_HIVE)
            if PLAYER_VISIBLE_HIVE[guess_row][guess_column] == "-":
                print(Fore.YELLOW + "You guessed that one already, have "
                      "another try." + Fore.RESET)
            elif PLAYER_VISIBLE_HIVE[guess_row][guess_column] == "0":
                print(Fore.YELLOW + "You guessed that one already, have "
                      "another try." + Fore.RESET)
            elif PLAYER_BEE_HIVE[guess_row][guess_column] == "X":
                print(Fore.GREEN + "SUCCESS! You fed a bee!" + Fore.RESET)
                PLAYER_VISIBLE_HIVE[guess_row][guess_column] = "0"
                success += 1
                break
            else:
                print(Fore.RED + "MISS! The bees are still hungry" +
                      Fore.RESET)
                PLAYER_VISIBLE_HIVE[guess_row][guess_column] = "-"
                break
            turn += 1
    print_hive(PLAYER_VISIBLE_HIVE)
    if success != 0:
        print(f'Well done for feeding {success} bees!')
    else:
        print('Bad luck, maybe you can feed more the bees next time.')


start_game()
