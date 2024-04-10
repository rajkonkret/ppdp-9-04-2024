dictionary = {'imie': 'Radek', 'nazwisko': "kowalski"}
print(type(dictionary))
print(dictionary)
# <class 'dict'>
# {'imie': 'Radek', 'nazwisko': 'kowalski'}

# wypisze klucze
for i in dictionary:
    print(i)
    # imie
    # nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wypisanie wartości
for v in dictionary.values():
    print(v)
# Radek
# kowalski

# wypisanie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => kowalski

c = {'name': "Radek", 'age': 5}
print({v: k for k, v in c.items()})
# {'Radek': 'name', 5: 'age'}

d = {}
for k, v in c.items():
    d[v] = k

print(d)  # {'Radek': 'name', 5: 'age'}
