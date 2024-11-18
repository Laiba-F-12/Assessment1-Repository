Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# list of names
>>> names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
>>> search_name = "Sam"
# check the entered name if it is found in the list
>>> if search_name in names:
...     print(f"{search_name} is found.")
... else:
...     print(f"{search_name} is not found.")
... 
...     
Sam is found.
