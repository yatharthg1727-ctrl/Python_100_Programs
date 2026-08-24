# Fibonacci Series: Print the first $N$ terms of the Fibonacci sequence using an iterative loop.

n= int(input("enter a number:"))

a = 0
b = 1

for i in range(n):

    print(a,end=" ")

    a,b = b,a+b