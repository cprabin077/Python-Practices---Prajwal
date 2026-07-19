# 2.	Create a Rectangle class and calculate area and perimeter.

# Create Class
class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def display(self):
        print("Rectangle Details")
        print("----------------")
        print("Length :", self.length)
        print("Breadth :", self.breadth)
        print("Area :", self.area())
        print("Perimeter :", self.perimeter())

# Create Object
rect1 = Rectangle(10,5)

# Display details
rect1.display()

