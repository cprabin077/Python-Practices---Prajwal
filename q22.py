# 22.	Create a dice rolling simulator.

import random

# Roll the dice
dice = random.randint(1, 6)

# Display the result
print("You rolled:", dice)


# Roll the Dice Multiple Times

import random

while True:
    print("You rolled:", random.randint(1, 6))

    choice = input("Roll again? (y/n): ")
    if choice.lower() != "y":
        break