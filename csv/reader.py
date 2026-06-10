'''
next() function returns the next item from an iterator.
syntax: next(iterator, default)

iterator: an iterator object to get the next item from.
default: (Optional) Value returned if the iterator is exhausted. If not provided, StopIteration is raised.
'''

import csv

with open('olympics.csv', 'r') as file:
    reader = csv.reader(file) # csv.reader() function reads the CSV file line by line and returns each row as a list.

    header = next(reader)
    print(header)

    for row in reader:
        if row[5] != 'NA':
            print(f'{row[0]}: {row[4]}, {row[5]}')