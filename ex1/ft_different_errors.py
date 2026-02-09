def garden_operations():
    n = 1
    try:
        int("abc")
    except ValueError:
        return ValueError
    try:
        n = n / 0
    except ZeroDivisionError:
        return ZeroDivisionError
    try:
        open("imaginaryfile.txt")


def test_error_types():
