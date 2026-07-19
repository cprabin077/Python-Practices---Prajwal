# 8.	Create a Product class with name, price, and quantity. Calculate total inventory value.

class Product:
    def __init__(self, name = "Unknown", price = 0, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_inventory_value(self):
        return self.price * self.quantity
    
    def display_details(self):
        print("\nProduct Information: ")
        print("---------------------")
        print("Name :", self.name)
        print("Price :", self.price)
        print("Quantity :", self.quantity)
        print("Total Inventory Value :", self.total_inventory_value())

product1 = Product()
product1.display_details()

product1 = Product("Laptop", 110000, 1)
product1.display_details()

product1 = Product("Mobile", 30000, 5)
product1.display_details()
