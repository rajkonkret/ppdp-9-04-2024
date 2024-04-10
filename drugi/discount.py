from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2024-04-10

time = datetime.now()
print(time)  # 2024-04-10 15:08:50.456928

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0):
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-04-11

print(time.hour)  # 15
print(today.day)  # 10

formated_date = datetime.now().strftime('%d/%m/%Y')
print(formated_date)  # 10/04/2024

formated_time = datetime.now().strftime('%H:%M')
print(formated_time)  # 15:14

products = [
    {'sku': 1, 'exp_date': today, 'price': 100},
    {'sku': 2, 'exp_date': tomorrow, 'price': 200},
    {'sku': 3, 'exp_date': today, 'price': 80.50},
    {'sku': 4, 'exp_date': today, 'price': 137.78},
]

for product in products:
    # print(product)  # {'sku': 1, 'exp_date': datetime.date(2024, 4, 10), 'price': 100}
    if product['exp_date'] != today:
        continue  # nic nie rób, weż kolejny element z kolekcji
    product['price'] *= 0.8  # p = p * 0.8
    print(f"""
Price for sku {product['sku']}
is now {product['price']}""")
