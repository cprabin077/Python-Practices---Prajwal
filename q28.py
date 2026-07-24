# 28.	Select 3 unique winners from a list of participants.

import random

participants = ["Prabin", "Ruchi", "Rekha", "Sagar", "Prajwal", "Bibek", "Depti"]

winners = random.sample(participants, 3)

print("Winners:", winners)