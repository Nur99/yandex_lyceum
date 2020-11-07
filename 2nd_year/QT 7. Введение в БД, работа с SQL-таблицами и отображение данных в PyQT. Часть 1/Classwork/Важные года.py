import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT year FROM Films WHERE title LIKE 'Х%' ORDER BY year""").fetchall()
con.close()
for item in result:
    print(item[0])
