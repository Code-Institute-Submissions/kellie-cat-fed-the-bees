import unicodedata

from random import randint

import os
import sys

import pyfiglet

import colorama
from colorama import Fore

SIZE = 8
NUM_BEES = 10
TURNS = 5

# Where computer places their bees randomly
PLAYER_BEE_HIVE = [[" "] * 8 for i in range(SIZE)]
# Where players guesses are displayed
PLAYER_VISIBLE_HIVE = [[" "] * 8 for i in range(SIZE)]


def print_intro():
    """
    Displays title_art and game instructions
    """
    title_art = pyfiglet.figlet_format('FREE THE BEES', font="bubble")
    print(Fore.YELLOW + 'Welcome to...\n')
    print((title_art) + Fore.RESET)
    input("Press enter to read the game instructions...\n")
    print("In a dystopian time, bees are hungry and can't escape their hive")
    print('You have stumbled across a beehive and want to help')
    print('Try to give the bees nectar without destroying their home')
    print(f'The hive is {SIZE} squares long and high')
    print(f'There are {NUM_BEES} bees to find in each hive')
    print('Feed as many bees as you can so they can survive!')
    print(f'You only have {TURNS} drops of nectar to give them')
    print('Feed the bees by guessing a coordinate you think they are at')
    print('When prompted, input a number for x-axis (horizontal rows) first')
    print('Then a number for the y-axis (vertical columns)\n')


def get_player_name():
    """
    Asks for player name and validates it
    """
    while True:
        player = input(Fore.CYAN + "Please tell us your name so the bees"
                       " can say thanks!\n" + Fore.RESET)
        if len(player) >= 2 and not player.isnumeric():
            print(f'Thanks for helping the bees, {player}!\n')
            break
        if player.isnumeric():
            print("Numbers don't count! Try a name with letters")
        elif len(player) <= 2:
            print(f"The bees are friends, {player}, tell them your full name")
        else:
            print("That name is not valid, please enter a name with letters,"
                  " or characters, bees don't like strangers!")


def print_hive(hive):
    """
    Prints the hive
    """
    print("  1   2   3   4   5   6   7   8")
    print(Fore.YELLOW + "  -------------------------------" + Fore.RESET)
    row_number = 1
    for row in hive:
        print(str(row_number) + " " + Fore.YELLOW + " | ".join(row) +
              Fore.RESET)
        row_number += 1


def computer_create_bees(hive):
    """
    Loop for computer to generate random coordinates for bees to find
    """
    for i in range(NUM_BEES):
        bee_row, bee_column = randint(0, 7), randint(0, 7)
        hive[bee_row][bee_column] = "X"


def guess_bee_location(hive):
    """
    Asks for player input to guess bee location and validates it
    """
    turn = 0
    if turn in range(TURNS):
        while True:
            try:
                guess_row = int(input(Fore.CYAN + 'Guess which row a bee is'
                                      ' hiding on:\n' + Fore.RESET)) - 1
                if guess_row in range(0, 8):
                    break
                if guess_row not in range(0, 8):
                    print("That is outside the hive. Pick a number from 1-8")
            except ValueError as e:
                print("That's not an appropriate choice, it gave an error: "
                      f"{e}\n Please select a valid row by picking a number "
                      " from 1-8, then enter")

        while True:
            try:
                guess_column = int(input(Fore.CYAN + 'Guess which column a bee'
                                         ' is hiding on:\n' + Fore.RESET)) - 1
                if guess_column in range(0, 8):
                    break
                if guess_column not in range(0, 8):
                    print("That is outside the hive. Pick a number from 1-8")
            except ValueError as e:
                print("That's not an appropriate choice, it gave an error: "
                      f"{e}\n Please select a valid column by picking a number"
                      " from 1-8, then enter")
        return guess_row, guess_column


def keep_playing(question):
    """
    Chose whether the player wants to continue or quit the game.
    """
    while True:
        player_input = input(Fore.CYAN + (question) + Fore.RESET).upper()
        if player_input == 'Y':
            return True
        if player_input == 'N':
            return False
        else:
            print("Invalid choice. Please enter 'Y' or 'N'")


def clear_console():
    """
    Removes 1st line in windows and others
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If computer is running windows use cls
        command = 'cls'
    os.system(command)


def finish_game():
    """
    Reset the game or exit
    """
    question = 'Would you like to play again? Enter Y or N:\n'

    if keep_playing(question) is True:
        os.execv(sys.executable, ['python'] + sys.argv)
        play_game()
    elif keep_playing(question) is False:
        print('Bye for now. Come back again soon to help more bees!')
        SystemExit()


def play_game():
    """
    Runs game, clears 1st line, randomly creates the coordinates for hidden
    bees and places them in hidden hive, gets player name, asks if player
    wants to continue game, takes a turn, gives feedback, prints the hive
    with gueses and finishes game
    """
    clear_console()

    miss = "\U00002B21"
    found_bee = "\U0001F41D"

    success = 0
    computer_create_bees(PLAYER_BEE_HIVE)

    print_intro()

    get_player_name()

    question = 'Would you like to try to find the bees? Enter Y or N:\n'

    for turn in range(0, TURNS, 1):
        while True:
            if turn <= TURNS - 1:
                if not keep_playing(question):
                    print('Bye for now. Please come back soon to help free '
                          'the bees!')
                    sys.exit()
            print('Guess a bee location on the hive below...')
            print_hive(PLAYER_VISIBLE_HIVE)
            guess_row, guess_column = guess_bee_location(PLAYER_BEE_HIVE)
            if PLAYER_VISIBLE_HIVE[guess_row][guess_column] == miss:
                print(Fore.YELLOW + "You guessed that one already, have "
                      "another try." + Fore.RESET)
            elif PLAYER_VISIBLE_HIVE[guess_row][guess_column] == found_bee:
                print(Fore.YELLOW + "You guessed that one already, have "
                      "another try." + Fore.RESET)
            elif PLAYER_BEE_HIVE[guess_row][guess_column] == "X":
                print(Fore.GREEN + "SUCCESS! You fed a bee!" + Fore.RESET)
                PLAYER_VISIBLE_HIVE[guess_row][guess_column] = found_bee
                success += 1
                break
            else:
                print(Fore.RED + "MISS! The bees are still hungry" +
                      Fore.RESET)
                PLAYER_VISIBLE_HIVE[guess_row][guess_column] = miss
                break
            turn += 1

    print_hive(PLAYER_VISIBLE_HIVE)

    if success != 0:
        print(f'Well done for feeding {success} bees!')
    else:
        print('Bad luck, maybe you can feed more bees next time.')

    finish_game()


play_game()
