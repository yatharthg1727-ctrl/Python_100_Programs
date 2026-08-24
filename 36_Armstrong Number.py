# .Armstrong Number: Check if a number is equal to the sum of its digits raised to the power of the number of digits.

n= int(input("Enter a number:"))

original = n
digits = len(str(n))
total = 0

while n>0:
    digit = n % 10
    total += digit ** digits
    n //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")