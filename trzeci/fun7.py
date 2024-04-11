# a=6 - argumenty po nazwie
# para klucz=wartosc
def connect(**opcje):  # ** - argumenty nazwane, słownikowe
    print(opcje)
    print(type(opcje))  # <class 'dict'>
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    connect_param['pwd'] = opcje
    print(connect_param)


def all_param(*args, **kwargs):
    print(args, kwargs)


connect()  # {}
connect(a=8, b=8)  # {'a': 8, 'b': 8}
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 8, 'b': 8}}
connect(name="Radek", pwd="10")
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'name': 'Radek', 'pwd': '10'}}

all_param()  # () {}
all_param(1, 2, 3)  # (1, 2, 3) {}
all_param(a=1, b=5, c=8, d=90)  # () {'a': 1, 'b': 5, 'c': 8, 'd': 90}
all_param(name="Radek")  # () {'name': 'Radek'}
# all_param(a=1, 2)  # SyntaxError: positional argument follows keyword argument
all_param(None)  # (None,) {}
