import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
res = cur.execute("""SELECT title FROM Films
     WHERE year >= 1995 AND year <= 2000 AND genre IN
     (SELECT id FROM genres WHERE title = 'детектив')""").fetchall()
con.close()
for i in res:
    print(i[0])