a = 10
b = 10


def dodaj():
    a = 6  # zmienne lokalne
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # zmienna globalna
    a = 8  # zmieniamy wartość zmiennej globalnej !!!
    b = 9
    print(a + b)


print("Wartośc a z góry (globalna)", a)  # Wartośc a z góry (globalna) 10
dodaj()  # 13
print("Wartośc a z góry (globalna)", a)  # Wartośc a z góry (globalna) 10
dodaj2()  # 20
print("Wartośc a z góry (globalna)", a)  # Wartośc a z góry (globalna) 10
dodaj3()  # 17
print("Wartośc a z góry (globalna)", a)  # Wartośc a z góry (globalna) 8
dodaj2()  # 18
print("Wartośc a z góry (globalna)", a)  # Wartośc a z góry (globalna) 8
