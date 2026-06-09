'''
insert() method is used to add an element at a specific position in a list. Unlike append() which adds elements only at the end, insert() allows adding elements anywhere in the list using an index and updates the original list

.insert(index, element)

index: position where the element will be inserted.
element: value to be added to the list.
'''

fruits = ['apple', 'cherry', 'mango', 'banana', 'orange', 'watermelon', 'strawberry']
fruits.insert(fruits.index('watermelon'), 'peach')
print(fruits)