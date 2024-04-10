# set (zbiór) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # rzzutowanie na set()
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

zb2 = set()  # tworzenie pustego seta
print(zb2)  # set() - pusty set

# dodawanie elemntów do zbioru
zb2.add(2)
zb2.add(2)
zb2.add(2)
zb2.add(3)
zb2.add(3)
zb2.add(5)
zb2.add(5)
print(zb2)  # {2, 3, 5}

print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(27)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 27}

zb3 = set()
name = "Radek"
zb3.add(name)
print(zb3)  # {'Radek'}

# usunięcie elementu ze zbioru
zbior.remove(44)  # 44 - element
print(zbior)  # {33, 66, 777, 11, 18, 22, 55, 27}

# pop() - usnięcie pierwszego elementu ze zbioru
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 18, 22, 55, 27}
print(zbior.pop())  # 66
print(zbior)  # {777, 11, 18, 22, 55, 27}

print(sorted(zbior))  # sortowanie zwraca liste [11, 18, 22, 27, 55, 777]
print(zbior)  # {777, 11, 18, 22, 55, 27}

zbior2 = {667, 44, 18, 52, 55, 22, 687, 62, 999, 999}
print(zbior2)  # {999, 44, 687, 18, 52, 22, 55, 667, 62}
print(type(zbior2))  # <class 'set'>

zbior.add(17)
zbior2.add(17)

# działania na zbiorach
print(zbior | zbior2)  # suma zbiorów {777, 11, 17, 18, 22, 27, 667, 999, 44, 687, 52, 55, 62}
print(zbior.union(zbior2))  # {777, 11, 17, 18, 22, 27, 667, 999, 44, 687, 52, 55, 62}
# zbiory nie zostały zmodyfikowane
print(zbior)  # {777, 11, 17, 18, 22, 55, 27}
print(zbior2)  # {999, 44, 687, 17, 18, 52, 22, 55, 667, 62}

print(zbior & zbior2)  # częśc wspólna  {17, 18, 22, 55}

print(zbior - zbior2)  # {27, 777, 11}
print(zbior.difference(zbior2))  # {27, 777, 11}
print(zbior2.difference(zbior))  # {999, 44, 687, 52, 667, 62}
# {999, 44, 687, 17, 18, 52, 22, 55, 667, 62} - {777, 11, 17, 18, 22, 55, 27} = {999, 44, 687, 52, 667, 62}

zbior4 = zbior.copy()  # kopia elementów zbioru
print(zbior4)  # {17, 18, 22, 55, 27, 777, 11}
zbior.clear()
print(zbior4)  # {17, 18, 22, 55, 27, 777, 11}

print(len(zbior4))  # 7 elementów

lista = list(zbior4)
print(lista)  # [17, 18, 22, 55, 27, 777, 11]

# zbiór mieszany
zbior5 = {"A", 1, 2, 3}
print(zbior5)  # {1, 2, 3, 'A'}
