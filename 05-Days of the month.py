Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# dictionary of months and days
>>> month_days = {
...     1: 31,  #January
...     2: 28,  #February (non-leap year)
...     3: 31,  #March
...     4: 30,  #April
...     5: 31,  #May
...     6: 30,  #June
...     7: 31,  #July
...     8: 31,  #August
...     9: 30,  #September
...     10: 31,  #October
...     11: 30,  #November
...     12: 31,  #December
... }
# take input from user as their choice
>>> month = int(input("Enter the month number: "))
Enter the month number: 3
# check with the dictionary if month number is valid
>>> if month in month_days:
...     print(f"We have {month_days[month]} days of month {month}.")
... else:
...     print("Invalid month number. Please enter a number between 1 and 12.")
... 
...     
We have 31 days of month 3.
