# 1.Write a program to find the factors of a given number and check whether
# the factor is even or odd.

given_number = int(input("Enter the number :"))

# factors = []
factors_= {}
for i in range(2, given_number//2):
    if given_number % i == 0:
        # factors.append(i)
        if(i & 1 == 0):                      # the factor is even
            factors_.update({i: 'Even'})
        else:                                # the factor is odd
            factors_.update({i:'Odd'})

# print(f'Factors of {given_number} : {factors_}')
print(f'Factors of {given_number} : {factors_}')

