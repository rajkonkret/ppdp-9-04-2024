# funkcje - wydzielony fragment kodu, można wykonać w dowolnej chwili, można wykonac wielokrotnie
# funkcja musi byc zadeklarowana wcześnij niz bedzie użyta
# w miejscu deklaracji funkcja nie wykonuje się

a = 8
b = 9


# deklaracja funkcji - funkcja sie nie wykonuje tutaj
def dodaj():  # funkcja bez argumentów, przyjęła wartości globalne
    print(a + b)


def dodaj2(a, b):  # deklarujemy dwa obowiązkowe argumenty
    print(a + b)  # a, b - lokalne


# można tworzyć funkcje z argumentami o wartości domyślnej
# pozwala to zasymulowac przeciązanie argumentów funkcji (liczbę argumentów)
def odejmij(a, b, c=0):
    print(a - b - c)


# uruchomienie funkcji -> nazwa funkcji i nawiasy ()
dodaj()
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(7, 8)  # 15
odejmij(9, 3)
odejmij(9, 3, 5)  # przekazywanie argumentów po pozycji
odejmij(b=9, c=8, a=0)  # -17, argumenty podane po nazwie
odejmij(5, c=9, b=6)  # mieszany, argumenty pozycyjne na początku
print(dodaj())  # None, funkcja nic nie zwraca
# print(dodaj() + dodaj2(8, 5))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
