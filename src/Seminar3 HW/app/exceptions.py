class WrongDataFormatException(Exception):
    def __init__(self, data, code):
        self.data = data
        self.code = code
        self.types = {1: "10 чисел в формате 1234567890",
                      2: "f или m",
                      3: "валидная дата в формате ДД.ММ.ГГГГ"}

    def __str__(self):
        return f"Код ошибки: 2\n" \
               f"Неверный формат данных.\n" \
               f"Требуется {self.types[self.code]}, введено {self.data}\n"


class WrongLenException(Exception):
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"Код ошибки: 1\n" \
               f"Неверное количество данных.\n" \
               f"Требуется 6, введено {self.length}\n"
