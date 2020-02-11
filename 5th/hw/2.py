def partial_sums(*numbers):
    result = [0]
    for number in numbers:
        result.append(result[-1] + number)
    return result
