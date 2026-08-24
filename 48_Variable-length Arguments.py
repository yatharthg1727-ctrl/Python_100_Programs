#  Variable-length Arguments (*args): Write a function that accepts any number of numerical arguments and returns their sum.

def add_numbers(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add_numbers(10,20,30,40))