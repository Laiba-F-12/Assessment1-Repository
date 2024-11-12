Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# ask the user a question
>>> question = "What is the capital of France?"
# store the correct answer in the program
>>> correct_answer = "Paris"
>>> user_answer = input(question + " ")
What is the capital of France? Paris
# check if answer is correct
>>> if (user_answer) == correct_answer:
...      print("Correct! Well done.")
... else:
...     print("Incorrect. The right answer is Paris.")
... 
...     
Correct! Well done.
