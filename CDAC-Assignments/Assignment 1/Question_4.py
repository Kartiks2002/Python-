# Write a program that accepts a string and calculates the number of letters and
# digits. Suppose if the entered string is: qwerty123 Then the output will be:
# LETTERS: - 6 DIGITS: - 3

user_string = input('Enter a string : ')
count_of_letters = 0
count_of_digits = 0
for i in user_string:
    if i.isalpha(): count_of_letters+=1
    elif i.isdigit(): count_of_digits+=1

print(f'LETTERS: {count_of_letters}, DIGITS: {count_of_digits}')
