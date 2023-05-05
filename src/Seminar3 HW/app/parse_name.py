class ParseName:
    def __init__(self, data):
        self.data: list = data
        self.first_name = None
        self.last_name = None
        self.patronymic = None

    def parse_last_name(self):
        suffixes = ["ов", "ова", "ев", "ева", "ин", "ина", "ын", "ына", "ий", "ая", "ой"]
        for i in self.data:
            if any(j in i for j in suffixes):
                self.last_name = i
                self.data.remove(i)
                break
        return self.last_name

    def parse_patronymic(self):
        suffixes = ["ович", "евич", "ич", "овна", "евна", "ична", "инична"]
        for i in self.data:
            if any(j in i for j in suffixes):
                self.patronymic = i
                self.data.remove(i)
                break
        return self.patronymic

    def get_name(self):
        return self.data[0]
