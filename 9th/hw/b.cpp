from string import ascii_lowercase as en, ascii_uppercase as EN, digits
import random


def generate_password(m):
    valid_EN = list(set(EN) - {'I', 'O'})
    valid_en = list(set(en) - {'l', 'o'})
    valid_digits = list(set(digits) - {'0', '1'})
    all_valid = valid_EN + valid_en + valid_digits
    p_EN = random.choice(valid_EN)
    p_en = random.choice(valid_en)
    p_digit = random.choice(valid_digits)
    password = [random.choice(all_valid) for _ in range(m - 3)] + [p_EN, p_en, p_digit]
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
