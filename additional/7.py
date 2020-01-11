def print_long_words(text):
    x = []
    for i in text:
        if not i.isalpha():
            text = text.split(i)
            x.append(text[0])
            if len(text) > 1:
                text = text[1:]
            text = str(i).join(text)
    for i in x:
        s = 0
        for j in i:
            if not j.isalpha():
                i = i[:i.index(j)] + i[i.index(j) + 1:]
            elif j in "а, о, э, и, у, ы, е, ё, ю, я, a, e, i, o, u, y":
                s += 1
        i = "".join(i)
        if s >= 4:
            print(i)
