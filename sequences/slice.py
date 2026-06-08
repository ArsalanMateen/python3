'''
Slicing allows you to extract a portion of a sequence (like a list, tuple, or string) by specifying a start index, an end index, and an optional step. 
The syntax for slicing is: [start:end:step]

start: The index where the slice starts (inclusive). If omitted, it defaults to 0.
end: The index where the slice ends (exclusive). If omitted, it defaults to the length of the sequence.
step: The interval between elements in the slice. If omitted, it defaults to 1.
'''

fullName = 'Arsalan Mateen'

# extract last name using slicing by identifying the index of the space character
spaceIndex = fullName.find(' ')
lastName = fullName[spaceIndex + 1:]
print(lastName)
