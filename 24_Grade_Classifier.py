# Grade Classifier: Classify marks (0-100) into grades (A, B, C, D, Fail) using if-elif-else.

marks = float(input("Enter the marks(0-100):"))

if marks <0 or marks >100:
    print("Invalid marks")

elif marks >=90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >=60:
    print("grade C")
elif marks >=40:
    print("Grade D")

else:
    print("Fail")