#10.	Write a program to check palindrome number?

def isPalindrome(n: int) -> bool:
    str_no = str(n)
    return str_no == str_no[::-1]


while(1):
    user_input = input("Enter a no (e to exit): ")
    if user_input.lower() == 'e':
        break
    try:
        no = int(user_input)
        print(isPalindrome(no))
    except ValueError:
        print("please enter a valid no!")