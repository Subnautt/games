import sqlite3
from config import DATABASE
con = sqlite3.connect("games.db") 

cur = con.cursor()
cur.execute("CREATE TABLE game(Название, Год выхода, Оценки критиков)")
cur.execute("""
    INSERT INTO game VALUES
        ('Subnautica, 2018, 89),
        (')
""")
con.commit()

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)
con.close()
