# Write a Python program to convert unix timestamp string to readable date
import datetime
print(datetime.datetime.fromtimestamp(int("1234567890"))
 .strftime('%Y-%m-%d %H:%M:%S'))
