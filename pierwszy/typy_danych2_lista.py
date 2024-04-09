# lista - kolekcja przechowujaca dowolną ilość danych, dowolnego typu na raz
# zachowuje kolejność przy dodawaniu elementów

lista = []  # pusta lista
print(type(lista))
print(lista)
# <class 'list'>
# [] - pusta lista

# append() - dodawanie elemntów na końcu listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marek")

print("Lista osób co zdały egzamin:", lista)
# Lista osób co zdały egzamin: ['Radek', 'Tomek', 'Zenek', 'Marek']
#                                 0          1       2        3
#                                  -4        -3      -2       -1
print(len(lista))  # ilość elemntów w liście: 4
print(lista[0])
print(lista[2])
print(lista[3])
# print(lista[4])  # IndexError: list index out of range

#
# Radek
# Zenek
# Marek
print(lista[-1])  # Marek
print(lista[-2])  # Marek
print(lista[-3])  # Marek

# slicowanie listy ( wyswietlanie części listy)
print(lista[0:3])  # 0,1,2  ['Radek', 'Tomek', 'Zenek'] - z prawej zbiór otwarty
print(lista[:3])
print(lista[3:9])  # ['Marek']
print(lista[10:12])  # []

print(lista[-3:1])  # []
print(lista[-1:2])
print(lista[-4:2])  # ['Radek', 'Tomek']
print(lista[0:-2])  # ['Radek', 'Tomek']

print(lista[0:])  # ['Radek', 'Tomek', 'Zenek', 'Marek']
print(lista[0:len(lista)])  # ['Radek', 'Tomek', 'Zenek', 'Marek']
print(lista[0:len(lista) - 1])  # ['Radek', 'Tomek', 'Zenek']

print(lista[0:5:2])  # ['Radek', 'Zenek'] start:stop:krok
print(lista[0::2])
print(lista[::2])  # ['Radek', 'Zenek']
print(lista[::-1])  # odwrócenie listy, ['Marek', 'Zenek', 'Tomek', 'Radek']

# nadpisanie elemntu w liscie
lista[2] = 'Mikołaj'
print(lista)  # ['Radek', 'Tomek', 'Mikołaj', 'Marek']

# dodanie elemntu we wskazanym miejscu
lista.insert(1, "Katarzyna")
print(lista)  # ['Radek', 'Katarzyna', 'Tomek', 'Mikołaj', 'Marek']

# usunięcie elemntu z listy
lista.remove("Mikołaj")
print(lista)

# lista.remove("Zenek")  # ValueError: list.remove(x): x not in list
lista.append("Zenek")
lista.append("Zenek")
print(lista)  # ['Radek', 'Katarzyna', 'Tomek', 'Marek', 'Zenek', 'Zenek']
# print(lista.remove("Zenek")) # None
lista.remove("Zenek")
print(lista)  # ['Radek', 'Katarzyna', 'Tomek', 'Marek', 'Zenek']

print("Zenek" in lista)  # True

# sprawdzenie indeksu dla elemntu
indeks = lista.index("Zenek")
print(indeks)  # 4

# usunięcie elementu po indeksie
print(lista.pop(indeks))  # Zenek - zwraca element usunięty
print(lista)  # ['Radek', 'Katarzyna', 'Tomek', 'Marek']
print(lista.pop())  # usunie ostatni element z listy -> Marek
print(lista)  # ['Radek', 'Katarzyna', 'Tomek']

a = 1
b = 3
a = b
print(a)  # 3
print(b)  # 3
b = 7
print(a)  # 3
print(b)  # 7

lista2 = lista  # kopiowanie referencji (adresu w pamięci)
lista3 = lista.copy()  # kopia elementów listy do nowej listy
lista.clear()  # czyszczenie elemntów listy
print(lista2)  # []
print(lista)  # []
print(id(lista2))  # 2793317716352
print(id(lista))  # 2793317716352
print(lista3)
print(id(lista3))  # 2236064118400

liczby = [54, 999, 34, 22, 64.34, 687]
# liczby = [54, 999, 34, 22, 64.34, 687, "A"]  # TypeError: '<' not supported between instances of 'str' and 'float',
# nie zadziała sort()
print(liczby)  # [54, 999, 34, 22, 64.34, 687]
liczby.sort()
print(liczby)  # [22, 34, 54, 64.34, 687, 999]

lista_osoby = ["radek", "ola", "agata"]
lista_osoby.sort()
print(lista_osoby)  # ['agata', 'ola', 'radek']

lista_osoby.reverse()  # odwróćenie bez sortowania
print(lista_osoby)  # ['radek', 'ola', 'agata']
lista_osoby.sort(reverse=True)  # sortowanie i odwrócenie

liczby[3] = 6666
print(liczby)  # [22, 34, 54, 6666, 687, 999]
liczby.pop(3)  # 3 numer indeksu
print(liczby)  # [22, 34, 54, 687, 999]

liczby.remove(54)  # 54 - element a nie numer indeksu
print(liczby)  # [22, 34, 687, 999]

tekst = "Python"
lista1 = [tekst]
print(lista1)  # ['Python']

# rozpakowanie sekwencji
lista2 = list(tekst)  # list() - rzutowanie na liste
print(lista2)  # ['P', 'y', 't', 'h', 'o', 'n']

krotka = tuple(lista3)  # tuple() - rzutowanie na krotkę, tuple
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Radek', 'Katarzyna', 'Tomek')
