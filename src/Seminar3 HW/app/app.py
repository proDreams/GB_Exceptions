from app.exceptions import WrongLenException, WrongDataFormatException, ReadOnlyException
from app.parse_name import ParseName


class CreateFile:
    def __init__(self):
        self.text = input("""
Введите строку содержащую следующие данные в указанном формате:
Фамилия - одно слово
Имя - одно слово
Отчество - одно слово
Дата рождения - ДД.ММ.ГГГГ
Номер телефона - 1234567890
Пол - m или f
: """).split()
        if not self.check_len(self.text):
            raise WrongLenException(len(self.text))

        self.dob = self.pop_dob()
        self.phone = self.pop_phone()
        self.sex = self.pop_sex()

        self.name_parser = ParseName(self.text)
        self.last_name = self.name_parser.parse_last_name()
        self.patronymic = self.name_parser.parse_patronymic()
        self.first_name = self.name_parser.get_name()

        self.create_file()

    @staticmethod
    def check_len(text):
        if len(text) != 6:
            return False
        return True

    def pop_dob(self):
        for i in range(len(self.text)):
            if "." in self.text[i]:
                try:
                    temp = [int(j) for j in self.text[i].split(".")]
                except ValueError:
                    raise WrongDataFormatException(3, self.text[i])
                if 0 < temp[0] <= 31 and 0 < temp[1] <= 12 and 1930 <= temp[2] <= 2023:
                    return self.text.pop(i)
                raise WrongDataFormatException(3, self.text[i])

    def pop_phone(self):
        for i in range(len(self.text)):
            if "+" in self.text[i]:
                raise WrongDataFormatException(1, self.text[i])
            elif self.text[i].isdigit():
                if len(self.text[i]) == 10 or (len(self.text[i]) == 11 and self.text[i][0] == "8"):
                    return self.text.pop(i)
                raise WrongDataFormatException(1, self.text[i])
        else:
            raise WrongDataFormatException(4)

    def pop_sex(self):
        for i in range(len(self.text)):
            if len(self.text[i]) == 1:
                if self.text[i] == "f" or self.text[i] == "m":
                    return self.text.pop(i)
                raise WrongDataFormatException(2, self.text[i])

    def create_file(self):
        try:
            with open(f"{self.last_name}.txt", "a", encoding="utf-8") as f:
                f.write(f"<{self.last_name}><{self.first_name}><{self.patronymic}><{self.dob}><{self.phone}><{self.sex}>\n")
            print(f"Создан файл {self.last_name}")
        except PermissionError:
            raise ReadOnlyException(f"{self.last_name}.txt")