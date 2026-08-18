# ASCII Value Finder: Input a character and display its ASCII value using ord(), then convert an ASCII value back using chr().

# ASCII Value Finder

ch = input("Enter a character: ")

# Convert character to ASCII value
ascii_value = ord(ch)
print("ASCII value of", ch, "is:", ascii_value)

# Convert ASCII value back to character
num = int(input("Enter an ASCII value: "))

character = chr(num)
print("Character for ASCII value", num, "is:", character)