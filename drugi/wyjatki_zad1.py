# wyjątki - błedy wykonania programu
# przerywają działąnie programu

# przechwycenie wyjatku
try:
    # print(5 / 0)
    # print("A" / 2)
    print(int("A"))
    print(1 + 2)
except ZeroDivisionError as e:
    print("Nie dziel przez zero", e)
except TypeError as e:
    print("Bład typu", e)
except ValueError as e:
    print("Bład typu")
except Exception as e:  # łapie pozostałe błędy
    print("Bład", e)
else:  # gdy nie ma błędu
    print("Tylko gdy nie ma błedu")
finally:  # zawsze
    print("Wykona się zawsze")

print("Dalsza częśc programu")
