def prime(number):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                return "Составное число"
        return "Простое число"
