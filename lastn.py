f = open("test.txt", "r")
lines = f.readlines()
last_lines = lines[-3:]
print(last_lines)