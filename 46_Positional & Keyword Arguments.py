#  Positional & Keyword Arguments: Create a function calculating total bill with price, tax, and discount using keyword arguments.

def total_bill(price, tax, discount):
    total = price + (price * tax/ 100) - (price * discount / 100)
    return total

print(total_bill(1000, tax=10, discount=5))