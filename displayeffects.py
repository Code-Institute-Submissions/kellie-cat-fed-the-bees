"""
Makes run.py more readable and shortens lines 
"""
import time
import os
import sys
import colorama
from colorama import Fore


class GameColours():
    """
    Holds a color shortcut library for the text in the game
    """
    R = Fore.RED
    G = Fore.GREEN
    Y = Fore.YELLOW
    C = Fore.CYAN
    RESET = Fore.RESET


def type_effect(text):
    """
    Function to add a typewriter effect to print statements.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.015)
    print()


def clear_console():
    """
    Removes 1st line in windows and others
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If computer is running windows use cls
        command = 'cls'
    os.system(command)
