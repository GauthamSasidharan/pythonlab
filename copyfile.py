# Write a Python program to copy the contents of a file to another file .


with open('firsttest.txt','r') as firstfile, open('secondtest.txt','a') as secondfile:
 
 # read content from first file
 for line in firstfile:
   
   # append content to second file
   secondfile.write(line)
