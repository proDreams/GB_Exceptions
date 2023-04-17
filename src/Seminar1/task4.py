def check_array(arr):
    for i in range(len(arr)):
        if arr[i] is None:
            print(f"Внимание! Пустой элемент на позиции {i + 1}!")
        elif type(arr[i]) != int:
            print(f"Число на позиции {i + 1} не целочисленное или не число вовсе!")


array = [1, 0, None, 4.5, None, "adada"]
check_array(array)
