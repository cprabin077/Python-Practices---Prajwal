# 5.	Create a Car class with attributes brand, model, and year. Display car information.

# Create Class 
class Car:
    def __init__(self, brand="Toyota", model="Corona", year=1966):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print("\nCar Information:")
        print("-----------------")
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Year :", self.year)
        

# Create Object
car1 = Car()

# Dispaly Details
car1.display_details()

# Create Object and Pass Values
car1 = Car("Toyota", "Prius", 2016)

# Dispaly Details
car1.display_details()

# Create Object and Pass Values
car1 = Car("Nissan", "Nissan Ariya", 2020)
# Dispaly Details
car1.display_details()


