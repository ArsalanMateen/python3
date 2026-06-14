'''
sort() method in Python is used to arrange the elements of a list in a specific order. 
It works only on lists, modifies the original list in place, and does not return a new list.

.sort(key=None, reverse=False)

key: function that decides how elements are compared.
reverse: If True, sorts the list in descending order.
'''

list = [ {"name": "Jake", "age": 30},
      {"name": "Joe", "age": 25},
      {"name": "Justin", "age": 35} ]

list.sort(key=lambda x: x["age"])
print(list) 