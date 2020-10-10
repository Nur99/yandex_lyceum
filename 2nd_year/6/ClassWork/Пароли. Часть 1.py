l3 = [
    'qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
    'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl',
    'zxc', 'xcv', 'cvb', 'vbn', 'bnm', 
    'йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх', 'зхъ',
    'фыв', 'ыва', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ',
    'ячс', 'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю', 'жэё'
]


def check(p):
    ret = 'ok'
    _error = 'error'

    if len(p) <= 8:
        ret = _error

    if p.lower() == p:
        ret = _error

    if p.upper() == p:
        ret = _error

    if not any([i in p for i in list('0123456789')]):
        ret = _error

    if any([i in p.lower() for i in l3]):
        ret = _error

    return ret


if __name__ == '__main__':
    print(check(input()))