def check_temperature(temp_str):
    print(f"Testing temperature: {temp_str}")
    try:
        n = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
    else:
        if n >= 0 and n <= 40:
            print(f"Temperature {n}°C is perfect for plants!\n")
            return n
        elif n > 40:
            print(f"Error: {n}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Error: {n}°C is too cold for plants (min 0°C)\n")
    
def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")

if __name__ == '__main__':
   test_temperature_input()

