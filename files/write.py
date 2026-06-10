file = open('squares.txt', 'w')

for number in range(10):
    square = number**2
    file.write(str(square)+'\n')

file.close()