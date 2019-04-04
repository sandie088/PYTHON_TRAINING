import psycopg2

conn = psycopg2.connect(database="dvdrental", user="postgres", password="admin", host="127.0.0.1", port="5432")
dbcursor = conn.cursor()
dbcursor.execute("Select * from category")
for row in dbcursor:
    print(row)
