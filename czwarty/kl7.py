# abstrakcja
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstrakcyjna, dekorator
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, 'Ja nie latam')

    def wydaj_odglos(self):
        print("Ko ko ko ko ko")


class Orzel(Ptak):
    """
    Klasa orzel
    """

    def wydaj_odglos(self):
        print("Kier kieeer kir")


# TypeError: Can't instantiate abstract class Sowa
# without an implementation for abstract method 'wydaj_odglos'
class Sowa(Ptak):
    """
    Klasa Sowa
    """


# po oznaczeniu klasy Ptak jako abstrakcyjnej
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzel", 45)
# or1.latam()  # Tu Orzel Lecę z szybkością 45
# or1.wydaj_odglos()  # niemy
#
# ku1 = Ptak("Kura", 0)
# ku1.latam()  # Tu Kura Lecę z szybkością 0
# ku1.wydaj_odglos()

ku2 = Kura("Kura domowa")
ku2.latam()  # Tu Kura domowa Ja nie latam
ku2.wydaj_odglos()
# Tu Kura domowa Ja nie latam
# Ko ko ko ko ko

or2 = Orzel("Orzel", 50)
or2.latam()
or2.wydaj_odglos()
# Tu Orzel Lecę z szybkością 50
# Kier kieeer kir

# nie mozemy stworzy c obiektu Sowa, ponieważ nie nadpisuje metody wydaj_odglos()
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sow = Sowa("Sowa", 5)
