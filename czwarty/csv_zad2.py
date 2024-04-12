import csv

filename = 'records3.csv'

fields = []
rows = []

with open(filename, "r") as file:
    dialect = csv.Sniffer().sniff(file.read(1024))
    print(dialect)
    print(dialect.delimiter, dialect.quotechar)  # ; "
    file.seek(0)  # ustawienie odczytu na początek pliku, sniff przesunał na 1024
    # csvreader = csv.reader(file, delimiter=";")
    csvreader = csv.reader(file, delimiter=dialect.delimiter)

    # print(csvreader)  # <_csv.reader object at 0x000001AC7CFFE200>
    # for i in csvreader:
    #     print(i)

    fields = next(csvreader)  # next() - pobranie elementu z obiektu typu iterator i ustawienie odczytu na następny
    print(fields)  # ['name', 'branch', 'year', 'cgpa']
    # print(next(csvreader))  # ['radek', 'coe', '3', '0.1'] nastepny element odczytany
    for row in csvreader:  # ta petla wystaryje od drugiego wiersza
        # print(row)
        rows.append(row)

print(rows)
print(rows[0])  # ['radek', 'coe', '3', '0.1']
print(fields)  # ['name', 'branch', 'year', 'cgpa']
