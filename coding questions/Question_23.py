#23.	Write a program to Check whether the number is EVEN or ODD, without using any arithmetic or relational operators

def odd_eve(num: int) -> str:
    if num & 1:
        return "Odd"
    return "Even"

while(1):
    user_input = input("Enter a no (e to exit): ")
    if user_input.lower() == 'e':
        break
    try:
        no = int(user_input)
        print(odd_eve(no))
    except ValueError:
        print("please enter a valid no!")