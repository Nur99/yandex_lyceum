def bracket_check(test_string):
    k = []
    w = 0
    for i in test_string:
        if i == "(":
            k.append("")
        else:
            if len(k) > 0:
                del k[-1]
            else:
                w += 1
    if (len(k) == 0) and (w == 0):
        print("YES")
    else:
        print("NO")
