# 25.	Generate a 6-digit OTP.

import random

otp = random.randint(100000, 999999)

print("Your OTP is: ", otp)


# Alternative Method
import random

otp = ""

for i in range(6):
    otp += str(random.randint(0, 9))

print("Your OTP is:", otp)
