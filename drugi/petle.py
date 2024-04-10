# petle
# for - petla iteracyjna

for i in range(10):  # 0..9
    print(i)

for i in range(1, 10):  # 1..9
    print(i)

my_string = "Radek"
for i in my_string:
    print(i)

for i in range(10):
    pass

for _ in range(4):  # niema zmienna
    print("Radek")
    print(_)
# Radek
# 0
# Radek
# 1
# Radek
# 2
# Radek
# 3

for i in range(10):
    if i % 2 == 0:  # modulo 2, czyli parzyste - reszta 0, nieparzyste reszta 1
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:
    print(c)
    if c == 2:
        c += 1  # c = c +1
        print("Tylko wypisze 3", c)
    print("Wypisze wszystkie", c)
print("Wypisze ostatni", c)
# 0
# Wypisze wszystkie 0
# 2
# Tylko wypisze 3 3
# Wypisze wszystkie 3
# 4
# Wypisze wszystkie 4
# 6
# Wypisze wszystkie 6
# 8
# Wypisze wszystkie 8
# Wypisze ostatni 8

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']
for p in imiona:
    print(p)
# wypisac ta liste w postaci
# 0 Radek
# 1 Asia

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin

for i in range(len(imiona)):  # range(4) 4 długosc listy, indeksy 0..3
    print(i, imiona[i])
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin

# enumerate() - zwraca ponumerowane elementy
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Asia')
# (2, 'Zbyszek')
# (3, 'Marcin')
p = (3, 'Marcin')
i, o = p
print(i, o)
for p, o in enumerate(imiona):
    print(p, o)
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin
for p, o in enumerate(imiona, start=1):  # start=1 - zaczynamy numerować od 1
    print(p, o)
# 1 Radek
# 2 Asia
# 3 Zbyszek
# 4 Marcin
#   sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
print(1, 2, 3, 4, 5, sep=";")  # 1;2;3;4;5
print("Radek", end=" ")
print("Tomek")  # Radek Tomek
print("Tobiasz")
# 1;2;3;4;5
# Radek Tomek
# Tobiasz
print("Radek", "Tomek", sep="\n")
# Radek
# Tomek

# ludzie = ["Radek", 'Janek', "Tomek", "Marek"]
wiek = [45, 56, 34, 32]
# IndexError: list index out of range dla róznych długości list błąd w klasycznym podejsciu
ludzie = ["Radek", 'Janek', "Tomek", "Marek", "Magda"]  # IndexError: list index out of range

# Radek 45
# for x in range(len(ludzie)):
#     print(ludzie[x], wiek[x])

# zip() - łaczy kolekcje w jedną
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 45)
# ('Janek', 56)
# ('Tomek', 34)
# ('Marek', 32)

for p, w in zip(ludzie, wiek):
    print(p, w)
# Radek 45
# Janek 56
# Tomek 34
# Marek 32

# 0 Radek 45
for i in enumerate(zip(ludzie, wiek)):
    print(i)  # (0, ('Radek', 45))

# # ValueError: not enough values to unpack (expected 3, got 2)
# for i, j, k in enumerate(zip(ludzie, wiek)):
#     print(i, j, k)
a, b = (0, ('Radek', 45))
print("a=", a)
print("b=", b)
# a= 0
# b= ('Radek', 45)
c, d = b
print("c:", c)
print("d:", d)
# c: Radek
# d: 45
print(a, c, d)
for a, (c, d) in enumerate(zip(ludzie, wiek)):
    print(a, c, d)
# 0 Radek 45
# 1 Janek 56
# 2 Tomek 34
# 3 Marek 32

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(10, 0, -2):  # krok do tyłu
    print(i)
# 10
# 8
# 6
# 4
# 2
parzyste = [i for i in range(0, 10, 2)]
print(parzyste)  # [0, 2, 4, 6, 8]
