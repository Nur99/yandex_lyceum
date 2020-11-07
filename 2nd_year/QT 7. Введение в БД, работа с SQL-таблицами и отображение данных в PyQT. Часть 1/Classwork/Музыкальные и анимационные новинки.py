import sqlite3

"""
SELECT перечень_полей FROM имя_таблицы
        WHERE условие
"""
# Подключение к БД
con = sqlite3.connect(input())

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT title FROM Films
        WHERE duration >= 60 AND genre =
        (SELECT id FROM genres WHERE title = 'комедия')""").fetchall()

# Отключиться от БД
con.close()

# Вывод результатов на экран
for item in result:
    print(item[0])
