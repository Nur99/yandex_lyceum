from sys import stdin
 
 
clov = []
s = [i.replace('\n', '') for i in stdin.readlines()]
w = s[0]
for i in s[1:]:
    pr = []
    a = (list(w)).copy()
    for j in i:
        if j in a:
            del a[a.index(j)]
            pr.append(True)
        else:
            pr.append(False)
    if False not in pr:
        clov.append(i)
print(len(clov))
for i in clov:
    print(i)
