from random import choice

rock = "rock"
paper = "paper"
scissors = "scissors"

cpuChoice = choice((rock, paper, scissors))
userChoice = input("what do you want to play? rock, paper, or scissors? ")
print("computer played", cpuChoice)

if userChoice == "rock":
    if cpuChoice == rock:
        print("you tied")
    elif cpuChoice == paper:
        print("you lost")
    else:
        print("you won")
elif userChoice == "paper":
    if cpuChoice == rock:
        print("you won")
    elif cpuChoice == paper:
        print("you tied")
    else:
        print("you lost")
elif userChoice == "scissors":
    if cpuChoice == rock:
        print("you lost")
    elif cpuChoice == paper:
        print("you won")
    else:
        print("you tied")
else:
    print("invalid input, try again")