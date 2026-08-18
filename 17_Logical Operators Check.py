# Logical Operators Check: Evaluate logical and, or, and not operations on multiple user conditions.

a= int (input("Enter the condition (0 or 1): "))
b = int(input("Enter the condition (0 or 1):"))

condition1 = bool(a)
condition2 = bool(b)

print("AND:", condition1 and condition2)
print("OR:", condition1 or condition2)
print("NOT condition1:", not condition2)
print("NOT condition2:", not condition1)