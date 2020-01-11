def ask_password():
    r = 0
    for i in range(3):
        d = input()
        if d == "password":
            print("Пароль принят")
            r = 1
            break
    if r != 1:
        print("В доступе отказано")
