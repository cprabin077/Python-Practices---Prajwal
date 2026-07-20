# 11.	Find the square root of a user-entered number.

num = float(input("Enter the number: "))

if num < 0:
    print("Square root of a negative number is not possible.")
else: 
    print(f"The square of {num} is: ", num**0.5) # root = pow(1/2) => pow(0.5)

print("-------------------"*5)
# Alternative method
import math

num = float(input("Enter a number: "))

# Check for negative number
if num < 0:
    print("Square root of a negative number is not possible.")
else:
    result = math.sqrt(num)
    print(f"The square of {num} is: ", result)