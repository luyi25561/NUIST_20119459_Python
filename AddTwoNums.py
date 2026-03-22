# Version 3
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
    print(f"Sum of {num1} and {num2} is {result}")
except ValueError:
    print("Please enter valid integers!")
