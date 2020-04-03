class OddEvenSeparator:
    def __init__(self):
        self.odds = []
        self.evens = []

    def add_number(self, x):
        if x % 2 == 0:
            self.evens.append(x)
        else:
            self.odds.append(x)

    def even(self):
        return self.evens

    def odd(self):
        return self.odds
