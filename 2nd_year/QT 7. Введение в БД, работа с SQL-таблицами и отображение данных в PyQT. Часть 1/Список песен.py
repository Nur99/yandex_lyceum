import sqlite3

con = sqlite3.connect('music.db')
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT name FROM tracks WHERE album in (SELECT id from albums WHERE artist = (SELECT id from artists WHERE name='Alik')) ORDER BY name""").fetchall()
con.close()
for item in result:
    print(item[0])
