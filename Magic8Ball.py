import random
import time

def quit():    #function to send a quit message in the program
    print("ok bye!")

#list for the possible responses
responseList = ["it is certain","it is decidedly so","without a doubt","yes definitely","you may rely on it",
            "as i see it, yes", "most likely", "outlook good", "yes", "signs point to yes", "dont count on it",
            "my reply is no", "my sources say no", "outlook not so good", "very doubtful", "reply hazy, try again",
            "ask again later","better not tell you now","cannot predict now","concentrate and ask again"]

print("welcome to the magic 8 ball!")
while (True): #true while loop that will only leave with a break
    print("would you like to ask a question? y/n")
    play = input()
    if (play == 'y' or play == "Y"):
        print("what is your question?")
        question = input()
        time.sleep(2)
        print("one sec... im still thinking")
        time.sleep(3)
        response = random.choice(responseList)
        print(response)

    elif (play == 'n' or play == "N"):
        quit()
        break #break to leave loop

    else: #catches all non "y/Y" or "n/N" responses
        print("thats not the what im looking for! try again with y or n")
