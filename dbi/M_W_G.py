import nltk
import MySQLdb

conn = MySQLdb.connect (host = "localhost", user = "imdb", db = "imdb")

cursor = conn.cursor()

foo = "\"Action\""
sq = """SELECT t.title FROM title t, movie_info mi WHERE t.kind_id = "1" AND mi.movie_id = t.id AND mi.info_type_id = 3 AND mi.info = """ + foo + """ """


sql = sq
print sql

cursor.execute(sql)
results = set(cursor.fetchall())

for x in results:
	print x
