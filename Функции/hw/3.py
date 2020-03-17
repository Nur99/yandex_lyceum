def golden_ratio(i):
    a = 1
    b = 1
    for j in range(2, i + 1):
        a, b = b, a + b
    print(b / a)
