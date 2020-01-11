def print_statistics(arr):
    print(len(arr))
    if len(arr) > 0:
        print(sum(arr) / len(arr))
        print(min(arr))
        print(max(arr))
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        if len(arr) % 2 == 0:
            print((arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2)
        else:
            print(arr[len(arr) // 2])
    else:
        print(0)
        print(0)
        print(0)
        print(0)
