import random
count = 0
for i in range(2999):
    x, y = random.random(), random.random()
    if x ** 2 + y ** 2 <= 1:
        count += 1
print(count / 2999 * 4) 
