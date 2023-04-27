class Counter:
    count = 0
    path = "123.txt"
    file = None

    def open(self):
        self.file = open(self.path, "a")

    def close(self):
        self.file.close()

    def add(self):
        try:
            self.file.write(str(self.count))
            self.count += 1
        except ValueError:
            print("File is closed")


add_count = Counter()
add_count.open()
add_count.add()
add_count.close()
# add_count.open()
add_count.add()
