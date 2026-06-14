'''
keys() method in Python returns a view object that contains all the keys of the dictionary. 
The returned object is dynamic, meaning any changes made to the dictionary are automatically reflected in the view. 
'''
inventory = {
    'apples' : 430,
    'bananas' : 312,
    'oranges' : 525,
    'mangoes': 132
}

for key in inventory.keys():
    print(key)