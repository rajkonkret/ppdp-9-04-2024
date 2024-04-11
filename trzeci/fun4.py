# funkcja zagnieżdzona, wewnętrzna
# mechanizm funkcji zagnieżdzonej używany jest w dekoratorach w pythonie

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwraca adres funkcji (referencje)


# nazwa funkcji i nawiasy()
fun1()  # To jest fun1
print(fun1())  # <function fun1.<locals>.fun2 at 0x00000147652F8CC0>
xfun = fun1()
print(xfun)  # <function fun1.<locals>.fun2 at 0x0000017E7C9E8CC0>
print(type(xfun))  # <class 'function'>
xfun()  # To jest fun2
