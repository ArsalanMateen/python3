file = open('olympics.txt', 'r')
content = file.read() # return the entire contents of the file as a single string
print(content[:50])
file.close()