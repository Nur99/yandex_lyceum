def num_digits(number):
    result = 1
    while number >= 10:
        result += 1
        number //= 10
    return result

