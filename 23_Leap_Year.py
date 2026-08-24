# .Leap Year Checker: Determine whether a given year is a leap year.

year = int(input("Enter the year:"))

if (year%400 == 0) or (year %4 == 0 and year% 100!=0):
    print("Lear year")

else:
    print("Not a leap year")