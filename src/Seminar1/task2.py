def array_sum(arr):
    result = 0
    for i in range(len(arr)):
        if len(arr) != len(arr[i]):
            raise Exception("Массив не квадратный!")
        for j in range(len(arr)):
            if arr[i][j] == 0 or arr[i][j] == 1:
                result += arr[i][j]
            else:
                raise Exception("В массиве должны быть только 0 и 1")
    return result


array = [[1, 1, 0], [0, 0, 1], [0, 1, 1]]
print(array_sum(array))
