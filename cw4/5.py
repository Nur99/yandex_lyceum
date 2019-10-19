i = input()

i = int(i)

s = 0

while i > 0:

    s = (i % 8)

    i = i // 8

print(s)
