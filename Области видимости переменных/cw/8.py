numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []  # В прошлом случае id переменных совпадали,
# то есть их значения были равны
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
