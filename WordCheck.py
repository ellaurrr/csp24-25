
def checkFive(wordsList):
    for word in wordsList:
        if (len(word) > 5):
            wordsFive.append(word)
    return(wordsFive)

#main
wordsFive = [] #empty list for words with 5+ letters

listWords = ["matcha", "espresso", "latte", "water", "milk", "coffee", "tea", "gatorade", "boba", "celsius"]
print(checkFive(listWords))


