i = input()

s = 0

while float(i) > 0:

    if (float(i) < 1000):

        s += float(i)

    else:

        s = s + float(i) - float(i) * 0.05

    i = input()

print(s)
