#  Triangle Validity: Determine if three side lengths can form a valid triangle.

a= float(input("Enter the first side: "))
b= float(input("Enter the second side: "))
c= float(input("Enter the third side: "))

if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("invalid triangle")