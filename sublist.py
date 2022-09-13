# Write a Python program to generate all sublists of a list.
list = list()
result = list()

size = (input('Enter the size of the list :'))

print('Enter all elements of the list :')

for i in range(size):
    list.append((input('Enter element to add : ')))

for i in range(len(list) + 1):
    for j in range(i + 1, len(list) + 1):
        list.append(list[i:j])

print(list)
print(result)