# csv - pliki w których dane oddzielone znakiem podziału
import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0.1']

filename = "record.csv"
with open(filename, 'w', newline="") as csv_f:
    # zapis wierszami
    csvwriter = csv.writer(csv_f)  # zwraca narzędzie do pracy z plikami csv
    csvwriter.writerow(fields)
    csvwriter.writerow(row)
# newline="" pozwala ominąc problem podwójnych enterów na końcu linii

dictionary = dict(zip(fields, row))
print(dictionary)
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0.1'}

with open('records2.csv', 'w', newline='') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dictionary)

dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0.1'},
    {'name': 'tomek', 'branch': 'cos', 'year': '3', 'cgpa': '0.1'},
    {'name': 'michal', 'branch': 'cod', 'year': '3', 'cgpa': '0.1'},
    {'name': 'zenek', 'branch': 'cor', 'year': '3', 'cgpa': '0.1'},
]

with open('records3.csv', 'w', newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(dict_list)
