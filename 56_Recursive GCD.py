# Recursive GCD: Compute the Greatest Common Divisor (GCD) using the Euclidean algorithm recursively.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD =", gcd(a, b))