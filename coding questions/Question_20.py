#20.	Write a program to Add Two Numbers Without Using the Addition Operator

def add(a: int, b: int) -> int:
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a


print(add(5,3))
