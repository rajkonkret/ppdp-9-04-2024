# wyjątki - błedy podczas wykonania programu - zatrzymuja program
# try - exept [else - finally]
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # print(5 / 0)
    raise ZeroDivisionError("Zero")  # rzucenie wyjątku
except ZeroDivisionError as e:
    print("Dzielenie przez zero", e)

x = 0
try:
    if x == 0:
        raise MyException("X nie może być 0")
except MyException as e:
    print("X nie może być zero")
# Dzielenie przez zero Zero
# X nie może być zero
