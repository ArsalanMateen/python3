'''
replace() method returns a new string where all occurrences of a specified substring are replaced with another substring. It does not modify the original string because Python strings are immutable.

.replace(old, new, count)

old: substring to be replaced.
new: substring to insert in place of old.
count (optional): maximum number of replacements. If not provided, all occurrences are replaced.
'''

receipt = 'Hello {NAME}, your order {ORDER_ID} has shipped!'
email = receipt.replace("{NAME}", "Alice").replace("{ORDER_ID}", "#98765")
print(email) 