import random
from datetime import timedelta


class Game:
    def __init__(self):
        self.result = None

    def play(self):
        pass

    def __str__(self):
        return f'Result: {self.result}'


class HeadsOrTails(Game):
    def play(self):
        self.result = random.choice(['Heads', 'Tails'])


class Dice(Game):
    def play(self):
        self.result = random.randint(1, 6)


class RandomNumber(Game):
    def play(self):
        self.result = random.randint(1, 100)


def get_random_date(start, end):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))
