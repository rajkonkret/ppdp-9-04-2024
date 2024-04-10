# while - petla sterowana warunkiem

licznik = 0
while True:  # pętla nieskończona
    print("Komunikat!!!")
    licznik += 1
    if licznik > 10:
        break

print(licznik)  # 11
licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat2 !!!")

lista_int = []
lista = []
while True:
    wej = input("podaj liczbę")
    if not wej.isnumeric():  # sprawdza każdy znak
        break
    lista.append(wej)
    lista_int.append(int(wej))

print("Nasza lista:", lista)  # Nasza lista: ['1', '2', '3', '4']
print("Nasza lista int:", lista_int)
# Nasza lista: ['3', '6', '8', '90', '111']
# Nasza lista int: [3, 6, 8, 90, 111]
print("168" * 40)
print(168 * 40)
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
# 6720
