import unicodedata
from random import randint
import pyfiglet
import os
import sys
from displayeffects import GameColours as Col
from displayeffects import clear_console
from displayeffects import type_effect
import ascii_art

SIZE = 8
NUM_BEES = 10
TURNS = 5
PLAYER = ''

# Where computer places their bees randomly
PLAYER_BEE_HIVE = [[" "] * 8 for i in range(SIZE)]
# Where players guesses are displayed
PLAYER_VISIBLE_HIVE = [[" "] * 8 for i in range(SIZE)]


def print_intro():
    """
    Displays title_art and game instructions
    """
    type_effect('Welcome to...\n')
    print((ascii_art.TITLE_ART) + Col.RESET)
    input("Press enter to read the game instructions...\n")
    print((ascii_art.INSTRUCTIONS) + Col.RESET)

def get_player_name():
    """
    Asks for player name and validates it
    """
    while True:
        PLAYER = input(Col.C + "Please tell us your name to start"
                       "feeding the bees!\n" + Col.RESET)
        if len(PLAYER.strip()) >= 2 and not PLAYER.isnumeric():
            type_effect(f'Thanks for helping the bees, {PLAYER}!\n')
            break
        if PLAYER.isnumeric():
            type_effect("Numbers on their own don't count! Try a name"
                        " with letters or characters too")
        elif len(PLAYER.strip()) <= 2:
            type_effect(f"'{PLAYER}' is not a valid choice, tell the "
                        "friendly bees your name with a few more letters"
                        " or characters")
        else:
            type_effect("That name is not valid, please enter a name with "
                        "letters, or characters, bees don't like strangers!")
    return PLAYER


def print_hive(hive):
    """
    Prints the hive
    """
    print("  1   2   3   4   5   6   7   8")
    print(Col.Y + "  -------------------------------" + Col.RESET)
    row_number = 1
    for row in hive:
        print(str(row_number) + " " + Col.Y + " | ".join(row) +
              Col.RESET)
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
                guess_row = int(input(Col.C + 'Guess which row a bee is'
                                      ' hiding on:\n' + Col.RESET)) - 1
                if guess_row in range(0, 8):
                    break
                if guess_row not in range(0, 8):
                    type_effect("That is outside the hive. Pick a number 1-8")
            except ValueError as e:
                type_effect("That's not a valid choice, it gave an error: "
                            "Please select a valid row by picking a number"
                            " from 1-8, then enter")

        while True:
            try:
                guess_column = int(input(Col.C + 'Guess which column a bee'
                                         ' is hiding on:\n' + Col.RESET)) - 1
                if guess_column in range(0, 8):
                    break
                if guess_column not in range(0, 8):
                    type_effect("That is outside the hive. Pick a number 1-8")
            except ValueError:
                type_effect("That's not a valid choice, it gave an error: "
                            "Please select a valid column by picking a number"
                            " from 1-8, then enter")
        return guess_row, guess_column


def keep_playing(question):
    """
    Chose whether the player wants to continue or quit the game.
    """
    while True:
        player_input = input(Col.C + (question) + Col.RESET).upper()
        if player_input == 'Y':
            return True
        if player_input == 'N':
            type_effect('Bye for now. Come back again soon to help more bees!')
            sys.exit()
        else:
            type_effect("Invalid choice. Please enter 'Y' or 'N'")


def finish_game():
    """
    Reset the game or exit
    """
    question = 'Would you like to play again? Enter Y or N:\n'
    while True:
        if keep_playing(question) is True:
            os.execv(sys.executable, ['python'] + sys.argv)
            play_game()
        else:
            type_effect('Bye for now. Come back again soon to help more bees!')
            sys.exit()


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
                    type_effect('Bye for now. Please come back soon to help '
                                'free the bees!')
                    sys.exit()
            type_effect('Guess a bee location on the hive below...')
            print_hive(PLAYER_VISIBLE_HIVE)
            guess_row, guess_column = guess_bee_location(PLAYER_BEE_HIVE)
            if PLAYER_VISIBLE_HIVE[guess_row][guess_column] == miss:
                print(Col.Y + "You guessed that one already, have "
                      "another try." + Col.RESET)
            elif PLAYER_VISIBLE_HIVE[guess_row][guess_column] == found_bee:
                print(Col.Y + "You guessed that one already, have "
                      "another try." + Col.RESET)
            elif PLAYER_BEE_HIVE[guess_row][guess_column] == "X":
                print(Col.G + "SUCCESS! You fed a bee!" + Col.RESET)
                PLAYER_VISIBLE_HIVE[guess_row][guess_column] = found_bee
                success += 1
                break
            else:
                print(Col.R + "MISS! The bees are still hungry" +
                      Col.RESET)
                PLAYER_VISIBLE_HIVE[guess_row][guess_column] = miss
                break
            turn += 1

    print_hive(PLAYER_VISIBLE_HIVE)

    if success != 0:
        type_effect(f'Well done for feeding {success} bees!\n'
                    'That is this round of Free the Bees over!')
    else:
        type_effect(f'Bad luck, maybe you can feed more bees'
                    ' next time.\n That is this round of Free '
                    'the Bees over!')

    finish_game()


play_game()
