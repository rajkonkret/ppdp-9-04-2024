# napisa©ćaplikację kalkulator
# wykorzystać jako główną pętlę programu, pętlę while
# umieścić sposób ucieczki
#
# wyswietlić opcje
# pobrać działanie od użytkownika
# pobrać liczby
# wyświetlić wynik działania
#
# obsłużyć wyjątki

while True:
    print(f"""
1. Dodawanie
2. Odejmowanie
3. Mnożenie
4. Dzielenie
5. Koniec
""")
    odp = input("Podaj działanie")
    if odp == "5":
        break

    try:
        a = int(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))

        if odp == "1":
            print(f"Wynik dodawania {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik odejmowania {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik mnożenia {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik dzielenia {a} / {b} = {a / b}")
        else:
            print("Nie znam działania")
    except ZeroDivisionError as e:
        print('Nie dziel przez zero', e)
    except ValueError as e:
        print("Bład wartości", e)
    except TypeError as e:
        print("Bład typu", e)
    except Exception as e:
        print("Bład", e)
    else:
        print("Działanie poprawne")
    finally:
        print("Zakończyłem")

# inne podejscie
while True:
    odp = input("Podaj wyrażenie")
    print(eval(odp))  # zwraca wynik wyrażenia podanego w stringu
