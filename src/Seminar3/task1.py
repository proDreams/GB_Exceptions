def do_something(a, b):
    return a / b


try:
    result = do_something(2, 0)
except ZeroDivisionError:
    print("Error")
else:
    print(result)
