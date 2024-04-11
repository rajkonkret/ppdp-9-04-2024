# funkcja obliczająca średnią np.: ocen
def liczby(name=None, *cyfry):  # * przyjmuje argumenty pozycyjne
    print(cyfry)  # (1, 2, 3, 4, 5) - krotka
    count = len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Błąd", e)
    else:
        print(f"Uczeń {name}, Srednia wynosi {avg}")
    finally:
        print("Koniec obliczenia")


liczby()
liczby("Radek", 1, 2, 3, 4, 5)
liczby("Tomek", 1, 2, 3, 4, 5, 6, 7, 8, 9)
# ()
# Błąd division by zero
# Koniec obliczenia
# (1, 2, 3, 4, 5)
# Uczeń Radek, Srednia wynosi 3.0
# Koniec obliczenia
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Uczeń Tomek, Srednia wynosi 5.0
# Koniec obliczenia
# rozpakowanie
name, *cyfry = ("Tomek", 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Name:", name)
print("Cyfry:", cyfry)
# Name: Tomek
# Cyfry: [1, 2, 3, 4, 5, 6, 7, 8, 9]
