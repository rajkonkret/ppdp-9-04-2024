# funkcje zwracające wynik
def dodaj(a, b):
    return a + b  # return - zwróc wynik


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


dodaj(4, 5)  # nie ma po drodze print, wynik się nie wyświetli
print(dodaj(4, 5))  # 9
wyn = dodaj(6, 9)
print(f'Wynik: {wyn}')  # Wynik: 15
print(odejmij())
print(odejmij(1))
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
print(odejmij(b=9, c=9))
print(odejmij(c=9, b=0, a=6))

# print(odejmij(1, 2, 3, 4))  # TypeError: odejmij() takes from 0 to 3 positional arguments but 4 were given
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, cena=8000))
# 1230.0
# 1080.0
# 9200.0

print(dodaj(7, 8) + oblicz_vat(1000))  # 1245.0

zm = oblicz_vat(1000)
print(zm)  # 1230.0
print(type(zm))  # <class 'float'>
if zm == 1230:
    print("OK")
