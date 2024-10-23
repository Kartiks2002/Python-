# Write a code that accepts a sequence of words as input and prints the words in a
# sequence after sorting them alphabetically

sequence_of_words = input('Enter some words : ')
words = sequence_of_words.split(' ')
words.sort()
print(words)