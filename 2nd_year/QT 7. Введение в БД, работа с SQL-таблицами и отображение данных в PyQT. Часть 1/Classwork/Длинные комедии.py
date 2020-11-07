import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films WHERE duration >=60
AND genre = (SELECT id FROM genres WHERE title='комедия')""").fetchall()
con.close()
for item in result:
    print(item[0])
