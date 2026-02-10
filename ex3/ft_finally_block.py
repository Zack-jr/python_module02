class InvalidPlantError(Exception):
    pass

def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise InvalidPlantError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except InvalidPlantError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(["tomato", None])
    print("\nCleanup always happens, even with errors!")

if __name__ == '__main__':
    test_watering_system()