import nltk
import MySQLdb

conn = MySQLdb.connect (host = "localhost", user = "imdb", db = "imdb")

cursor = conn.cursor()
foo = raw_input ("Enter movie title: ")
foo = "\"" + foo + "\""
sq = """SELECT n.name FROM name n, cast_info ci, title t WHERE n.id = ci.person_id AND ci.movie_id = t.id AND t.title = """ + foo + """ """
sql = sq
cursor.execute(sql)
results = cursor.fetchall()


for x in results:
	print x