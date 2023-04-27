import os


class DivisionByZeroError(ArithmeticError):
    pass


class NullElementError(TypeError):
    pass


class FileNotExists(FileNotFoundError):
    pass


def division(a, b):
    if b == 0:
        raise DivisionByZeroError
    else:
        return a / b


def array_elem(arr, ind):
    if arr[ind]:
        return arr[ind]
    raise NullElementError


def check_file(path):
    if os.path.exists(path):
        return os.path.exists(path)
    raise FileNotExists


lst = [1, 2, 3, None, 5, None, 0]
try:
    # division(2, 0)
    # array_elem(lst, 3)
    print(check_file("1235.txt"))
except DivisionByZeroError:
    print("Нельзя делить на ноль!")
except NullElementError:
    print("Пустой элемент")
except FileNotExists:
    print("Файла не существует!")
