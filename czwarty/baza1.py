# bazy danych
# sql, nosql
# sqlite3 - baza danych w jednym pliku lub pamięci
import sqlite3

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print("Baza danych została podłaczona")
except sqlite3.Error as e:
    print("Bład połączenia z bazą", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")

# Baza danych została podłaczona
# Połaczenie zostało zamknięte