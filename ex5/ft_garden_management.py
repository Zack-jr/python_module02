class GardenError(Exception):
    """Custom exception inheriting from Exception"""
    pass


class PlantError(GardenError):
    """Custom exception inheriting from GardenError"""
    pass


class Plant:
    """Define a plant class"""
    def __init__(self, plant_name, water_level, sunlight_hours):
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """Define a GardenManager class"""
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name, water_level, sunlight_hours):
        """adding a plant to a GardenManager"""
        if not plant_name:
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        new_plant = Plant(plant_name, water_level, sunlight_hours)
        self.plants.append(new_plant)
        print(f"Added {plant_name} successfully")

    def water_plants(self):
        """Watering the Garden Manager's plants"""
        print("Watering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.plant_name} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self):
        """Checking plant attributes and raising errors"""
        print("Checking plant health...")
        for plant in self.plants:
            try:
                if plant.water_level < 1:
                    raise ValueError(f"Water level {plant.water_level}"
                                     f" is too low (min 1)")
                elif plant.water_level > 10:
                    raise ValueError(f"Water level {plant.water_level}"
                                     f" is too high (max 10)")
                elif plant.sunlight_hours < 2:
                    raise ValueError(f"Sunlight hours {plant.sunlight_hours}"
                                     f" is too low (min 2)")
                elif plant.sunlight_hours > 12:
                    raise ValueError(f"Sunlight hours {plant.sunlight_hours}"
                                     f" is too high (max 12)")
                else:
                    print(f"{plant.plant_name}: healthy (water: "
                          f"{plant.water_level}, sun: {plant.sunlight_hours})")
            except ValueError as e:
                print(f"Error checking {plant.plant_name}: {e}\n")


def main():
    print("=== Garden Management System ===\n")
    gm = GardenManager()

    print("Adding plants to garden...")
    try:
        gm.add_plant("tomato", 5, 8)
        gm.add_plant("lettuce", 15, 5)
        gm.add_plant("", 0, 0)
    except PlantError as e:
        print(f"{e}\n")
    gm.water_plants()
    gm.check_plant_health()

    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...\n")
    finally:
        print("Garden management system test complete!")


if __name__ == '__main__':
    main()
