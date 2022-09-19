# Write a Python program to write a list to a file.
a_list = ["abc", "def", "ghi"]
textfile = open("list.txt", "w")
for element in a_list:
    textfile.write(element + "\n")
textfile.close()