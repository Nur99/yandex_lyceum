def equation(a, b):
    a = a.split(";")
    b = b.split(";")
    if a[0] == b[0]:
        print(float(a[0]))
    elif a[1] == b[1]:
        print(float(a[1]))
    else:
        s = (float(b[1]) - float(a[1])) / (float(b[0]) - float(a[0]))
        print(s, end=" ")
        print(float(a[1]) - float(a[0]) * s)
