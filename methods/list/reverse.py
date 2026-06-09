'''
The reverse() method is an inbuilt method in Python that reverses the order of elements in a list. 
This method modifies the original list and does not return a new list, which makes it an efficient way to perform the reversal without unnecessary memory uses.
'''

fruits = ['apple', 'cherry', 'mango', 'banana', 'orange', 'watermelon', 'strawberry']
fruits.reverse()
print(fruits)

# reverse using slicing 
fruits = fruits[::-1]
print(fruits)