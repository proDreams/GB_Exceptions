MAX_ARRAY_LENGTH = 3


def get_element(arr):
    if len(arr) > MAX_ARRAY_LENGTH:
        return -1
    else:
        return len(arr)


array = [1, 2, 3, 4, 5]
print(get_element(array))

