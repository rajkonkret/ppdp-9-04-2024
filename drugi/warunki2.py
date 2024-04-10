# match case - od Python 3.10
lista = []
lang = input("Podaj znane Ci języki")

match lang.lower().replace(" ", ""):
    case "python":
        print("Lubię pythona")
        lista.append(lang)
    case "java":
        print("Java to kawa")
        lista.append(lang)
    case _:  # wartość domyślna (else)
        print("Nie znam takiego języka")

print(lista)
