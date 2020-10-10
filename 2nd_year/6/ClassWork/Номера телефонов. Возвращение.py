def to_std(tel):
    _error_msg = "error"

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
        return "неверный формат"

    if not len(tel[1:]) == 11:
        return "неверное количество цифр"

    return tel


if __name__ == "__main__":
    print(to_std(input()))