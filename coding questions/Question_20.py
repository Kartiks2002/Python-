#20.	Write a program to Add Two Numbers Without Using the Addition Operator

def add(a: int, b: int) -> int:
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


print(add(5,3))