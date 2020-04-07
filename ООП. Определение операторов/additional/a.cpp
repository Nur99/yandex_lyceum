class Polynomial:
    def __init__(self, coefs):
        self.coefs = coefs

    def __call__(self, x):
        x_pow = 1
        result = 0
        for coef in self.coefs:
            result += coef * x_pow
            x_pow *= x
        return result

    def __add__(self, other):
        size = max(len(self.coefs), len(other.coefs))
        new_coefs = [0] * size
        for i in range(len(self.coefs)):
            new_coefs[i] += self.coefs[i]
        for i in range(len(other.coefs)):
            new_coefs[i] += other.coefs[i]
        return Polynomial(new_coefs)

