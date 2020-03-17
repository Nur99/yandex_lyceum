def letter(email, name, date, place='Москве'):
    head = f'To: {email}'
    greet = f'Здравствуйте, {name}!'
    body = f'Были бы рады видеть вас на встрече начинающих программистов в {place}, которая пройдёт {date}.'
    return "\n".join((head, greet, body))
