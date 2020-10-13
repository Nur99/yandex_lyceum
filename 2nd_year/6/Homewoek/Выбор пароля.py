l3 = [
    'qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
    'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl',
    'zxc', 'xcv', 'cvb', 'vbn', 'bnm',
    'йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх', 'зхъ',
    'фыв', 'ыва', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ',
    'ячс', 'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю',
]


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(p):
    if len(p) <= 8:
        raise LengthError

    if p.lower() == p:
        raise LetterError

    if p.upper() == p:
        raise LetterError

    if not any([i in p for i in list('0123456789')]):
        raise DigitError

    if any([i in p.lower() for i in l3]):
        raise SequenceError

    return True


if __name__ == '__main__':
    while True:
        try:
            line = input()
            if line == 'Ctrl+Break':
                raise KeyboardInterrupt()
            check_password(line)
            print("ok")
            break
        except PasswordError as PE:
            print(PE.__class__.__name__)
        except KeyboardInterrupt:
            print("Bye-Bye")
            break