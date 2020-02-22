from random import random


# Сравниваем площадь четверти круга
# единичного радиуса с площадью единичного квадрата

count = 0
N = 1000000

for i in range(N):
    x = random()
    y = random()

    if x**2 + y ** 2 <= 1:
        count += 1

print(count / N * 4) 
