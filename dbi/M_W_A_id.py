import nltk
import MySQLdb

conn = MySQLdb.connect (host = "localhost", user = "imdb", db = "imdb")

cursor = conn.cursor()
foo = "\"371934\""
sq = """SELECT t.id FROM title t, cast_info ci, name n WHERE ci.role_id = "1" AND t.kind_id = "1" AND t.id = ci.movie_id AND ci.person_id = n.id AND n.id = """ + foo + """ """
sql = sq
print sql
sq2 = """SELECT t.id FROM title t, cast_info ci, name n WHERE ci.role_id = "2" AND t.kind_id = "1" AND t.id = ci.movie_id AND ci.person_id = n.id AND n.id = """ + foo + """ """
sql2 = sq2
print sql2
cursor.execute(sql)
results = set(cursor.fetchall())
cursor.execute(sql2)
results2 = set(cursor.fetchall())

inter = results.union(results2)

for x in inter:
	print x