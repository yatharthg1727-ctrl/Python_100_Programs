# Sum of Digits: Calculate the sum of individual digits of an integer.

n= int(input("Enter a number:"))

total = 0
while n>0:
    digit = n%10
    total += digit
    n//= 10

print("Sum of digits= ",total)