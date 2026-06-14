'''
items() method in Python returns a view object containing all key-value pairs of the dictionary as tuples. 
This view updates automatically when the dictionary is modified.
'''

cart = {
    "Wireless Mouse": 2,
    "Mechanical Keyboard": 1,
    "USB-C Cable": 3
}

# Pricing database
prices = {
    "Wireless Mouse": 25.00,
    "Mechanical Keyboard": 90.00,
    "USB-C Cable": 10.00
}

bill = 0.0

for product, quantity in cart.items():
    unitPrice = prices.get(product, 0.0)
    itemTotal = unitPrice * quantity
    bill += itemTotal
    print(f"{product} x {quantity}: ${itemTotal:.2f}")

print(f"Total Amount Due: ${bill:.2f}")