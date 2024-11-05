#12.	Write a program to check Armstrong number?


def is_armstrong(no: int) -> bool:
    num_of_digits = len(str(no))
    temp = 0
    temp2 = no
    while(no > 0):
        digit = no % 10
        temp = temp + digit** num_of_digits
        no //= 10
    if temp == temp2:
        return True
    return False

print(is_armstrong(153))
print(is_armstrong(1634))
print(is_armstrong(69))