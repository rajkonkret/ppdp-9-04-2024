class Human:
    """
    Kalsa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca dla klasy Human (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):  # self - obiekt, który wywołuje funkcję
        print(f"Nazywam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Mam {self.wzrost} cm wzrostu ")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Anna", 28, 170)
print(cz1.plec)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.imie)
# k
# 28
# 170
# Anna
# dopisac metode powitanie()
# dopisac metode wypisz_wiek()
cz1.powitanie()
cz1.wypisz_wiek()
# Nazywam się Anna
# Mam 170 cm wzrostu

cz2 = Human("Radek", 45, 190, "m")
cz2.powitanie()
cz2.wypisz_wiek()
# Nazywam się Radek
# Mam 190 cm wzrostu

cz1.ruszaj()  # Ruszyłam w drogę
cz2.ruszaj()  # Ruszyłem w drogę
