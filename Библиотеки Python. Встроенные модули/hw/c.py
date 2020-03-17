from math import sin, pi
import datetime as dt


def emotion(t):
    p = 28
    b = sin((2 * pi * t) / p) * 100
    return b

    
def phisic(t):
    p = 23
    b = sin((2 * pi * t) / p) * 100
    return b


def intell(t):
    p = 33
    b = sin((2 * pi * t) / p) * 100
    return b


d1 = input().split(".")
r1 = int(d1[0])
m1 = int(d1[1])
g1 = int(d1[2])
d1 = dt.date(g1, m1, r1)
d2 = input().split(".")
r1 = int(d2[0])
m1 = int(d2[1])
g1 = int(d2[2])
d2 = dt.date(g1, m1, r1)
t = (d2 - d1).days
print(phisic(t))
print(emotion(t))
print(intell(t))
