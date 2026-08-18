# Swapping without Third Variable: Swap two variables using pythonic assignment (a, b = b, a) and arithmetic operations.

x= int(input("Enter the x:"))
y = int(input("Enter the y:"))

print("Before swapping: x=",x,"y=",y)

x,y = y,x
print("After swapping: x=",x,"y=",y)

# using arithmetic operation  
x= x+y
y=x-y
x=x-y
print("After swapping: x=",x,"y=",y)