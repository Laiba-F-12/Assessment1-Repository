Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# store correct password in the program
>>> correct_password = "12345"
# use while loop to repeatedly ask the userr for correct password until the correct one is entered
>>> while True:
...     user_input = input("Please enter the password: ")
...     if user_input == correct_password:
...         print("Access granted!")
...         break
...     else:
...         print("Incorrect password. Please try again.")
... 
...         
Please enter the password: 123
Incorrect password. Please try again.
Please enter the password: 789
Incorrect password. Please try again.
Please enter the password: 1234
Incorrect password. Please try again.
Please enter the password: 12345
Access granted!
