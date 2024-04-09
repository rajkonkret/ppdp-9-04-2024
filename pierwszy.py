import sys

print()  # wypisz/wydrukuj komunikat
print("Hello, World!")  # Hello, World!
print('Hello, World!')  # Hello, World!
print('Hello, World!')  # Hello, World!
print('Hello, World!')  # Hello, World!
print('Hello, World!')  # Hello, World!
print('Hello, World!')  # Hello, World!
print('Hello, World!')  # Hello, World!
# ctrl d - powielanie linijek
print('Nazywam się Radek')
# print("Nazywam się Radek')
#   File "C:\Users\CSComarch\PycharmProjects\ppdp-9-04-2024\pierwszy.py", line 11
#     print("Nazywam się Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 11)
print(type("Nazywam się Radek"))  # type() - sprawdzenie typu danych  - <class 'str'> typ tekstowy
print(39)
print(type(39))  # <class 'int'> liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)
print("54" + "14")  # 5414 - konkatenacja tekstów
print(54 + 14)  # 68
# print("54" + 14)  # TypeError: can only concatenate str (not "int") to str
# silne typowanie - nie zmienia sam typów
print(5 * "4")  # 44444
print(5 * int("4"))  # int() - rzutowanie(zamiana) na typ int  # 20
print(str(56) + "44")  # str() - rzutowanie na string(typ tekstowy) 5644 - konkatenacja
