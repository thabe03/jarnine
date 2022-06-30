import sqlite3
import time
conn = sqlite3.connect('annonce.db')
cursor = conn.cursor()

def suppr(id):
  cursor.execute("SELECT * FROM batisse WHERE id="+str(id))
  userChoice = cursor.fetchone()
  if userChoice == None:
    return 0
  else:
    try:
      cursor.execute("DELETE FROM batisse WHERE id="+str(id))
      conn.commit()
      return 202
    except Exception:
        return 404