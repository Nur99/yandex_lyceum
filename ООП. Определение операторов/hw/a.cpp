DAYS_PER_MONTH = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Date:
    def __init__(self, month, day):
        self.ordinal = sum(DAYS_PER_MONTH[1:month]) + day

    def __sub__(self, other):
        return self.ordinal - other.ordinal
