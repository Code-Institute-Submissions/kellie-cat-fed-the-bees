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


class Bees:
    def __init__(self, hive):
        self.hive = hive

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
        try:
            bee_row = int(input(Fore.CYAN + 'Guess which row a bee '
                                'is hiding on:\n' + Fore.RESET)) - 1
            while bee_row not in range(0, 8):
                print("That's not in the hive. Pick a number from 1-8")
                bee_row = int(input(Fore.CYAN + 'Guess which row a bee '
                                'is hiding on:\n' + Fore.RESET)) - 1

            bee_column = int(input(Fore.CYAN + 'Guess which column a bee'
                                    ' is hiding on:\n' + Fore.RESET)) - 1
            while bee_column not in range(0, 8):
                print("That is outside the hive. Pick a number from 1-8")
                bee_column = int(input(Fore.CYAN + 'Guess which column a bee'
                                    ' is hiding on:\n' + Fore.RESET)) - 1
            return bee_row, bee_column
        except ValueError or KeyError:
            print("That's not an appropriate choice, it gave an error.\n"
                  "Please select a valid column by picking a number from "
                  "1-8, then enter")
            return self.guess_bee_location()


def play_game():
    """
    """
    size = 8
    success = 0

    miss = "\U00002B21"
    found_bee = "\U0001F41D"

    player_bee_hive = GameHive([[" "] * 8 for i in range(size)])
    # Where players guesses are displayed
    player_visible_hive = GameHive([[" "] * 8 for i in range(size)])

    Bees.create_bees(player_bee_hive)

    GameHive.get_player_name(player_bee_hive)
    GameHive.print_hive(player_bee_hive)

    for turn in range(0, TURNS):
        while True:
            if turn <= TURNS - 1:
                print('Guess a bee location on the hive below...')
                GameHive.print_hive(player_visible_hive)
                bee_row, bee_column = Bees.guess_bee_location(object)
            if player_bee_hive.hive[bee_row][bee_column] == miss:
                print(Fore.YELLOW + "You guessed that one already, have "
                      "another try." + Fore.RESET)
            elif player_visible_hive.hive[bee_row][bee_column] == found_bee:
                print(Fore.YELLOW + "You guessed that one already, have "
                      "another try." + Fore.RESET)
            elif player_bee_hive.hive[bee_row][bee_column] == "X":
                print(Fore.GREEN + "SUCCESS! You fed a bee!" + Fore.RESET)
                success += 1
                break
            else:
                print(Fore.RED + "MISS! The bees are still hungry" +
                      Fore.RESET)
                Bees.guess_bee_location(player_visible_hive) == miss
                break
            turn += 1

    GameHive.print_hive(player_visible_hive)

    if success != 0:
        print(f'Well done for feeding {success} bees!')
    else:
        print('Bad luck, maybe you can feed more bees next time.')


if __name__ == '__main__':
    play_game()
    