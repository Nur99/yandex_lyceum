import string
import random


def generate_password(m):
    valid_symbols = list(set(string.ascii_letters + string.digits) - {'I', 'l', '1', 'o', 'O', '0'})
    # return ''.join(random.choices(valid_symbols, k=m))  # 3.6+
    return ''.join(random.choice(valid_symbols) for _ in range(m))


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
