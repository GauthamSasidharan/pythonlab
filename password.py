import random

print('hello, Welcome to Password generator!')
length = int(input('\nEnter the length of password: '))
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lower= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
 
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                    
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
           
all = lower + upper + nums + symbols
temp = random.sample(all,length)

password = "".join(temp)
print(password)


