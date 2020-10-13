with open('pipes.txt') as in_file, open('time.txt', 'w') as out_file:
    *efficiency, pipes = in_file.readlines()
    efficiency = list(map(float, efficiency[:-1]))
    pipes = list(map(int, pipes.split()))
    arr = [efficiency[i - 1] for i in pipes]
    summary = sum(map(lambda x: 1 / x, arr))
    result = 60 / summary

    print(result, file=out_file)
