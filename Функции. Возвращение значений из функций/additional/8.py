def password_level(s):
    level = 0
    # Проверим длину пароля
    if len(s) < 6:
        level = -1
    # Проверим, состоит ли пароль только из цифр
    elif s.isdigit():
        level = 0
    # Остальные варианты
    else:
        # Есть ли в пароле символы разных регистров
        if s != s.lower() and s != s.upper():
            level += 1
        for i in '0123456789':
            if i in s:
                level += 1
                break
    levels = ['Ненадежный', 'Слабый', 'Надежный', 'Недопустимый']
    return levels[level] + ' пароль'
