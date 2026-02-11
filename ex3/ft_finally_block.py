class InvalidPlantError(Exception):
    """Custom exception inheriting from Exception"""
    pass


def water_plants(plant_list):
    """ Waters plants in a plant_list"""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise InvalidPlantError(f"Cannot water {plant} "
                                        f"- invalid plant!")
            print(f"Watering {plant}")
    except InvalidPlantError as e:
        print(f"Error: {e}")
        raise e
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Testing the watering system"""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    try:
        plant_list = ["tomato", "lettuce", "carrots"]
        water_plants(plant_list)
        print("Watering completed successfully!\n")
    except InvalidPlantError:
        pass
    print("Testing with error...")
    try:
        water_plants(["tomato", None])
    except InvalidPlantError:
        pass
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == '__main__':
    test_watering_system()

# finally works with try / try except
# use finally when you have to "cleanup" and pass by a certain
# block of code regardless of the exceptions/errors
