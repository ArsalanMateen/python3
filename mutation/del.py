'''
del Keyword removes the reference to an object. If that object has no other references, it gets cleared from memory. Trying to access a deleted variable or object will raise a NameError.
'''
fruits = ['apple', 'cherry', 'mango', 'banana', 'orange', 'watermelon', 'strawberry']

del fruits[fruits.index('watermelon')]
print(fruits)

del fruits
print(fruits) # error
