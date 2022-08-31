# Ask the user for a string and print out whether this string is a palindrome or not

a=input("Enter the string:")
b=a[::-1]
if a == b:
  
	print(a, " is a palindrome")

else:
  
	print(a, " is not a palindrome")
