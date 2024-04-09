tekst = "Witaj świecie"
print(tekst)
print(type(tekst))
# Witaj świecie
# <class 'str'>
tekst.upper()  # """ Return a copy of the string converted to uppercase. """
# zwraca nowy string ze zmianami, nie zmienia oryginału
print(tekst)  # Witaj świecie
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_2 = tekst.upper()
print(tekst_2)  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie

# lower()
print(tekst.lower())  # witaj świecie
tekst_3 = tekst.lower()  # witaj świecie
print(tekst_3)  # witaj świecie

print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst.removeprefix("Witaj"))  # " świecie"

encoded_s = tekst.encode("utf-8")
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
# b =- postac bajtowa
# \xc5 - liczba w sytemie szesnastkowym
print(type(encoded_s))  # <class 'bytes'> typ binarny/bajtowy
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))
# 0 - pierwszy index (pierwszy element)
# 4 - indeks końca, ale ta metoda nie bierze osattniego pod uwage, czyli wyswietla tak naprawdę do 4-1 = 3
# Witaj
# 01234
print(tekst.count("j", 0, 4))  # 0 bo j na piątym miejscu(indeks 4) zbiór otwarty z prawej strony
print(tekst.count("j", 5, 9))  # 0  - indeksy 5678 -> 9 juz nie
print(tekst)  # Witaj świecie
# teksty w pytone są immutable (niezmienne)

imie = "Radek"
tekst_format = f"\tMam na imię {imie}\n i lubie Pytona.\b Dodatkowe zdanie."
print(tekst_format)
# "    Mam na imię Radek
#  i lubie Pytona Dodatkowe zdanie."
# \n - nowa linia
# \t - tabulator
# \b - backspace
# f - fstring - formated string - tekst sformatowany

starszy = "Witaj %s!"  # %s - oczekuje stringa
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!

# tekst wielolinijkowy
print("""
    Tekst wielolinijkowy
    dodakowe dane
    """)
#     Tekst wielolinijkowy
#     dodakowe dane
''' komentarz
wielolinijkowy'''
