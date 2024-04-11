# funkcja lambda - skrócony zapis funkcji

def odejmij(a, b):
    return a - b


print(odejmij(6, 8))

odejmij_2 = lambda a, b: a - b  # lambda zwraca wartość funkcji
print(odejmij_2(7, 3))  # 4

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
# -2
# 4
# 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))
print(wiek(10))
# dziecko
# nastolatek
print(wiek(17))
print(wiek(18))
# nastolatek
# dorosły
print(wiek(25))  # dorosły

lista = [1, 2, 3, 4, 24, 50, 100, 500]

l = []
for i in lista:
    l.append(i * 2)
print(l)

print([i * 2 for i in lista])


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)

# [2, 4, 6, 8, 48, 100, 200, 1000]
# [2, 4, 6, 8, 48, 100, 200, 1000]
# [2, 4, 6, 8, 48, 100, 200, 1000]

# funkcje wyższego rzędu

# map() - pobiera element, wykonuja na nim działanie zadane funkcją
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 48, 100, 200, 1000]

# zastosowanie labmbda jako funkcja anonimowa ( nie przypisujemy do zmiennej, nie nadajemy nazwy)
# wykonywana jest w miejscu deklaracji
print(f"Zastosowanie map(): {list(map(lambda x: x * 3, lista))}")
# Zastosowanie map(): [3, 6, 9, 12, 72, 150, 300, 1500]
print(f"Zastosowanie map(): {list(map(lambda x: x * 8, lista))}")
# Zastosowanie map(): [8, 16, 24, 32, 192, 400, 800, 4000]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)  # [1, 2]

# filter() - pobiera elemnt, sprawdza warunek, zwraca gdy spełnia
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter: [1, 2]
# zrobic filter dla x > 50
# dla x > 20
# dla x > 3 a mniejszego od  40
print(f"Zastosowanie filter: {list(filter(lambda x: x > 50, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x > 20, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x > 3 and x < 40, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 40, lista))}")
# Zastosowanie filter: [100, 500]
# Zastosowanie filter: [24, 50, 100, 500]
# Zastosowanie filter: [4, 24]
# Zastosowanie filter: [4, 24]
