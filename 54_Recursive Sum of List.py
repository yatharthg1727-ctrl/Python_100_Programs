# Recursive Sum of List: Compute the sum of a numeric list recursively.

def list_sum(n):
    if len(n) ==0:
        return 0
    return n[0] + list_sum(n[1:])

n= [10,30,40,20]
print("Sum =",list_sum(n))