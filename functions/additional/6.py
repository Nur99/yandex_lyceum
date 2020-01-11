def eratosthenes(N):
    s = []
    for i in range(1, N + 1):
        s.append(i)
    i = 2
    while i < N:
        for j in s:
            if (j % i == 0) and (j != i):
                print(j)
                del s[s.index(j)]
        for j in s:
            if j > i:
                i = j
                N = s[-1]
                break
