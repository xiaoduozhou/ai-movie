import nltk
import MySQLdb

conn = MySQLdb.connect (host = "localhost", user = "imdb", db = "imdb")

cursor = conn.cursor()
#sql="""SELECT n.name FROM name n, cast_info ci, title t WHERE n.id = ci.person_id AND ci.movie_id = t.id AND t.title = "Snakes on a Plane" """
sql=""" FROM name n, cast_info ci, SELECT n.name, title t WHERE n.id = ci.person_id AND ci.movie_id = t.id AND t.title = "Snakes on a Plane" """
cursor.execute(sql)
results = cursor.fetchall()
raw_input ("Press key to do shit")

for x in results:
	print x