def triangle(a, b, c):
    s = 0
    if a + b > c:
        if a + c > b:
            if c + b > a:
                s = 1
    if s == 1:
        print("Это треугольник")
    else:
        print("Это не треугольник")
