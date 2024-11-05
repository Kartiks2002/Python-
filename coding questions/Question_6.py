#6.	Program to find n’th Fibonacci number

def fibo(no: int) -> int:
    a, b = 0, 1
    if no == 1:
        return a
    elif no == 2:
        return b
    for i in range(no):
        a, b = b, a+b
    return a


# fibo series : 0 1 1 2 3 5 8 13 21 34 55 89 144
# no          : 1 2 3 4 5 6 7 8  9  10 11 12 13

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
