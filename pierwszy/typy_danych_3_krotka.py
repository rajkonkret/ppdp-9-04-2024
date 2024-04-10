# krotka - niezmienna kolekcja
# krotka jednoelementowa - stała - zmienna niezmienna - zajmuje jeden element w pamieci czyli tak samo jak zmienna

temp = 36, 6
print(temp)  # (36, 6)
print(type(temp))  # <class 'tuple'>

tupla = "radek"
print(type(tupla))  # <class 'str'>
tupla2 = ("radek")
print(type(tupla2))  # <class 'str'>
tupla3 = "radek",
print(type(tupla3))
print(tupla3)  # ('radek',)
tupla4 = ("Radek",)
print(type(tupla4))  # PEP8 zaleca umieszczac jednoelementową tuple w nawiasie
print(tupla4)  # ('Radek',)
print(tupla4[0])
# print(tupla4[1])  # IndexError: tuple index out of range

tupla_names = "Radek", "Tomek", "Zenek", "Bartek"
print(type(tupla_names))  # <class 'tuple'>
print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Bartek')

tupla_names_2 = ("Radek", "Tomek", "Zenek", "Bartek")
print(tupla_names_2)
print(type(tupla_names_2))
# ('Radek', 'Tomek', 'Zenek', 'Bartek')
# <class 'tuple'>

# tuple są immutable
print(temp[0])  # 36
# temp[0] = 1  # TypeError: 'tuple' object does not support item assignment
#  usunięcie jedego elementu z krotki - nie ma możliwości
# del temp[0]  # TypeError: 'tuple' object doesn't support item deletion,
del temp  # usunięcie całej krotki
# cała krotka została usunięta, nie można już jej wypisac
# print(temp)  # NameError: name 'temp' is not defined

print(tupla_names[0])
print(tupla_names[1:3])
print(tupla_names[:3])
print(tupla_names[2:])
# Radek
# ('Tomek', 'Zenek')
# ('Radek', 'Tomek', 'Zenek')
# ('Zenek', 'Bartek')
print(tupla_names[-1])  # Bartek
print(tupla_names[:])  # wypisanie całej listy ('Radek', 'Tomek', 'Zenek', 'Bartek')

print("Radek" in tupla_names)  # True

print(tupla_names.count("Tomek"))  # 1 - występuje raz
print(tupla_names.index("Tomek"))  # 1 - ma indeks 1

# sortowanie
# sortowanie tupli zwraca nową listę !!!
print(sorted(tupla_names))  # ['Bartek', 'Radek', 'Tomek', 'Zenek']
print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Bartek')
print(sorted(tupla_names, reverse=True))  # ['Zenek', 'Tomek', 'Radek', 'Bartek']

# rozpakowanie krotki (tupli)
a, b = 1, 2
print(a, b)  # a=1, b=2
print(type((1, 2)))  # <class 'tuple'>

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3  # * worek na pozostałe dane
print("a=", a)
print("b=", b)
# a= 1
# b= [2, 3]

*a, b = 1, 2, 3
print("a=", a)
print("b=", b)
# a= [1, 2]
# b= 3
# ('Radek', 'Tomek', 'Zenek', 'Bartek')
imie1, *imie2, imie3 = tupla_names
# "Radek", ['Tomek', 'Zenek'],"Bartek"
print(imie1)  # Radek
print(imie2)  # ['Tomek', 'Zenek']
print(imie3)  # Bartek

# wypisac inne mozliwosci wstawienia gwiazdki

*imie1, imie2, imie3 = tupla_names
print(imie1)  # ['Radek', 'Tomek']
print(imie2)  # Zenek
print(imie3)  # Bartek

imie1, imie2, *imie3 = tupla_names
print(imie1)  # Radek
print(imie2)  # Tomek
print(imie3)  # ['Zenek', 'Bartek']

lista = list(tupla_names)  # rzutowanie krotki na liste
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Bartek']
print(type(lista))  # <class 'list'>
print(len(tupla_names))  # 4 długośc tupli
