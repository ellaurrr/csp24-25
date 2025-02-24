
def checkFive(wordsList):
    for word in wordsList:
        if (len(word) > 5):
            wordsFive.append(word)
    return(wordsFive)

#main
wordsFive = [] #empty list for words with 5+ letters

stringWords = "water matcha espresso coffee tea latte gatorade boba celsius" #string of words
listWords = stringWords.split() #splits string by spaces
print(checkFive(listWords))

