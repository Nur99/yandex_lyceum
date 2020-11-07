import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM genres WHERE id IN
(SELECT DISTINCT genre FROM Films WHERE year IN (2010,2011))""").fetchall()
con.close()
for item in result:
    print(item[0])
