# Create the Rock-Paper-Scissors game
# - Play against AI
# - Play against another player
# - Grabs 1 or more users input depending on game version they play
# - AI will be based off a random number and depending on that number will result in getting 1 of the 3 options
import random

robotNum = random.randint(1,3)

decisionList = ["Rock", "Paper", "Scissors"]

def robotVsPlayer():
    global robotNum
    global decisionList
    

# def playerVsPlayer():


def main():
    robotVsPlayer()

main()