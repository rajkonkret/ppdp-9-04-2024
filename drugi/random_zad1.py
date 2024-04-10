import random  # biblioteka do generowania liczb pseudolosowych

print(random.randint(1, 6))  # int 1..6
print(random.randrange(1, 6))  # int 1..5
print(random.randrange(6))  # int 0..5
print(random.random())  # 0.8148211253214378 - float 0 do 0.999999
print(random.random() * 10)  # 5.21330288054166 - float od 0.00 do 9.999999

lista = [5, 7, 45, 34.56, 67, 80]
print(random.choice(lista))  # 45

lista_lotto = list(range(1, 50))  # 1 do 49

# print(random.choice(lista_lotto))
# print(random.choice(lista_lotto))
# print(random.choice(lista_lotto))
# print(random.choice(lista_lotto))
# print(random.choice(lista_lotto))
# print(random.choice(lista_lotto))

wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)

for i in range(6):
    wyn = random.choice(lista_lotto)
    lista_lotto.remove(wyn)
    print(wyn)

print(random.choices(lista_lotto, k=6))  # [18, 25, 24, 24, 46, 24] - losowanie z powtórzeniami
print(random.sample(lista_lotto, k=6))  # [7, 20, 24, 38, 45, 32]
print(random.sample(lista_lotto, 6))  # [12, 5, 18, 24, 11, 40]

print(random)
# <module 'random' from 'C:\\Users\\CSComarch\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\random.py'>
