# 10.	Create a Library class that stores and displays book information.

# Create Class
class Library:
    def __init__(self, title, author, price, edition):
        self.title = title
        self.author = author
        self.price = price
        self.edition = edition

    def display_details(self):
        print("\nLibrary Book Information")
        print("------------------------")
        print("Title  :", self.title)
        print("Author :", self.author)
        print("Price  : Rs.", self.price)
        print("Edition :", self.edition)


# Create Objects
book1 = Library("Python Programming", "Prabin Chaudhary", 850, "10th")
book2 = Library("Data Structures", "Mark Allen Weiss", 1200, "5th")
book3 = Library("Database Systems", "Abraham Silberschatz", 1500, "4th")

# Display Details
book1.display_details()
book2.display_details()
book3.display_details()