#Recursive Fibonacci: Find the $n$-th Fibonacci number using recursion. 

def fibonacci(n):
    if n<= 1:
        return n
    return fibonacci(n - 1)  + fibonacci(n - 2)

n= int(input("Enter position :"))
print("Fibonacci number =",fibonacci(n))