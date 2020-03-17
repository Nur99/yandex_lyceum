from random import choice
from swift import words
d = [w.lower() for w in words]	
s = {}

for first, second in zip(d[:-1], d[1:]):
    if first not in s:
        s[first] = [second]
    else:
        s[first].append(second)

for i in range(10):
    first_w = choice(s["."])
    print(first_w, end=" ")
    for i in range(25):
        next_w = choice(s[first_w])
        print(next_w, end=" ")
        if next_w == '.':
            break
        first_w = next_w
    print()
