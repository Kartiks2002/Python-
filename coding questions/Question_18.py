#18.	Write a program to check the given number format is in binary or not.

def isBinary(n: int) -> bool:
    str_n = str(n)
    for i in str_n:
        if i not in ['0', '1']:
            return False
    return True

while(1):
    user_input = input("Enter a no (e to exit): ")
    if user_input.lower() == 'e':
        break
    try:
        no = int(user_input)
        print(isBinary(no))
    except ValueError:
        print("please enter a valid no!")