import sys

wiek = 47
rok = 2024
temp = 36.6  # float
temp2 = 36, 6  # krotka - tupla

print(wiek)
print(type(wiek))

print(temp)
print(type(temp))
# 47
# <class 'int'>
# 36.6
# <class 'float'>

print(type(temp2))  # <class 'tuple'>

print(6 * "Radek")  # RadekRadekRadekRadekRadekRadek
print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # dzielenie -> wynik zawsze float
# 2071
# -1977
# 95128
# 0.023221343873517788
print(wiek // rok)  # 0 - część całkowita dzielenia
print(wiek % rok)  # 47 - reszta z dzielenia, modulo
print(10 % 3)  # reszta 1 bo 3 * 3 + 1 = 10
print(wiek ** rok)  # potęgowanie
print(len(str(wiek ** rok)))  # len() - długośc kolekcji, 3385

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0
print(0.1 + 0.5)  # 0.6
print(0.1 + 0.2)  # 0.30000000000000004
print(0.2 + 0.7)  # 0.8999999999999999
# liczby narażone na błąd zaokrąglenia
# x=SMB^{E} - s - znak, m - mantysa, b - base, e - wykładnik
# 1.4567 * 10 ^ 5
# 1.2345 * 2 ^ 3
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")
print(f"""
{temp}
    {wiek}""")
# "Sprawdzenie zmiennej 36.6 47
#
# 36.6
#     47"

wyn = 0.2 + 0.7
print(f"Wynik: {wyn:.2f}")  # Wynik: 0.90
print(f"Wynik: {wyn}")  # Wynik: 0.8999999999999999

# typ logiczny
# True, False
czy_znasz_python = True
print(czy_znasz_python)  # True
print(type(czy_znasz_python))  # <class 'bool'>
print(int(czy_znasz_python))  # 1
print(int(False))  # 0
print(bool(0))  # bool() - rzutowanie na typ logiczny, False
print(bool(1))  # True

print(bool(100))  # True
print(bool(-10))  # True
print(bool("Radek"))  # True

print(bool(""))  # False
print(bool(None))  # False, None (null) - wartość nieokreslona

# and - i
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(False and True)  # False

# or - lub
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True

x = 1
print(not x == 1)  # False, == - porównanie

a = 6
b = 9
print(f"Porównanie {a} > {b}", a > b)
print(f"Porównanie {a} < {b}", a < b)
print(f"Porównanie {a} == {b}", a == b)  # porównanie, czy równe
print(f"Porównanie {a} >= {b}", a >= b)
print(f"Porównanie {a} != {b}", a != b)  # różne, Porównanie 6 != 9 True
print(f"Porównanie {a} <= {b}", a <= b)
# Porównanie 6 > 9 False
# Porównanie 6 < 9 True
# Porównanie 6 == 9 False
# Porównanie 6 >= 9 False
# Porównanie 6 != 9 True
# Porównanie 6 <= 9 True
