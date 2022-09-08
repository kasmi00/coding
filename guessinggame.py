#random number guessing game

import random

number = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess the number:"))
    if user == number:
        print("Congratulations you won the game!")
        print(f"{number}is the correct guess")
        break
if user !=number:
    print(f"Your guess is incorrect,{number} is the right guess")

