# 28.	Write a program to swap two numbers without using the third variable?


def swap(a: int, b: int) -> None:
    a, b = b, a
    return a, b

if __name__ == "__main__":
    a, b = 1, 2
    a, b = swap(a, b)
    print(a, b)

