class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        return sum([self.transform(n) for n in range(1, N + 1)])


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3
