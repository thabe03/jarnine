import sqlite3
conn = sqlite3.connect('annonce.db',check_same_thread=False)
cursor = conn.cursor()

def lire():
  cursor.execute("SELECT * FROM batisse")
  row = cursor.fetchall()
  return row