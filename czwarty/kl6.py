# pracownik - imie, nazwisko, pensja
# manager - imie, nazwisko, pensja, premia
class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Mam na imię {self.imie} {self.nazwisko}")

    def oblicz_pensja(self):
        return self.pensja


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensja(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 10000)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensja()
print(f"Wynagradzenie dla {pracownik.imie} {pracownik.nazwisko} wynosi: {wyn_prac}")
# Mam na imię Jan Kowalski
# Wynagradzenie dla Jan Kowalski wynosi: 10000

menago = Manager("Anna", "Nowak", 15000, 3000)
menago.przedstaw_sie()
wyn_man = menago.oblicz_pensja()
print(f"wynagrodzenie dla {menago.imie} {menago.nazwisko} wynosi: {wyn_man}")
# Mam na imię Anna Nowak
# wynagrodzenie dla Anna Nowak wynosi: 18000
