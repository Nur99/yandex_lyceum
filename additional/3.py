def squared():
    for i in range(1, 10):
        for j in range(1, 10):
            if j != 9:
                print(str((i * 10 + j) ** 2).ljust(4), end=" ")
            else:
                print(str((i * 10 + j) ** 2))
