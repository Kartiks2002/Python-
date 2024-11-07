#29.	Write a program which takes a variable number of arguments.

def vari_no_args(*args, **kwargs) -> None:
    print(args)
    print(kwargs)

vari_no_args(123,235,36, "yo",name="john wick", car="mustang")
