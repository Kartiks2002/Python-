#19.	Write a program to find a sum of digits of a number using recursion.

def rec_sum(num: int, ans=0) -> ():
    if num == 0:
        return ans
    ans += (num % 10)
    return rec_sum(num//10, ans)

while(1):
    user_input = input("Enter a no (e to exit): ")
    if user_input.lower() == 'e':
        break
    try:
        no = int(user_input)
        print(rec_sum(no))
    except ValueError:
        print("please enter a valid no!")