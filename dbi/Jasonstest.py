import nltk
import MySQLdb
import sets

conn = MySQLdb.connect (host = "localhost", user = "imdb", db = "imdb")

cursor = conn.cursor()
foo = "\"Jackson, Samuel L.\""
bar = "\"Travolta, John\""
sq = """SELECT t.title FROM title t, cast_info ci, name n WHERE t.id = ci.movie_id AND ci.person_id = n.id AND n.name = """ + foo + """ """

sql = sq
print sql

sq2 = """SELECT t.title FROM title t, cast_info ci, name n WHERE t.kind_id = "1" AND t.id = ci.movie_id AND ci.person_id = n.id AND n.name = """ + bar + """ """
sql2 = sq2

print sql2

cursor.execute(sql)
results = sets.Set(cursor.fetchall())
cursor.execute(sql2)
results2 = sets.Set(cursor.fetchall())
raw_input ("Press key to do shit")

inter = results.intersection(results2)

for x in inter:
	print x