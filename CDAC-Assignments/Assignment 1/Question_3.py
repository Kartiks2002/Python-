# Write a program that will find all the numbers between 1000 and 3000 (both excluded) such
# that each digit of a number is an odd number. Print the number of such elements

odd_digit_numbers = []

for i in range(1001, 3000):
    temp = i
    flag = True
    while(temp > 0):
        digit = temp%10
        if (digit & 1 != 1):
            flag = False
            break
        temp //=10
    if (flag): odd_digit_numbers.append(i)

print(odd_digit_numbers)
