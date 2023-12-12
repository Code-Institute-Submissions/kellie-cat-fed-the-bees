class Bee:
    def __init__(self, kind, number):
        self.kind = kind
        self.number = number


bee_1 = Bee('worker', 10)
bee_2 = Bee('queen', 1)
bee_3 = Bee('drone', 4)

print(bee_1.kind)