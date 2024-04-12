import pickle

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
print(type(lista))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# <class 'list'>

with open('lista.txt', 'w') as f:
    f.write(str(lista))

with open('lista.txt', 'r') as file:
    dane = file.read()

print(dane)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(dane[0])
print(type(dane))  # <class 'str'>
print(dane.split())  # ['[1,', '2,', '3,', '4,', '5,', '6,', '7,', '8,', '9]']
print(list(dane))
# ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ',', ' ',
#  '6', ',', ' ', '7', ',', ' ', '8', ',', ' ', '9', ']']

print(eval(dane))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(eval(dane)))  # <class 'list'>

with open('lista.pickle', "wb") as f:
    pickle.dump(lista, f)

with open('lista.pickle', "rb") as f:
    loaded_list = pickle.load(f)

print(loaded_list)
print(type(loaded_list))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# <class 'list'>

# serializacja - zamiana na postac bajtową
ser_lista = pickle.dumps(lista)
print(ser_lista)
# b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\te.'

# deserializacja
print(pickle.loads(ser_lista))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
