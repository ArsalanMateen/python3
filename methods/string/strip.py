'''
strip() method in Python removes all leading and trailing whitespace by default. You can also specify a set of characters to remove from both ends. It returns a new string and does not modify the original.

.strip(char)

char: a string specifying the set of characters to remove from the beginning and end of the string.
'''

title = '** Python3 Specialization by University of Michigan **'
sanitized = title.strip('**')
print(sanitized)