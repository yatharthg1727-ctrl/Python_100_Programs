#  Default Arguments: Write a function power(base, exponent=2) that calculates squares by default unless an exponent is passed.

def power(base, exponent = 2):

    return base ** exponent

print(power(5))
print(power(5, 3))