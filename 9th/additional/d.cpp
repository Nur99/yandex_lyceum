from random import choice
from swift import words

d = [w.lower() for w in words]	
sequences = {}

for first, second in zip(d[:-1], d[1:]):
    if first not in sequences:
        sequences[first] = [second]
    else:
        sequences[first].append(second)

for i in range(10): # напечатаем 10 предложений
    first_w = choice(sequences["."]) # Начнем со слов, с которых обычно начинаются предложения
    print(first_w, end=" ")
    for i in range(50): # Не более 50 слов в предложении
        next_w = choice(sequences[first_w])
        print(next_w, end=" ")
        if next_w == '.':
            break
        first_w = next_w
    print()
