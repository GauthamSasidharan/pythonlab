# Write a Python program to count the number of characters (character frequency) in a string.

str1 = input ("Enter the string: ")
d = dict()
for i in str1:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)