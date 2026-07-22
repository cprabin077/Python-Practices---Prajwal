# 23.	Create a coin toss program.

import random

# Toss the coin
result = random.choice(["Heads", "Tails"])

print("Coin Toss Result:", result)


# Toss the Coin Multiple Times
import random

while True:
    result = random.choice(["Heads", "Tails"])
    print("Coin Toss Result:", result)

    choice = input("Toss again? (y/n): ")
    if choice.lower() != "y":
        break