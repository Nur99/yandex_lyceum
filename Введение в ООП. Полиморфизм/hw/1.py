class MinStat:
    def __init__(self):
        self.min_ = None

    def add_number(self, x):
        if self.min_ is None:
            self.min_ = x
        else:
            self.min_ = min(self.min_, x)

    def result(self):
        return self.min_


class MaxStat:
    def __init__(self):
        self.max_ = None

    def add_number(self, x):
        if self.max_ is None:
            self.max_ = x
        else:
            self.max_ = max(self.max_, x)

    def result(self):
        return self.max_


class AverageStat:
    def __init__(self):
        self.sum_ = 0
        self.n = 0

    def add_number(self, x):
        self.sum_ += x
        self.n += 1

    def result(self):
        if self.n == 0:
            return None
        else:
            return self.sum_ / self.n

