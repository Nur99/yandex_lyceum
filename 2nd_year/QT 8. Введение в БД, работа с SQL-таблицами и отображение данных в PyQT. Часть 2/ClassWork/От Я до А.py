import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    res = cur.execute("""DELETE from Films WHERE title LIKE 'Я%а'""").fetchall()
    con.commit()
    con.close()