def roots_of_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return ['all']
            else:
                return []
        else:
            return [-c / b]
    else:
        D = b ** 2 - 4 * a * c
        if D < 0:
            return []
        elif D == 0:
            return [-b / (2 * a)]
        else:
            x1 = (-b - D ** 0.5) / (2 * a)
            x2 = (-b + D ** 0.5) / (2 * a)
            return [x1, x2]
