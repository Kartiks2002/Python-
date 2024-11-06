#22.	Write a program to Multiply an Integer Number by 2 Without Using Multiplication Operator

def mul_2(num: int) -> int:
    # return num + num
    return num << 1
print(mul_2(5))