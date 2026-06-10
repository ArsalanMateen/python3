file = open('olympics.txt', 'r')
lines = file.readlines() # return a list of strings, one string for each line in the file
print(lines[:50])
file.close