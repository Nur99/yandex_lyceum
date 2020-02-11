def matrix(m=1, n=None, a=0):
    if not n:
        n = m
    return [[a for j in range(n)] for i in range(m)]

