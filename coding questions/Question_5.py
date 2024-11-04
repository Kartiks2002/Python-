#5.	Write a program of Fibonacci series using generators


def fibo(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

fibo_generator = fibo(15)
for num in fibo_generator:
    print(num, end=" ")
