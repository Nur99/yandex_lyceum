def line(s, t):
    t = t.split(";")
    s = s.split("x")
    d = s[0]
    if float(t[1]) == (float(d) * float(t[0]) + float(s[-1])):
        print("True")
    else:
        print("False")
