# 13.	Write a program to reverse a given number?

def reverseNo(n : int) -> int:
    str_no = str(n)
    str_no = str_no[::-1]
    return int(str_no)

while(1):
    user_input = input("Enter a no (e to exit): ")
    if user_input.lower() == 'e':
        break
    try:
        no = int(user_input)
        print(reverseNo(no))
    except ValueError:
        print("please enter a valid no!")