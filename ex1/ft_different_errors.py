def garden_operations():
    try:
        print("Testing ValueError")
        int("abc")
    except ValueError:
        print(f"Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        n = 1
        n = n / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    try:
        print("Testing FileNotFoundError")
        open("imaginaryfile.txt")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file 'imaginaryfile.txt'\n")
    try:
        print("Testing KeyError...")
        plants = {"rose": 1}
        print(plants["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    print("Testing multiple errors together")
    try:
        a = 1 / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

def test_error_types():
    print("===Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")

test_error_types()