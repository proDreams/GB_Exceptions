MIN_ARRAY_LENGTH = 3


def get_ind(arr, val):
    if arr:
        if len(arr) < MIN_ARRAY_LENGTH:
            return -1
        elif val in arr:
            return arr.index(val)
        return -2
    return -3


array = [1, 2, 3, 4, 5]
value = int(input("Введите число для поиска в массиве: "))
result = get_ind(array, value)
match result:
    case -1:
        print("Длина массива меньше минимума")
    case -2:
        print("Искомый элемент не найден")
    case -3:
        print("Пустой массив")
    case _:
        print(f"Индекс элемента: {result}")
