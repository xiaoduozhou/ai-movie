import nltk
import MySQLdb

conn = MySQLdb.connect (host = "localhost", user = "imdb", db = "imdb")

cursor = conn.cursor()
foo = "\"Nicholson, Jack\""
bar = "\"institution\""
sq = """SELECT t.title FROM title t, movie_keyword mk, keyword k WHERE t.id = mk.movie_id AND k.keyword = """ + bar + """ AND mk.keyword_id = k.id """

sql = sq
print sql


cursor.execute(sql)
results = cursor.fetchall()
raw_input ("Press key to do shit")


for x in results:
	print x
