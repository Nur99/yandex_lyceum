def catalan(n):
    num = [1]
    for i in range(1, n + 1):
        k = 0
        for j in range(0, i):
            k += num[j] * num[i - j - 1]
        num.append(k)
    return num[-1]
