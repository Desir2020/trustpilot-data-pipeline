import sqlite3
from pathlib import Path

db_dir = Path(__file__).parent 

def create_database():
    try: 
        con = sqlite3.connect(db_dir/"Truspilot_Reviews.db")

        cur = con.cursor() 

        cur.execute("CREATE TABLE IF NOT EXISTS Reviews(id INTEGER PRIMARY KEY AUTOINCREMENT, company_name TEXT NOT NULL, author_name TEXT NOT NULL, title TEXT, rating INTEGER NOT NULL, description TEXT, reviewed_at TEXT NOT NULL)")

        con.commit()

        con.close()
    except sqlite3.Error as e:
        raise ValueError(f"Erreur : {e}")
    

if __name__ == "__main__":
    create_database()
