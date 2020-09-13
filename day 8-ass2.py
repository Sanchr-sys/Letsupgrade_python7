##############FILE HANDLING##############

class MyException(Exception):
    pass

class NoWriteException(MyException):
    def __init__(self):
        print("Cannot be written")


try:
    f1 = open(file = r"C:\Users\sanchal\PycharmProjects\letsupgrade.txt ", mode = "r")
    print("readable = ?",f1.readable())
    output = f1.read()
    print("File contents are:", output)

    try:
        if f1.mode == 'r':
            f1 = open(file=r"C:\Users\sanchal\PycharmProjects\letsupgrade.txt ", mode="w")
            raise NoWriteException()
        else:
            print("File can be read only")

    except NoWriteException:
        pass

finally:
    f1.close()