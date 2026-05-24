import sqlite3
from pathlib import Path
import logging 

db_dir = Path(__file__).parent 

def create_database():
    try: 
        con = sqlite3.connect(db_dir/"Truspilot_Reviews.db")

        cur = con.cursor() 

        cur.execute("CREATE TABLE IF NOT EXISTS Reviews(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, title TEXT, stars INTEGER NOT NULL, description TEXT, date TEXT NOT NULL)")

        con.commit()

        con.close()
    except sqlite3.Error as e:
        logging.error(f"Erreur : {e}")



    

if __name__ == "__main__":
    create_database()
