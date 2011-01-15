import nltk
import MySQLdb

conn = MySQLdb.connect (host = "localhost", user = "imdb", db = "imdb")

cursor = conn.cursor()
sql = """show tables;"""
cursor.execute(sql)
results = cursor.fetchall()
raw_input("Press key to receive tables in imdb")

for x in results:
   print  x

raw_input("Finally. God damn this was annoying. ;)\n\n")

raw_input("Time to show columns... press key to continue\n")

sql = """show columns in title;"""
cursor.execute(sql)
results = cursor.fetchall()


for x in results:
   print  x

raw_input("\nNow trying to receive movie ID from The Big Lebrowski...!")	
sql = """SELECT id FROM title WHERE title = "The Big Lebowski";"""
cursor.execute(sql)
results = cursor.fetchall()

for x in results:
   print  x

raw_input("\nLastly, trying to receive associated keywords with The Big Lebwoski")	
sql = """SELECT kw.keyword  FROM keyword kw, movie_keyword mk
WHERE mk.movie_id = 517746 AND mk.keyword_id = kw.id"""
cursor.execute(sql)
results = cursor.fetchall()
print results
raw_input("Finally. ;)")
exit()
