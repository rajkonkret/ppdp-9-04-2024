# bazy danych
# sql, nosql
# sqlite3 - baza danych w jednym pliku lub pamięci
import sqlite3

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print("Baza danych została podłaczona")

    query = '''
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''

    insert = """
    INSERT INTO developers (id, name, email, salary) VALUES (1, 'Radek', 'r@r.pl',10000); 
    """
    select = """
    SELECT * FROM developers;
    """

    c.execute(query)
    conn.commit()

    # c.execute(insert)
    # conn.commit()

    for row in c.execute(select):
        print(row)  # (1, 'Radek', 'r@r.pl', None, 10000.0)

except sqlite3.Error as e:
    print("Bład połączenia z bazą", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")

# Baza danych została podłaczona
# Połaczenie zostało zamknięte
