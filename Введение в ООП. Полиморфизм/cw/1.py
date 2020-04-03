class Selector:
    def __init__(self, lst):
        self.evens = []
        self.odds = []
        for i in lst:
            if i % 2 == 0:
                self.evens.append(i)
            else:
                self.odds.append(i)

    def get_odds(self):
        return self.odds

    def get_evens(self):
        return self.evens
