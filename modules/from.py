from random import random

fraction = random()

# random floating values b/w custom range
max = 100 
min = 0
float = fraction * (max - min) + min
print("The random float b/w 0 and 100 is: ", round(float, 2))

# an alternatiive way of fixing a floating values to a certain decimal places
# print ("The random float b/w 0 and 100 is: ", "{:.2f}".format(float))
