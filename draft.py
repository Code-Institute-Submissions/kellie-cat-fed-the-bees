import unicodedata

from random import randint

import os
import sys

import pyfiglet

import colorama
from colorama import Fore

NUM_BEES = 10
TURNS = 5


class GameHive:
    def __init__(self, hive):
        self.hive = hive

    def get_player_name(self):
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

    def print_hive(self):
        """
        Prints the hive
        """
        print("  1   2   3   4   5   6   7   8")
        print(Fore.YELLOW + "  -------------------------------" + Fore.RESET)
        row_number = 1
        for row in self.hive:
            print(str(row_number) + " " + Fore.YELLOW + " | ".join(row) +
                  Fore.RESET)
            row_number += 1


class Bees:
    def __init__(self, hive):
        self.hive = hive
        self.bee_row = bee_row
        self.bee_column = bee_column

    def create_bees(self):
        """
        Loop for computer to generate random coordinates for bees to find
        """
        for i in range(NUM_BEES):
            self.bee_row, self.bee_column = randint(0, 7), randint(0, 7)
            while self.hive[self.bee_row][self.bee_column] == "X":
                self.bee_row, self.bee_column = randint(0, 7), randint(0, 7)
            self.hive[self.bee_row][self.bee_column] == "X"
        return self.hive

    def guess_bee_location(self):
        """
        Asks for player input to guess bee location and validates it
        """
        while True:
            try:
                bee_row = int(input(Fore.CYAN + 'Guess which row a bee '
                                    'is hiding on:\n' + Fore.RESET)) - 1
                if bee_row in range(0, 8):
                    break
                if bee_row not in range(0, 8):
                    print("That's not in the hive. Pick a number from 1-8")
            except ValueError and KeyError:
                print("That's not an appropriate choice, it gave an error:\n"
                      "Please select a valid row by picking a number from"
                      "1-8, then enter")

        while True:
            try:
                bee_column = int(input(Fore.CYAN + 'Guess which column a bee'
                                       ' is hiding on:\n' + Fore.RESET)) - 1
                if bee_column in range(0, 8):
                    break
                if bee_column not in range(0, 8):
                    print("That is outside the hive. Pick a number from 1-8")
            except ValueError as e:
                print("That's not an appropriate choice, it gave an error:\n"
                      "Please select a valid column by picking a number from "
                      "1-8, then enter")
        return bee_row, bee_column

    def count_fed_bees(self):
        success = 0
        for row in self.hive:
            for column in row:
                if column == 'X':
                    success += 1
        return success


def play_game():
    """
    """
    size = 8
    turns = 0

    miss = "\U00002B21"
    found_bee = "\U0001F41D"

    player_bee_hive = GameHive([[" "] * 8 for i in range(size)])
    # Where players guesses are displayed
    player_visible_hive = GameHive([[" "] * 8 for i in range(size)])

    Bees.create_bees(player_bee_hive)

    GameHive.get_player_name(player_bee_hive)

    while turns in range(0, TURNS):
        print('Guess a bee location on the hive below...')
        GameHive.print_hive(player_visible_hive)
        Bees.guess_bee_location(player_visible_hive)
    while player_bee_hive.hive[bee_row][bee_column] == miss:
        print(Fore.YELLOW + "You guessed that one already, have "
                "another try." + Fore.RESET)
        bee_row, bee_column = Bees.guess_bee_location(object)
    if player_visible_hive.hive[bee_row][bee_column] == 'X':
        print(Fore.YELLOW + "You guessed that one already, have "
                "another try." + Fore.RESET)
    elif player_bee_hive.hive[bee_row][bee_column] == 'X':
        print(Fore.GREEN + "SUCCESS! You fed a bee!" + Fore.RESET)
    else:
        print(Fore.RED + "MISS! The bees are still hungry" +
                Fore.RESET)
        player_visible_hive.hive[bee_row][bee_column] == miss
    turns += 1

    GameHive.print_hive(player_visible_hive)

    if Bees.count_fed_bees(player_visible_hive) == 5:
        print('Well done for feeding all the bees!')
    success = Bees.count_fed_bees(player_visible_hive)
    if success != 0:
        print(f'Well done for feeding {success} bees!')
    else:
        print('Bad luck, maybe you can feed more bees next time.')


def finish_game():
    SystemExit


finish_game()


if __name__ == '__main__':
    play_game()
