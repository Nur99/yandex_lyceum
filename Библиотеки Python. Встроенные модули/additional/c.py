from random import choice


def func1(n):
    return list(str(n))


def func2(n1, n2):
    buk = 0
    korova = 0
    i = 0
    while i < 4:
        if n1[i] == n2[i]:
            buk += 1
            del n1[i]
            del n2[i]
            i -= 1
        i += 1 
    for i in range(len(n2)):
        for j in range(len(n1)):
            if n1[j] == n2[i]:
                kotova += 1
    return buk, korova


def func3(n1, n2):
    global history
    n3 = n1.copy()
    i = 0
    while i < 4:
        if n1[i] == n2[i]:
            del n1[i]
            del n2[i]
            i -= 1
        i += 1
    a = list()
    for i in range(len(n2)):
        for j in range(len(n1)):
            if n1[j] == n2[i]:
                a.append([n2[i], i])
    for i in range(len(a)):
        n3[a[i][1]] = a[i][1] 
    return n3


history = list()
n = choice([i for i in range(1000, 9999)])
n = func1(n)
n1 = int(input())
while n1 != n:
    n1 = func1(n1)
    buk, korova = func2(n, n1)
    print(buk, korova)
    history.append([int(''.join(n1)), buk, korova])
    n = func3(n, n1)
    n1 = int(input())
