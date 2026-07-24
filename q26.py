# 26.	Pick a random student from a list.

import random

# List of students
students = ["Prabin", "Ruchi", "Rekha", "Sagar", "Prajwal", "Bibek"]

student = random.choice(students)

print("Selected Student:", student)

print("-------------"*5)

# Alternative Method: Using User Input

import random

# Input student names
students = input("Enter student names separated by commas: ").split(",")

# Remove extra spaces
students = [student.strip() for student in students]

# Pick a random student
print("Selected Student:", random.choice(students))



