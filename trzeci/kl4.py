# zrobic klasę Dom
# dodac dokumentacje
# metraz, kolor, liczba_okien
# pola prywatne
# metody do zapisu i odczytu tych pol
class Dom:
    """
    Klasa opisująca Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def mam_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def mam_metraz(self):
        print(f"Mam metraż {self.__metraz}")

    def mam_okna(self):
        print(f"Mam {self.__liczba_okien} okna/okien")

    def zmien_kolor(self):
        odp = input("Podaj nowy kolor")
        self.__kolor = odp
        self.mam_kolor()
        self.__farba()

    def zmien_metraz(self):
        odp = int(input("Podaj nowy metraż"))
        self.__metraz = odp
        self.mam_metraz()

    def zmien_okna(self):
        odp = int(input("Podaj liczbę okien"))
        self.__liczba_okien = odp
        self.mam_okna()  # wywolanie metody mam_okna()

    def __farba(self):  # metoda prywatna
        print("Brakło farby...")


dom1 = Dom(500, "czerwony", 56)
dom1.mam_metraz()  # Mam metraż 500
dom1.zmien_kolor()
