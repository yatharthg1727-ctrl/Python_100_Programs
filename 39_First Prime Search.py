#  First Prime Search: Search for the first prime number in a range and break the loop when found.

start = int(input("Enter start:"))
end = int(input("enter end:"))

for n in range(start,end +1):

    if n < 2:
        continue
    prime = True

    for i in range(2, n):
        if n% i ==0:
            prime = False
            break

    if prime:
        print("First prime =", n)
        break