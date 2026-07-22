# 24.	Generate a 4-digit OTP.

import random

# Generate a 4-digit OTP
otp = random.randint(1000, 9999)

# Display OTP
print("Your OTP is:", otp)


# Alternative Method
import random

otp = ""

for i in range(4):
    otp += str(random.randint(0, 9))

print("Your OTP is:", otp)
