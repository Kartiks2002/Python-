# 14.	Given a list and find even numbers in that list using lambda function

lis = [1,2,3,4,5,6]
# even_nos = [i for i in lis if i%2 == 0]
even_nos = list(filter(lambda x: x % 2 == 0, lis))
print(even_nos)