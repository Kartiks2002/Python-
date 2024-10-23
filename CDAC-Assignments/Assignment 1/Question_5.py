# Design a code which will find whether the given number is Palindrome number or not

number = int(input("Enter a number: "))

digits = []

while number > 0:
    digit = number % 10
    digits.insert(0,digit)
    number //= 10

# print(digits)

is_palindrome = False
for i in range(len(digits)//2):
    if digits[i] != digits[-1-i]:
        break
    else:
        is_palindrome = True

if not is_palindrome:
    print(f'The given number is not a palindrome')
else:
    print(f'The given number is a palindrome')