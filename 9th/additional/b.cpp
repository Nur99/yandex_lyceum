from string import ascii_lowercase as en, ascii_uppercase as EN, digits
import random


def generate_password(m):
    assert m >= 3
    valid_EN = set(EN) - {'I', 'O'}
    p_EN = random.choice(list(valid_EN))
    rest_EN = list(valid_EN - {p_EN})
    valid_en = set(en) - {'l', 'o'}
    p_en = random.choice(list(valid_en))
    rest_en = list(valid_en - {p_en})
    valid_digits = set(digits) - {'0', '1'}
    p_digit = random.choice(list(valid_digits))
    rest_digits = list(valid_digits - {p_digit})
    all_rest_valid = rest_EN + rest_en + rest_digits

    password = random.sample(all_rest_valid, m - 3) + [p_EN, p_en, p_digit]
    random.shuffle(password)
    return ''.join(password)


def main(n, m):
    passwords = []
    for _ in range(n):
        passwords.append(generate_password(m))
        while passwords[-1] in passwords[:-1]:
            passwords[-1] = generate_password(m)
    return passwords


if __name__ == '__main__':
    print("Случайный пароль из 7 символов:", generate_password(7))
    print("10 случайных паролей длиной 15 символов:")
    print(*main(10, 15), sep="\n")
