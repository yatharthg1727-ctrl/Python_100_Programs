# .Reverse a Number: Reverse an input integer using a while loop (e.g., $123 \rightarrow 321$).

n= int(input("Enter a number:"))

reverse =  0
while n>0:
    digit = n%10
    reverse = reverse *10+digit

    n//=10

print("Reverse =",reverse)