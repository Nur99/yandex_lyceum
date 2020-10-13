def lr(a, b):
    return list(range(a, b + 1))


def to_std(tel):
    try:
        tel = "".join(tel.split())

        s = tel.find("(")
        if s > -1:
            e = tel.index(")", s + 2)
            tel = list(tel)
            tel.pop(s)
            tel.pop(e - 1)
            tel = "".join(tel)

        if tel.find("+7") != 0 and tel.find("8") != 0:
            raise ValueError

        if tel.find("8") == 0:
            tel = "+7" + tel[1:]

        tel = "+" + "".join(str(int(p)) for p in tel.split("-"))

    except Exception:
        raise ValueError("неверный формат")

    if not len(tel[1:]) == 11:
        raise ValueError("неверное количество цифр")

    ranges = (lr(910, 919) + lr(980, 989) + lr(920, 929) +
              lr(930, 939) + lr(902, 906) + lr(960, 969))
    if int(tel[2:5]) not in ranges:
        raise ValueError("не определяется оператор сотовой связи")

    return tel


if __name__ == "__main__":
    try:
        print(to_std(tel=input()))
    except ValueError as e:
        print(e)