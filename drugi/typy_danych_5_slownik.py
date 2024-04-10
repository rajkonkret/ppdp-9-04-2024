# słownik - para klucz:wartosc
# { "name" : "Radek" } - para klucz wartosc
# odpowiednik jsona w pythonie
# klucze nie mogą sie powtarzać

my_dict = {"A": 'one', "B": "two", "C": "three"}
print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three'}
print(type(my_dict))  # <class 'dict'>

# tworzenie pustego słownika
empty_dict = {}  # pusty słownik
empty_dict2 = dict()
print(empty_dict)  # {}  - pusty słownik
print(empty_dict2)  # {}

dict_mixed = {1: 'one', 'A': 'two', 3: 'three'}
print(dict_mixed)

print(dict_mixed.keys())
print(dict_mixed.values())
print(dict_mixed.items())
# {1: 'one', 'A': 'two', 3: 'three'}
# dict_keys([1, 'A', 3])
# dict_values(['one', 'two', 'three'])
# dict_items([(1, 'one'), ('A', 'two'), (3, 'three')])

# dodanie wielu elementó do słownika za pomocą tupli
dictionary = {'x': 2}
dictionary.update([('y', 2), ('z', 3)])
print(dictionary)  # {'x': 2, 'y': 2, 'z': 3}

# dodanie jedego elementu
empty_dict['imie'] = "Radek"
print(empty_dict)  # {'imie': 'Radek'}
empty_dict['wiek'] = 39
print(empty_dict)  # {'imie': 'Radek', 'wiek': 39}

# nadpisanie wartosci dla klucza
empty_dict['wiek'] = 43
print(empty_dict)  # {'imie': 'Radek', 'wiek': 43}

# wypisanie wartości dla klucza
print(empty_dict['wiek'])  # 43
print(empty_dict.get('wiek'))  # 43
print(empty_dict.get('wiek2', 'default'))  # default
# print(empty_dict['wiek2'])  # KeyError: 'wiek2'

print(empty_dict.pop('wiek'))  # 43
print(empty_dict)  # {'imie': 'Radek'}
empty_dict['age'] = 45
print(empty_dict)  # {'imie': 'Radek', 'age': 45}
print(empty_dict.popitem())  # usunięcie ostatniego elemntu, ('age', 45)

empty_dict.clear()
print(empty_dict)  # {}

my_dict = dictionary.copy()  # kopiowanie elementów
print(my_dict)
