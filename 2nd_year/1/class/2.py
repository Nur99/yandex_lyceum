kol = int(input())
first, second, third, fourth = 0, 0, 0, 0
for i in range(kol):
    k = input()
    k = k.split()
    f = int(k[0])
    s = int(k[1])
    if f == 0 or s == 0:
        print((f, s))
    else:
        if f > 0 and s > 0:
            first += 1
        if f > 0 and s < 0:
            fourth += 1
        if f < 0 and s > 0:
            second += 1
        if f < 0 and s < 0:
            third += 1
print('I: ', first, ', ', 'II: ', second, ', ', sep='', end='')
print('III: ', third, ', ', 'IV: ', fourth, '.', sep='')

