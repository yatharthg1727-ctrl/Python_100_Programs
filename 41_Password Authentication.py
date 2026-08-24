#  Password Authentication: Loop indefinitely for input password; break on correct entry, retry on incorrect.

correct_password = "billionaire120$"

while True:
    password = input("Enter password:")

    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect password")