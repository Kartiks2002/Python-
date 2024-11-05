#7.	Write a program to print Fibonacci series without using recursion?

def fibo(n: int) -> [int]:
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    fib = [a, b]
    for i in range(1, n):
        a, b = b, a+b
        fib.append(b)
    return fib


while 1:
    user_input = input("Enter no (e to exit) : ")
    if user_input == 'e':
        break
    else:
        try:
            no = int(user_input)
            print(fibo(no))
        except ValueError:
            print("Please enter a valid no of e to exit")


