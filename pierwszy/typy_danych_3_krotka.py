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
