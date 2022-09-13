# Write a Python program to get the key, value and item in a dictionary.
#  eg:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key  value  items")
for count, (key, value) in enumerate(dict_num.items()):
    print(key,'   ',value,'    ', count)