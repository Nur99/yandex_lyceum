import sys
from random import shuffle

names = [n for n in sys.stdin.read().split('\n') if n]

names2 = names[:]

while True:
    shuffle(names2)
    if not any(names[i] == names2[i] for i in range(len(names))):
        break

for i in range(len(names)):
    print("%s - %s" % (names[i], names2[i]))

