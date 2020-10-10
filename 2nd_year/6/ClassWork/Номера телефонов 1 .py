def to_std(tel):
    _error_msg = "error"

    tel = "".join(tel.split())  # убрали все пробелы

    if tel.find("+7") != 0 and tel.find("8") != 0:
        return _error_msg

    if not all(tel.split("-")):  # условие на знак -, нет пустых строк, если разделим по ним
        return _error_msg
    else:
        tel = tel.replace("-", "")

    start_bt = tel.find("(")
    end_bt = tel.find(")")

    if start_bt > -1:
        if end_bt < start_bt or not tel[start_bt + 1:end_bt].isdigit() \
                or not tel.count("(") == 1 or not tel.count(")") == 1:
            return _error_msg
    else:
        if end_bt > -1:
            return _error_msg

    tel = tel.replace("(", "")
    tel = tel.replace(")", "")

    if tel.find("8") == 0:
        tel = "+7" + tel[1:]

    if not tel[1:].isdigit() or not len(tel[1:]) == 11:
        return _error_msg

    return tel


if __name__ == "__main__":
    print(to_std(input()))