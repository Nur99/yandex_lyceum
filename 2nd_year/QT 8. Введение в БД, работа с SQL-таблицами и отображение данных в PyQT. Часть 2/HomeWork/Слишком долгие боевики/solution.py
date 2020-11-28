import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("""DELETE FROM films WHERE duration >=90 AND genre = (SELECT id FROM genres WHERE title = 'боевик')""")
    con.commit()
    con.close()
