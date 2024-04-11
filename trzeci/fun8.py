def all_params(a, b, /, c=42, d=256):
    print("a, b", a, b)
    print("c, d", a, b)


all_params(1, 2)
all_params(1, 2, 3, 4)
# po dołozeniu /
# TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'b'
# oddziela argumenty które musza byc przekazane po pozycji od nazwanych
# all_params(1, c=2, b=3, d=4)
all_params(1, 2, d=7, c=9)


# a i b muszą byc po pozycji !!!
# c i d mogą być po pozycji lub po nazwie

def all_params_2(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


all_params_2(1, 2)  # a, b 1 2
all_params_2(1, 2, 3)  # c, d 3 256
all_params_2(1, 2, c=8)  # c, d 8 256
all_params_2(1, 2, 3, 4)  # args (4,)
all_params_2(1, 2, 3, 4, 5, 6, 7, 8, 9)  # args (4, 5, 6, 7, 8, 9)
all_params_2(1, 2, 3, 4, 5, 6, 7, 8, 9, d=90)  # c, d 3 90, d musi byc po nazwie
all_params_2(1, 2, 3, 4, 5, 6, 7, 8, 9, d=90, name="Radek")  # kwargs {'name': 'Radek'}
all_params_2(1, 2, 3, 4, 5, 6, 7, 8, 9, d=90, name="Radek", e=899)
# kwargs {'name': 'Radek', 'e': 899}
all_params_2(1, 2, 3, 4, 5, 6, 7, 8, 9, d=90, name="Radek", e=899, a=111)
# kwargs {'name': 'Radek', 'e': 899, 'a': 111}
