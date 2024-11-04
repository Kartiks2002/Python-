#2.	Write a program to check prime number?
def isPrime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

while(1):
    user_input = input("Enter a no (e to exit): ")
    if user_input.lower() == 'e':
        break
    try:
        no = int(user_input)
        print(isPrime(no))
    except ValueError:
        print("please enter a valid no!")


