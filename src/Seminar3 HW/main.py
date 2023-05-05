from app.app import CreateFile
from app.exceptions import WrongLenException, WrongDataFormatException

if __name__ == "__main__":
    while True:
        try:
            CreateFile()
        except WrongLenException as ex:
            print(ex)
        except WrongDataFormatException as ex:
            print(ex)
