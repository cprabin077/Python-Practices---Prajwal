# 12.	Calculate the factorial of a given number using the math module.
import math

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = math.factorial(num)
    print(f"Factorial of {num} = ", result)

    