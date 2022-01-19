import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://sieg:885522@localhost:5432/py46_hw')
engine
connection = engine.connect()

res1 = connection.execute("""SELECT album_name, release_date FROM albums
                    WHERE release_date = 2018;""").fetchall()
pprint(res1)

longest = connection.execute("""SELECT MAX(duration) FROM tracks;""").fetchall()
res2 = connection.execute("""SELECT track_name, duration FROM tracks WHERE duration = %s;""", (longest)).fetchall()
pprint(res2)

res3 = connection.execute("""SELECT track_name FROM tracks WHERE duration >= 210;""").fetchall()
pprint(res3)

res4 = connection.execute("""SELECT collection_name FROM collections WHERE release_date BETWEEN 2018 AND 2020;""").fetchall()
pprint(res4)

res5 = connection.execute("""SELECT artist_name FROM artists WHERE artist_name NOT LIKE '%% %%';""").fetchall()
pprint(res5)

res6 = connection.execute("""SELECT track_name FROM tracks 
        WHERE track_name iLIKE '%%my%%' OR track_name iLIKE '%%мой%%';""").fetchall()
pprint(res6)
