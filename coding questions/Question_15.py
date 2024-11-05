# 15.	Remove duplicates from an array?

array = [1,2,2,3,3,4,5,6,7,7]

# using sets
rm_duplicates = list(set(array))
print(rm_duplicates)

# using list comprehension
unique_arr = []
[unique_arr.append(x) for x in array if x not in unique_arr]
print(unique_arr)

# using dict.fromkeys()
unique_elements = list(dict.fromkeys(array))
print(unique_elements)