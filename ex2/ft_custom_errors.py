class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def check_plant_health():
    raise PlantError("The tomato plant is wilting!")

def check_water():
    raise WaterError("Not enough water in the tank!")

def catch_errors():
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        check_plant_health()
    except GardenError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        check_water()
    except GardenError as e:
        print(f"Caught WaterError: {e}\n")
    print(f"Testing carching all the garden errors...")
    for func in [check_plant_health, check_water]:
        try:
            func()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")

if __name__ == '__main__':
    catch_errors()