# CRUD - Create, Read, Update, Delete

# Działanie	Instrukcja SQL	HTTP	            DDS
# Create	        INSERT	PUT / POST	        write
# Read (Retrieve)	SELECT	GET	read /          take
# Update	        UPDATE	POST / PUT / PATCH	write
# Delete (Destroy)	DELETE	DELETE	            dispose
# REST API

# HTTP GET
import requests as re

# pip install requests
url = "http://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = re.get(url)
print(response)  # <Response [200]>
# 200 - ok, 2xx
# 3xx - błedy przekierowania
# 4xx - 404 - brak zasoby, 400 Bad Request - błedy w danych
# 5xx - błedy serwera
print(response.status_code)
print(response.text)
print(type(response.text))  # <class 'str'>

data = response.json()
print(type(data))  # <class 'dict'>
print(data)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '073/A/NBP/2024', 'effectiveDate': '2024-04-12', 'mid': 3.9983}]}
# wypisac wszystkie klucze
print(data.keys())
for k in data:
    print(k)
# dict_keys(['table', 'currency', 'code', 'rates'])
# table
# currency
# code
# rates
print(data['table'])  # A
for k, v in data.items():
    print(k, "=>", v)
# table => A
# currency => dolar amerykański
# code => USD
# rates => [{'no': '073/A/NBP/2024', 'effectiveDate': '2024-04-12', 'mid': 3.9983}]
print(type(data['rates']))  # <class 'list'>
print(type(data['rates'][0]))  # <class 'dict'>
print(data['rates'][0]['mid'])  # 3.9983
# w ramach pracy domowej odczytac kurs eur, złota, lista wszystkich walut
# https://github.com/public-api-lists/public-api-lists
