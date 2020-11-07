import sqlite3

con = sqlite3.connect('music_db.sqlite')
cur = con.cursor()
genre = input()
# genre_id = cur.execute(f"""-- SELECT GenreId FROM Genre WHERE Name = {genre}""").fetchone()
# result = cur.execute(f"""-- SELECT Title FROM Album WHERE AlbumId IN (SELECT AlbumId FROM Track WHERE GenreId = {genre_id})""").fetchall()
res = con.cursor().execute(
    f"""SELECT DISTINCT title FROM album where albumid in
    (SELECT albumid from track where genreid in
    (select genreid from genre where name = '{genre}')) ORDER BY artistid, title""").fetchall()


con.close()
for item in result:
    print(item[0])
