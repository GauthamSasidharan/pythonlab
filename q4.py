
# Write a python program to count repeated characters in a string.

print("Enter the String: ")
string = str(input())
dictionary = {}
for char in string:
    if( char in dictionary.keys()):
        dictionary[char] += 1
    else:
        dictionary[char]=1
for char in dictionary:
    print(char,' -- ',dictionary[char])