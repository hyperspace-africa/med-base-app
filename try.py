import sqlite3 as sql

db = sql.connect('database.db')

db.row_factory = sql.Row

cursor = db.execute("SELECT COUNT(first_name), last_name FROM patients")

for row in cursor:
    print(dict(row))