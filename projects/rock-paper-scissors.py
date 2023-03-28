#Rock wins over the scissors
#Scissors wins over the paper
#Paper wins over the rock
from random import randint

objects = ("rock", "scissor", "paper")

computer = objects[randint(0, 2)]

while True:
    user = input("rock, paper or scissors? ").lower().lstrip()
    if user == computer:
        print("Tie!")
    elif user == "rock":
        if computer == "paper!":
            print ("You lose! - "," cover ", user)
        else:
            print ("You win! - ", user , " smashes ", computer)
    elif user == "scissors":
        if computer == "rock":
            print ("You lose! - ", computer, "smashes", user)
        else:
            print ("You win! -", user , "cut ",computer)
    elif user == "paper":
        if computer == "scissors":
            print ("You lose! - ", computer , " cut ", user)
        else:
            print ("You win! - ", user , " cover ", computer)
    else:
        print ("Invalid input!")
    computer = objects[randint(0, 2)]