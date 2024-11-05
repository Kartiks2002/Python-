#11.	Write a program to print factorial of given number without using recursion?

def factorial(no: int) -> int:
    ans = 1
    for i in range(2, no+1):
        ans *= i
    return ans

while True:
    try:
        number = int(input("Enter a non-negative integer to find its factorial: "))
        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            result = factorial(number)
            print(f"The factorial of {number} is {result}")
            break
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")