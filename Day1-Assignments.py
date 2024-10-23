# Assignment 1: Objective: Create a program that converts inches to feet, meters and centimeters and continue until the user wishes to
# Input:
# Prompt the user to enter a value (float) and the unit of measurement (e.g. inches).
# Prompt the user to select the target unit for conversion
# Prompt the user to press ‘Yes’ or ‘No’ to repeat
# Calculation:
# Convert the input value to the target unit using appropriate conversion factors.
# Use typecasting where necessary to handle different types of input.
# Use a while loop to repeat
# Use break statement to stop calculations one user enters ‘No’
# Output:
# Display the converted value along with its unit.
# Continue until the user presses No.
# Conversion Options:
# Inches to feet, meters, and centimeters.
def convert_units(value, unit, target_unit):
    # Conversion factors
    if unit == "inches":
        if target_unit == "feet":
            return value / 12
        elif target_unit == "meters":
            return value * 0.0254
        elif target_unit == "centimeters":
            return value * 2.54
    return None


while True:
    value = float(input("Enter the value: "))
    unit = input("Enter the unit of measurement (inches): ").lower()

    if unit != "inches":
        print("Currently only supports conversion from inches.")
        continue

    target_unit = input("Enter the target unit (feet, meters, centimeters): ").lower()
    result = convert_units(value, unit, target_unit)

    if result is not None:
        print(f"{value} {unit} is {result} {target_unit}.")
    else:
        print("Invalid target unit.")

    repeat = input("Do you want to continue? (Yes/No): ").lower()
    if repeat == "no":
        break

# -------------------------------------------
# Assignment 2: Build a calculator for +, -, * and / operations using if and else condition statements
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        return "Invalid operation"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

result = calculator(a, b, operation)
print(f"The result is: {result}")

# -------------------------------------------
# Assignment 3: Print a Fibonacci series of numbers starting from 2 go until 100
def fibonacci_series():
    a, b = 0, 1
    print(a, end=" ")
    while b <= 100:
        print(b, end=" ")
        a, b = b, a + b

fibonacci_series()
