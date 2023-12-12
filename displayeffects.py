"""
Import section
"""
import colorama
from colorama import Fore


class GameColors():
    """
    Holds a color shortcut library for the text in the game
    """
    R = Fore.RED
    G = Fore.GREEN
    Y = Fore.YELLOW
    C = Fore.CYAN
    RESET = Fore.RESET


def strip_color_codes(text):
    """
    Function to remove color codes from the given text
    https://www.w3schools.com/python/ref_string_strip.asp
    """
    return Fore.strip(text)
