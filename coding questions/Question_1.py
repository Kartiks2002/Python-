#1.	Write a program for counting the number of every character of a given text file.

count = {}
with open("test.txt", "r") as f:
    content = f.read()

for i in content:
    if i not in count:
        count.update({i:1})
    else:
        count.update({i:count[i]+1})

print(count)

# print(dic["h"])