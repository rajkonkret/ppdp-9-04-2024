# dziedziczenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")

    def __repr__(self):  # metoda opisująca obiekt
        return f"Kolor: {self.kolor}"


class Samochod(Pojazd):  # klasa Samochod dziedziczy po klasie Pojazd
    """
    klasa Samochód
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)  # musimy wywołać konstruktor z klasy wyzszej
        self.marka = marka

    def info(self):
        super().info()  # możemy wywołac metodę z klasy wyzszej
        print(f"Marka: {self.marka}")

    def __repr__(self):  # metoda opisująca obiekt
        return f"Marka: {self.marka}, Kolor: {self.kolor}"


poj = Pojazd("czerwony")
poj.info()

sam = Samochod("niebieski", "Opel")
sam.info()
# Kolor: czerwony
# Kolor: niebieski
# Marka: Opel

lista = [poj, sam]
for i in lista:
    i.info()

# Kolor: czerwony
# Kolor: niebieski
# Marka: Opel

# polimorfizm - obiekty różnych klas
# dziedziczą cechy po wspolnej klasie i mozemy po tych wspolnych cechach traktowac je tak samo
for i in lista:
    print(i)

# bez __repr__
# <__main__.Pojazd object at 0x0000025F6990DCA0>
# <__main__.Samochod object at 0x0000025F6990DB20>
# po nadpisaniu __repr__
# Kolor: czerwony
# Marka: Opel, Kolor: niebieski
