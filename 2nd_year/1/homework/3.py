h = input().split()
m = input().split()
for i in range(len(h)):
    h[i] = int(h[i])
for i in range(len(m)):
    m[i] = int(m[i])
h.sort()
m.sort()
for i in range(len(h)):
    if h[i] < 10:
        h[i] = '0' + str(h[i])
    else:
        h[i] = str(h[i])
for i in range(len(m)):
    if m[i] < 10:
        m[i] = '0' + str(m[i])
    else:
        m[i] = str(m[i])
for i in h:      
    for j in m:
        if int(i[0]) + int(i[1]) != int(j[0]) + int(j[1]):
            print(i + ':' + j)

