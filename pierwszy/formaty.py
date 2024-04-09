user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # float - zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>
liczba = 1234567890123  # int
print(type(liczba))  # <class 'int'>

print("Witaj %s masz teraz %d lat." % (user, wiek))
# Witaj Tomek masz teraz 39 lat.
# w tym przypadku sprawdza typ danych
# print("Witaj %s masz teraz %d lat." % (wiek, user))  # TypeError: %d format: a real number is required, not str
# %s - string
# %d digit - liczba
print("Witaj %(user)s, masz teraz %(wiek)d lat" % {'user': user, 'wiek': wiek})
print("Witaj %(user)s, masz teraz %(age)d lat" % {'user': user, 'age': wiek})
# Witaj Tomek, masz teraz 39 lat
# Process finished with exit code 0 - program zakończony bez błedu

print(f"Witaj {user} masz teraz {wiek} lat.")
print(f"Witaj {wiek} masz teraz {user} lat.")
# Witaj Tomek masz teraz 39 lat.
# Witaj 39 masz teraz Tomek lat.
print("Witaj {} masz teraz {} lat.".format(user, wiek))
# Witaj Tomek masz teraz 39 lat.

print("Uzywamy wersji pythona %i" % 3)  # Uzywamy wersji pythona 3
print("Uzywamy wersji pythona %f" % 3.9)  # Uzywamy wersji pythona 3.900000
print("Uzywamy wersji pythona %.1f" % 3.9)  # Uzywamy wersji pythona 3.9
print("Uzywamy wersji pythona %.2f" % 3.9)  # Uzywamy wersji pythona 3.90
print("Uzywamy wersji pythona %.0f" % 3.9)  # Uzywamy wersji pythona 4 - zaokrągla, nie zmienia wartości zmiennej
print("Uzywamy wersji pythona %.f" % 3.9)  # Uzywamy wersji pythona 4 - zaokrągla, nie zmienia wartości zmiennej

print(f"Uzywamy wersji Python: {wersja}")  # Uzywamy wersji Python: 3.900001
print(f"Uzywamy wersji Python: {wersja:.1f}")  # Uzywamy wersji Python: 3.9
print(f"Uzywamy wersji Python: {wersja:.2f}")  # Uzywamy wersji Python: 3.90
print(f"Uzywamy wersji Python: {wersja:.0f}")  # Uzywamy wersji Python: 4

print(f"{user:>20}")  # "               Tomek"
print(f"{user:<25}")  # "Tomek                    "
print(f"{user:^30}")  # "            Tomek             "
print(f"{user:^3}")  # "Tomek"

print(liczba)  # 1234567890123
print("Nasza duża liczba {:,}".format(liczba))
# Nasza duża liczba 1,234,567,890,123
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))
# Nasza duża liczba 1.234.567.890.123
# Nasza duża liczba 1 234 567 890 123
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))
# Nasza duża liczba 1 234 567 890 123
