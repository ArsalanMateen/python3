# masking sensitive information (e.g credit cards)
cardNum = '1234 5678 9810 1112'
maskedNum = '*' * 8 + cardNum[-4:]

print("Payment Successful using the card", maskedNum)