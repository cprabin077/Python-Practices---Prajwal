# Student Class

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display_details(self):
        print("Student Details")
        print("----------------")
        print("Name :", self.name)
        print("Roll :", self.roll)
        print("Marks:", self.marks)


# Create an object
student1 = Student("Prabin Chaudhary", 101, 92)

# Display student details
student1.display_details()