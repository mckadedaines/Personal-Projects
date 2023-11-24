# Develop a game where the computer randomly selects a number, and the user has to guess it.
# Steps needed:
# - import random and store random int it in a variable
# - prompt the user to guess
# - Check to see if the users guess equals the random number
# - Add checks to guide the user to the correct answer. If they enter anything other then a number then it will through and invalid response and make them guess again.

import random

def main():
    print("Welcome to the Random Number Game!")

    randomNum = random.randint(0, 10)

    while True:
        try:
            userGuess = int(input("Please guess a number from 0 - 10: "))

            if(userGuess == randomNum):
                print("Congrats! You guessed the correct number!")
                break
            elif (userGuess < randomNum):
                print("Guess Higher.")
            elif (userGuess > randomNum):
                print("Guess Lower.")
        except ValueError:
            print("Invalid Input. Please enter a number.")

main()