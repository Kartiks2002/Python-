#17.	Write a program to check if it is a palindrome number or not using a recursive method.

def reverseNum(num : int, rev=0) -> int:
    if num == 0:
        return rev

    rev = (rev * 10) + (num % 10)
    return reverseNum(num//10, rev)

def isPalindrome(num: int) -> bool:
    return num == reverseNum(num)

while(1):
    user_input = input("Enter a no (e to exit): ")
    if user_input.lower() == 'e':
        break
    try:
        no = int(user_input)
        print(isPalindrome(no))
    except ValueError:
        print("please enter a valid no!")