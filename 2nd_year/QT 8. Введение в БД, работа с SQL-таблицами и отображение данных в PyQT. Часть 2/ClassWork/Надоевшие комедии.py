import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    res = cur.execute("""DELETE from Films WHERE genre = (SELECT id FROM genres WHERE title='комедия')""").fetchall()
    con.commit()
    con.close()