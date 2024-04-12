# json - {"name" : "Radek"}
# obiekt typu klucz-wartosc
# przypomina słownik w pythonie
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

# tworzenie jsona
dict_json = json.dumps(person_dict)
print(dict_json)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(dict_json))  # <class 'str'>

# zapisanie jsona do pliku
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4)
    # {
    #     "name": "Radek",
    #     "age": 40,
    #     "czy_pali": null
    # }
with open('nasze_dane.json', 'r') as file:
    data = json.load(file)

print(data)
print(type(data))
# {'name': 'Radek', 'age': 40, 'czy_pali': None}
# <class 'dict'>

print(data.keys())
print(data.values())
print(data.items())
print(data['name'])
# dict_keys(['name', 'age', 'czy_pali'])
# dict_values(['Radek', 40, None])
# dict_items([('name', 'Radek'), ('age', 40), ('czy_pali', None)])
# Radek
