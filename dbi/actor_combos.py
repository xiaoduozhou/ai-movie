import nltk
import MySQLdb

conn = MySQLdb.connect (host = "localhost", user = "imdb", db = "imdb")

cursor = conn.cursor()
foo = "\"Jackson, Samuel L.\""
bar = "\"Travolta, John\""
sq = """SELECT t.title FROM title t, cast_info ci, name n WHERE t.id = ci.movie_id AND ci.person_id = n.id AND n.name = """ + foo + """ AND t.id = ci.movie_id AND ci.person_id = n.id AND n.name = """ + bar + """ """
sql = sq
print sql


cursor.execute(sql)
results = cursor.fetchall()
raw_input ("Press key to do shit")

for x in results:
	print x