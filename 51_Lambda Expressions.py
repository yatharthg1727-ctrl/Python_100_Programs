# Lambda Expressions: Use a lambda function to compute the square and cube of a number.

n = int(input("Enter a number: "))

square = lambda x: x * x
cube = lambda x: x * x * x

print("Square =", square(n))
print("Cube =", cube(n))