import chardet

#  pip install chardet

# print(chardet)
# <module 'chardet'
# from 'C:\\Users\\CSComarch\\PycharmProjects\\ppdp-9-04-2024\\.venv\\Lib\\site-packages\\chardet\\__init__.py'>

file_path = 'test.log'
with open(file_path, 'rb') as file:  # musi byc odczytany w trybie binarnym 'rb'
    raw_data = file.read()

print(raw_data)  # b'Radek\r\nDodane\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'
result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.670697820753897, 'language': 'Turkish'}
# po zwiększeniu próbki wynik mamy na 99%
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
print(type(result))
encoding = result['encoding']
confidence = result['confidence']
print(encoding, confidence)  # utf-8 0.99

print(raw_data.decode(encoding=encoding))
# Radek
# Dodane
# Dodane
# Dodane
# Dośdane
# Dośdane
# Dośćąźdane
