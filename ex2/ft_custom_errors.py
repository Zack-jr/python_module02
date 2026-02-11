class GardenError(Exception):
    """Custom exception inheriting from Exception"""
    pass


class PlantError(GardenError):
    """Custom exception inheriting from GardenError"""
    pass


class WaterError(GardenError):
    """Custom exception inheriting from GardenError"""
    pass


def check_plant_health():
    """Raise a custom error"""
    raise PlantError("The tomato plant is wilting!")


def check_water():
    """Raise a custom error"""
    raise WaterError("Not enough water in the tank!")


def catch_errors():
    """Catch every error"""
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
    print("Testing catching all the garden errors...")
    for func in [check_plant_health, check_water]:
        try:
            func()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == '__main__':
    catch_errors()

# raise allows us to signal an error in a specific case
# we can raise and pass a message as a parameter
# Errors a.k.a exceptions can inherit from other error classes
# We can create custom exceptions
