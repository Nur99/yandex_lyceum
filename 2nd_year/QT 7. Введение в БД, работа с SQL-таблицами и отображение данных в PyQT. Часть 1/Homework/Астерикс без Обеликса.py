import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films WHERE 
title LIKE '%Астерикс%' AND 
title NOT LIKE '%Обеликс%'""").fetchall()
con.close()
for item in result:
    print(item[0])
