# 13.	Find the GCD of two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

small = min(num1, num2)

for i in range(small, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
        break


print(f"GCD of {num1} and {num2} = ", gcd)
