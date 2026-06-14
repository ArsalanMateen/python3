'''
get() method in Python returns the value associated with a given key. 
If the key is not present, it returns None by default or a specified default value if provided. 
It allows safe access to dictionary keys without raising a KeyError.

get(key, default)

key: key whose value needs to be retrieved.
default: value returned if the key is not found. Default is None.
'''

cart = {
    "item_name": "Wireless Headphones",
    "price": 99.99,
    "quantity": 1
}

# No crash: safely defaults to 0.0 if 'discount' is missing
discount = cart.get("discount", 0.0)

print(f"Discount: ${discount}") # Output: Discount: $0.0
