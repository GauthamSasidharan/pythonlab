#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

n=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)