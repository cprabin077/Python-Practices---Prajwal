# 29.	Generate a random password of 8 characters.

import random
import string

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate an 8-character password
password = ""

for i in range(8):
    password += random.choice(characters)

print("Random Password:", password)