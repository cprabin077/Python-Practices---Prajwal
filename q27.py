# 27.	Shuffle a list of names.

import random

names = ["Prabin", "Ruchi", "Rekha", "Sagar", "Prajwal", "Bibek"]

random.shuffle(names)

print("Shuffled Names:", names)

print("-------------"*5)

# Alternative Method: Using User Input

import random

# Input student names
names = input("Enter student names separated by commas: ").split(",")

names = [name.strip() for name in names]

random.shuffle(names)

print("Shuffled Names:", names)