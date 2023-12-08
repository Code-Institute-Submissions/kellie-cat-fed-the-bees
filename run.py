from random import randint

# Where computer places their bees randomly
PLAYER_BEE_HIVE = [[" "] * 8 for i in range(8)]
# Where players guesses are displayed
PLAYER_VISIBLE_HIVE = [[" "] * 8 for i in range(8)]
# Where computer guesses are displayed and where player inputs their bees
COMPUTER_VISIBLE_HIVE = [[" "] * 8 for i in range(8)]
