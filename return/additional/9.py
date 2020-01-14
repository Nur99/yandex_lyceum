def check_pin(pinCode):
    one, two, three = pinCode.split('-')
    one = int(one)
    three = int(three)
    if two != two[::-1]:
        return 'Некорректен'
    else:
        flag = False
        if one > 1:
            flag = True
            for i in range(2, one):
                if (one % i) == 0:
                    flag = False
                    break
        if not flag:
            return 'Некорректен'
        else:
            if three & (three - 1):
                return 'Некорректен'
            else:
                return 'Корректен'
