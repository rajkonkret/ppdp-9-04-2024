# hermetyzacja - zabezpieczenie pół przed dostepem z zewnątrz
# enkapsulacja - wystawienie dedykowanych metod do odczytu i zapisu pól
class Car:
    """
    Klasa opsijąca samochód w pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car1 = Car("Ford Mustang", 1956)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# po oznaczeniu pola jako prywatne __predkosc, nie madostepu do tego pola z zewnątrz
# print(car1.__predkosc)  # 50
car1.licznik()  # Prędkość wynosi 50 km/h
car1.__predkosc = 0  # dodalismy pole o nazwie __predkosc ale jako globalne (publiczne)
print("------")
car1.licznik()
# Prędkość wynosi 50 km/h
# ------
# Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 10 km/h
print(car1.__predkosc)  # 0
