# klasy - szablon, przepis
# pola
# funkcje
# obiekt  - instancja klasy, obiekt zbudowany wg przepisu czyli klasy

# deklaracji klasy - tu się nie wykonuje
class Human:
    """
    Klasa Human opisująca człowiek a w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):  # self - obiekt, który wywołuje funkcję
        print(f"Nazywam się {self.imie}")


print(Human.__doc__)  # wypisanie dokumentacji klasy
#     Klasa Human opisująca człowiek a w pythonie
print(print.__doc__)
# Prints the values to a stream, or to sys.stdout by default.
#
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.

# tworzenie obiektu klasy Human, uruchomienie klasy
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000002B6F6C41B80>
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# None
# k

# naddanie wartości polom obiektu
cz1.wiek = 56
cz1.imie = "Anna"

# odczytanie wartości pól obiektu
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Anna
# 56
# k

cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 57
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Radek
# 57
# m
cz1.powitanie()
cz2.powitanie()
# Nazywam się Anna
# Nazywam się Radek
