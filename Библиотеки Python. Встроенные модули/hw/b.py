from random import choice
from string import ascii_lowercase, digits, ascii_uppercase


def generate_password(k):
    x = ascii_uppercase + digits + ascii_lowercase
    y = []
    for i in x:
        y.append(i)
    f = ""
    d = "lIOo01"
    q = choice(ascii_uppercase)
    while (q in d) or (q in f):
        q = choice(ascii_uppercase)
    f += q
    q = choice(ascii_lowercase)
    while (q in d) or (q in f):
        q = choice(ascii_lowercase)
    f += q
    q = choice(digits)
    while (q in d) or (q in f):
        q = choice(digits)
    f += q
    for i in range(k - 3):
        q = choice(y)
        while (q in d) or (q in f):
            q = choice(y)
        f += q
    return f


def main(n, m):
    w = []
    for i in range(n):
        k = generate_password(m)
        while k in w:
            k = generate_password(m)
        w.append(k)
    return w
