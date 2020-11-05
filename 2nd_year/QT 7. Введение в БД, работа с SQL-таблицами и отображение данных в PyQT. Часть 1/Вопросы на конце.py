import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films WHERE title LIKE '%?'""").fetchall()
con.close()
for item in result:
    print(item[0])

"""
А_и% = Али, Алик, АлиАбавава
%? = Как достать соседа? 
"""
