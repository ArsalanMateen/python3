'''
Lambda functions are small anonymous functions, meaning they do not have a defined name. These are small, short-lived functions used to pass simple logic to another function.

Contain only one expression.
Result of that expression is returned automatically (no return keyword needed).
'''

num = int(input("Enter you number: "))
square = lambda num: num**2
print(square(num))