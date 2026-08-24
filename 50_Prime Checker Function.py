#  Prime Checker Function: Write a function returning True if a number is prime and False otherwise.

def is_prime(n):

    if n < 2:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False

        return True

number = int(input("Enter a number:"))

if is_prime(number):
    print("True - Prime Number")
else:
    print("False - not a prime number")