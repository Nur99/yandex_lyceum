x, y = [], []
for i in range(int(input())):
    a = input().split()
    a = [int(a[0]), int(a[1])]
    if (a[0] != a[1]) and (a[0] != - 1 * a[1]):
        if abs(a[1]) < abs(a[0]):
            print('(' + str(a[0]) + ', ' + str(a[1]) + ')')
    x.append(a[0])
    y.append(a[1])
print('left:', (min(x), y[x.index(min(x))]))
print('right:', (max(x), y[x.index(max(x))]))
print('top:', (x[y.index(max(y))], max(y)))
print('bottom:', (x[y.index(min(y))], min(y)))
