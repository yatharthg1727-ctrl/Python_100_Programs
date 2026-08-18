#  Largest of Three Numbers: Determine the maximum among three numbers using nested ifelse.

x= int(input("Enter the first number:"))
y= int(input("Enter the second number:"))
z= int(input("Enter the third number:"))

if x>=y:
    if x>=z:
      largest = x
    else:
       largest = z

else:
   if y>=z:
      largest = y
   else:
        largest =z

print("Largest number = ",largest)