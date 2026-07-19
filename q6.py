# 6.	Create a Book class and display book details using objects.

class Book:
    def __init__(self, name="Unknown", price=0, author="Unknown", edition="0", publisher="Unknown"):
        self.name = name
        self.price = price
        self.author = author
        self.edition = edition
        self.publisher = publisher

    def display_details(self):
        print("\nBook Details")
        print("------------")
        print("name  :", self.name)
        print("Price : Rs.", self.price)
        print("Author :", self.author)
        print("Edition  :", self.edition)
        print("Publisher :", self.publisher)


# Create Object (Default Values)
book1 = Book()
book1.display_details()

# Create Object (Custom Values)
book2 = Book("Python Programming", 850, "Prabin Chaudhary", "4th", "Heritage Publication")
book2.display_details()

# Create Object (Custom Values)
book3 = Book("Data Structures", 1200, "Mark Allen Weiss", "9th", "Unique Publication")
book3.display_details()
