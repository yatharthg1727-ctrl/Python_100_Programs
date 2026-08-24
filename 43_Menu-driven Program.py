#  Menu-driven Program: Implement a simple continuous menu (Add, Subtract, Exit) using while True and break.

while True:
    print("\n 1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = int(input("Enter a choice:"))
    if choice == 3:
        print("Program ended")
        break
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))

    if choice == 1:
        print("Result = ",a+b)

    elif choice == 2:
        print("Result =",a-b)

    else:
        print("Invalid choice")
