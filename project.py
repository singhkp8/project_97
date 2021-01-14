import random

Guess = random.randint(0,10)

userGuess = int(input("Enter Your Guess :- \n"))

if (Guess == userGuess):
    print("You Won")
    print("Your Guess is :- " + userGuess)
    print(Guess)
elif(Guess != userGuess):
    print("You Lose")
