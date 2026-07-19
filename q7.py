# 7.	Create a Circle class and calculate area and circumference.

p = 22/7
class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        r = self.radius
        return p * r * r
    
    def circumference(self):
        r = self.radius
        return 2 * p * r
    
    def display_details(self):
        print("\nCircle Information: ")
        print("--------------------")
        print("Radius :", self.radius)
        print("Area :", self.area())
        print("Circumference :", self.circumference())


circle1 = Circle()
circle1.display_details()

circle1 = Circle(7)
circle1.display_details()

circle1 = Circle(14)
circle1.display_details()