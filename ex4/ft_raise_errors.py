def check_plant_health(plant_name, water_level, sunlight_hours):
    """checking the parameters and raising errors"""
    if plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         f"is too high (max 12)")
    else:
        return (f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks():
    """Checking the error raising"""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 8, 6))
    except ValueError as e:
        print(f"Error: {e}\n")
    print("Testing empty plant name...")
    try:
        print(check_plant_health(None, 8, 2))
    except ValueError as e:
        print(f"Error: {e}\n")
    print("Testing bad water level...")
    try:
        print(check_plant_health("cactus", 15, 4))
    except ValueError as e:
        print(f"Error: {e}\n")
    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("rose", 3, 0))
    except ValueError as e:
        print(f"Error: {e}\n")
    print("All error raising tests completed!")


if __name__ == '__main__':
    test_plant_checks()
