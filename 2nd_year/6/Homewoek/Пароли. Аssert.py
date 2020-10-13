l3 = [
    'qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
    'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl',
    'zxc', 'xcv', 'cvb', 'vbn', 'bnm', 
    'йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх', 'зхъ',
    'фыв', 'ыва', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ',
    'ячс', 'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю', 
]


def check_password(p):

    assert len(p) > 8

    assert p.lower() != p

    assert p.upper() != p

    assert any([i in p for i in list('0123456789')])

    assert not any([i in p.lower() for i in l3])

    return True


if __name__ == '__main__':
    try:
        check_password(input())
        print("ok")
    except AssertionError:
        print("error")


        
