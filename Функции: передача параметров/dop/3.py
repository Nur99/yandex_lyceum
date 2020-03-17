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


def solve(*coefficients):
    if len(coefficients) == 0 or len(coefficients) > 3:
        return None
    elif len(coefficients) == 3:
        a, b, c = coefficients
    elif len(coefficients) == 2:
        a = 0
        b, c = coefficients
    else:
        a = b = 0
        c, = coefficients
    return roots_of_quadratic_equation(a, b, c)


# Получим список чисел-коэффициентов
coefficients = [float(x) for x in input().split()]
# Раскроем список коэффициентов в набор аргументов функции
# Cписок корней, которые являются результатом выполнения функции - 
#   раскроем как отдельные аргументы функции print
print(*solve(*coefficients))
