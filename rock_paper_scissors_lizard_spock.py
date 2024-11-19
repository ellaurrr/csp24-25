from random import choice

rock = "rock"
paper = "paper"
scissors = "scissors"
spock = "spock"
lizard = "lizard"

cpuOption = ["rock", "paper", "scissors", "spock", "lizard"]

doItAgain = "n"

while (True):
    print("do you want to play? y/n")
    doItAgain = input()
    if (doItAgain == "y" or doItAgain == "Y"):
        cpuChoice = choice(cpuOption)
        userChoice = input("what do you want to play? rock, paper, scissors, lizard, or spock? ")
        print("computer played", cpuChoice)

        if userChoice == "rock":
            if cpuChoice == rock:
                print("you tied")
            elif cpuChoice == paper:
                print("you lost")
            elif cpuChoice == lizard:
                print ("you won") #crushes
            elif cpuChoice == spock:
                print("you lost") #vaporizes
            else:
                print("you won")
        elif userChoice == "paper":
            if cpuChoice == rock:
                print("you won")
            elif cpuChoice == paper:
                print("you tied")
            elif cpuChoice == lizard:
                print ("you lost") #eats
            elif cpuChoice == spock:
                print("you won") #disapproves
            else:
                print("you lost")
        elif userChoice == "scissors":
            if cpuChoice == rock:
                print("you lost")
            elif cpuChoice == paper:
                print("you won")
            elif cpuChoice == lizard:
                print ("you won") #decapitates
            elif cpuChoice == spock:
                print("you lost") #smashes
            else:
                print("you tied")
        elif userChoice == "lizard":
            if cpuChoice == rock:
                print("you lost")
            elif cpuChoice == paper:
                print("you won")
            elif cpuChoice == lizard:
                print ("you tied")
            elif cpuChoice == spock:
                print("you won")
            else:
                print("you lost")
        elif userChoice == "spock":
            if cpuChoice == rock:
                print("you won")
            elif cpuChoice == paper:
                print("you lost")
            elif cpuChoice == lizard:
                print ("you lost")
            elif cpuChoice == spock:
                print("you tied")
            else:
                print("you won")
        else:
            print("invalid input, try again")
    else:
        print("ok bye!")
        break