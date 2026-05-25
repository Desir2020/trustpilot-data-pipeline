import sqlite3
from pathlib import Path

db_file= Path(__file__).parent.parent / "database" / "Truspilot_Reviews.db"
    
def load_reviews(tuples_list):
        try:
            with sqlite3.connect(db_file) as connection:
                connection.executemany("""
                    INSERT OR IGNORE INTO Reviews(
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

        except sqlite3.Error as e:
             raise ValueError(f"Echec: {e}")

if __name__ == "__main__":
     con = sqlite3.connect(db_file)
     cursor = con.execute("""SELECT COUNT(*) FROM reviews""")

     for row in cursor.fetchall():
          print(row)

     
     