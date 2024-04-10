# instrukcja warunkowe
# uzależnia wykonanie programu od wyniku wyrażenia - bool
# instrukcje strowania przepływem programu
# if - jesli/jeżeli
# if warunek:
#     komenda_do_wykonania - gdy warunek spełniony
# po : musi byc wciecie i mimum jedna komenda pythonowa

odp = True
print(type(odp))

if odp:
    print("Brawo")

print("Dalsza częśc programu")
odp = False
if odp:
    print("Brawo")  # gdy warunek True
else:
    print("Musisz się uczyć")  # obowiązkowe wciecie, gdy warunek False
# <class 'bool'>
# Brawo
# Dalsza częśc programu
# Musisz się uczyć
print("Dalsza czesc programu 2")

if odp:
    pass  # nic nie rób

print("Dalej")

# podatek = 0.9
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.6
# else:
#     podatek = 0.9
# print(f"Zapłacisz {zarobki * podatek} pln.")
# podatek 0.2 dla dochodu od 10000 do 29999
# kolejnosc elif ma znaczenie
# po spełnieniu pierwszego warunku(True) wychodzi z pięterka, pozostałe nie są sprawdzane

suma_zam = 150
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabaciik {rabacik}")

rabat = 25 if suma_zam > 150 else 0
print(f"Rabaciik {rabat}")

# zasymulejemy system analziy logów
# dane przyjdą w zmiennych
# na podstawie wartości tych zmiennych bedziemy wykonywac różne działania
# console, email, inny
# error -> critical, medium, inny
# w przypadku błedu w konsoli wyświetlamy komunikat, że nastąpił błąd
# w przypadku sytemu email do listy wpisywac będziemy opis poziomu błedów
# np.: critical -> krytyczny

alert_system = 'email'
error = 'critical'
error_list = []

if alert_system == 'console':
    print("Stało się coś strasznego!!!")
elif alert_system == 'email':
    if error == 'critical':
        error_list.append("Krytyczny")
    elif error == 'medium':
        error_list.append('Ostrzeżenie')
    else:
        print("Inny błąd, idź na kawę.")
else:
    print("Nie znam takiego sytemu")

print(error_list)

# Stworzyc program - test z ......
# zadac pytanie
# pobrac odpowiedź
# sprawdzic poprawnośc i wyswietlić odpowiedni komunikat

odp = input("Podaj nazwę stolicy Polski")
if odp.upper().replace(" ", "") == "WARSZAWA":
    print("Prawidłowa odpowiedź")
else:
    print("Sprawdź w wikipedii")
# dodać kilka pytań, dodać licznik prawidłowych odpowiedzi

a = 0
a = a + 1
a += 1
print(a)

spam = 1
spam += 1  # spam = spam + 1
print(spam)

spam -= 1  # spam = spam - 1
print(spam)

spam *= 1  # spam = spam * 1
print(spam)

spam /= 1  # spam = spam / 1
print(spam)

spam %= 1  # spam = spam % 1
print(spam)
