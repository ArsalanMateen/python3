'''
pop() method removes and returns an element from a list. By default, it removes the last item, but we can specify an index to remove a particular element. It directly modifies the original list.
'''
cars = ['BMW', 'Honda', 'GMC', 'Toyota', 'KIA', 'Mercedes']
ROKbrand = cars.pop(cars.index('KIA'))
print (ROKbrand)