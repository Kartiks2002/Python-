#8.	Write a program to print Fibonacci series using recursion?

def fibo(n: int) -> int :
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

def print_fibo_series(n: int):
    for i in range(n):
        print(fibo(i), end=" ")

if __name__ == "__main__":
    while 1:
        user_input = input("Enter no (e to exit) : ")
        if user_input == 'e':
            break
        else:
            try:
                no = int(user_input)
                print_fibo_series(no)
                print()
            except ValueError:
                print("Please enter a valid no of e to exit")

