def ask_password(login, password, success, failure):
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = list(filter(lambda letter: letter not in vowels, letters))
    login = login.lower()
    password = password.lower()
    number_of_vowels = len(list(filter(lambda letter: letter in vowels, password)))
    consonants_in_login = list(filter(lambda letter: letter in consonants, login))
    consonants_in_passwords = list(filter(lambda letter: letter in consonants, password))

    if (number_of_vowels != 3) and (consonants_in_login != consonants_in_passwords):
        failure(login, 'Everything is wrong')
    elif number_of_vowels != 3:
        failure(login, 'Wrong number of vowels')
    elif consonants_in_login != consonants_in_passwords:
        failure(login, 'Wrong consonants')
    else:
        success(login)


def main(login, password):
    ask_password(
        login,
        password,
        lambda name: print('Привет, {}!'.format(name)),
        lambda name, error: print(
            'Кто-то пытался притвориться пользователем {}, но в пароле '
            'допустил ошибку: {}.'.format(name, error.upper())
        )
    )
