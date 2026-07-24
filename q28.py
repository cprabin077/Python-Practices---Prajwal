# 28.	Select 3 unique winners from a list of participants.

import random

participants = ["Prabin", "Ruchi", "Rekha", "Sagar", "Prajwal", "Bibek", "Depti"]

winners = random.sample(participants, 3)

print("Winners:", winners)

print("--------------"*5)

# Alternative Method: Using User Input
import random

participants = input("Enter participant names separated by commas: ").split(",")

participants = [name.strip() for name in participants]

winners = random.sample(participants, 3)

print("Winners:", winners)