import sqlite3

genre = input().strip()
con = sqlite3.connect('music_db.sqlite')
# res = con.cursor().execute(
#     f"""SELECT name from artist WHERE artistid in
#     (SELECT artistid FROM album where albumid in
#     (SELECT albumid from track where genreid in
#     (select genreid from genre where name = '{genre}'))) ORDER BY name""").fetchall()
res = con.cursor().execute(
    f"""SELECT DISTINCT ar.Name from Artist as ar
LEFT JOIN album on ar.ArtistId = Album.ArtistId
LEFT join Track T on Album.AlbumId = T.AlbumId
LEFT join Genre G on T.GenreId = G.GenreId
WHERE G.Name='{genre}' order by ar.Name""").fetchall()

for i in res:
    print(i[0])
