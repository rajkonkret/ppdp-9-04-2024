# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):  # kolejnośc ma znaczenie
    """
    klasa dziedziczy po klasie B i A
    """


class D(A, B):
    """
    Klasa dziedziczy po kalsie A i B
    """

    def method(self):
        super().method()  # wywołanie metody z klasy wyzszej


class E(B, A):
    def method(self):
        print("Metoda z klasy E")  # nadpisujemy metodę


class G(A, B):
    def method(self):
        B.method(self)  # wskazanie, ze chcemy uzyc metody z klasy B


class H(A, B):
    def method(self):
        super().method()  # uzycie z klasy wyzszej czyli A
        B.method(self)  # wskazanie uzycia z klasy B
        print("Metoda z klasy H")  # dopisanie w klasie H


a = A()
a.method()  # Metoda z klasy A

b = B()
b.method()  # Metoda z klasy B

c = C()
c.method()  # Metoda z klasy B
print(C.__mro__)
# , <class '__main__.B'(<class '__main__.C'>>, <class '__main__.A'>, <class 'object'>)

d = D()
d.method()  # Metoda z klasy A

e = E()
e.method()  # Metoda z klasy E

g = G()
g.method()  # Metoda z klasy B

h = H()
h.method()
# Metoda z klasy A
# Metoda z klasy B
# Metoda z klasy H
print(H.__mro__)
# (<class '__main__.H'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
