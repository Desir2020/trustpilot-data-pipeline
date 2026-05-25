import sqlite3
from pathlib import Path

db_file= Path(__file__).parent.parent / "database" / "Truspilot_Reviews.db"

def connect_db():
    try:
        con = sqlite3.connect(db_file)
        return con

  

    except sqlite3.Error as e:
        raise ValueError(f"Erreur de connexion:  {e}")
    
def load_reviews(tuples_list):
        try:
            con = connect_db()
            
            cursor= con.cursor()

            cursor.executemany("""
                INSERT INTO Reviews(
                        company_name,
                        author_name,
                        title,
                        rating,
                        description,
                        reviewed_at
                        ) 
                        VALUES (
                        ?, ?, ?,
                        ?, ?, ?
                        ) 
                """,
                
                    tuples_list
                )
            
            con.commit()
            cursor.close()
            con.close()

        except sqlite3.Error as e:
             raise ValueError(f"Echec: {e}")

if __name__ == "__main__":
     con = connect_db()
     cursor = con.execute("""SELECT COUNT(*) FROM reviews""")

     for row in cursor.fetchall():
          print(row)

     
     