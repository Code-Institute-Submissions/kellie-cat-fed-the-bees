class Bee:
    def __init__(self, kind, number):
        self.kind = kind
        self.number = number


bee_1 = Bee('worker', 10)
bee_2 = Bee('queen', 1)
bee_3 = Bee('drone', 4)

print(bee_1.kind)


class Continue:
    def __init__(self, question):
        self.question = question


start_play = Continue('Are you ready to feed the bees? Enter Y to play or'
                      ' N to end the program:\n')
keep_playing = Continue('Would you like to keep looking for bees? Enter Y'
                        ' or N:\n')
finish_game = Continue('Would you like to play again? Enter Y or N:\n')

print(start_play.question)
