line = input().split(' -> ')
for i in range(int(input())):
    a = input()
    if a == line[0]:
        print(' -> '.join(line[:2]))
    elif a == line[len(line) - 1]:
        print(' -> '.join(line[len(line) - 2:]))
    else:
        print(' -> '.join(line[line.index(a) - 1:line.index(a) + 2]))

    
