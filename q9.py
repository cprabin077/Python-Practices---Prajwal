# 9.	Create a Laptop class and demonstrate the use of a constructor (_init_).

class Laptop:
    def __init__(self, brand = "Unknown", model = "Unknown", price = 0):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print("\nLaptop Details")
        print("--------------")
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price : Rs.", self.price)

laptop1 = Laptop()
laptop1.display_details()

laptop1 = Laptop("Dell", "Inspiron 15", 85000)
laptop1.display_details()

laptop1 = Laptop("Dell", "Vostro", 105000)
laptop1.display_details()