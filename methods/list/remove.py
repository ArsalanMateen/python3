'''
remove() function removes the first occurrence of a given item from list. It make changes to the current list. It only takes one argument, element we want to remove and if that element is not present in the list, it gives ValueError.
'''

cars = ['BMW', 'Honda', 'GMC', 'Toyota', 'KIA', 'Mercedes']
cars.remove('KIA')
print (cars)