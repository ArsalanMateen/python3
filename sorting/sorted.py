'''
sorted() function in Python returns a new sorted list from the elements of any iterable, such as a list, tuple, set, or string. 
It does not modify the original iterable, unlike the sort() method for lists.

sorted(iterable, key=None, reverse=False)

iterable: sequence to be sorted (list, tuple, set, string, etc.)
key (Optional): function to customize the sort order.
reverse (Optional): If True, sorts in descending order.
'''

fruits = ["apple", "banana", "cherry", "date"]
print(sorted(fruits, key=len)) # ['date', 'apple', 'banana', 'cherry']