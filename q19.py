# 19.	Remove the decimal part from a number using trunc().

import math

num = float(input("Enter a decimal number: "))

result = math.trunc(num) # 4.99999 => 4

print("Number after truncation =", result)