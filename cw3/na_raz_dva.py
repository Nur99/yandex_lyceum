a = int(input())

b = int(input())

c = int(input())

d = 0

e = 0

f = 0

if a >= b and b >= c:

    d = a

    e = b

    f = c

elif a <= b and b <= c:

    d = c

    e = b

    f = a

elif a <= b and a >= c:

    d = b

    e = a

    f = c

elif b >= c and c >= a:

    d = b

    e = c

    f = a

elif c >= a and a >= b:

    d = c

    e = a

    f = b

else:

    d = a

    e = c

    f = b

print(d)

print(e)

print(f)
