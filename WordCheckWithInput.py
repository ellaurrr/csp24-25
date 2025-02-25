
def checkFive(wordsList):
    for word in wordsList:
        if (len(word) > 5):
            wordsFive.append(word)
    return(wordsFive)

#main
wordsFive = [] #empty list for words with 5+ letters

listWords = input("give me words to check if it is 5 letters or more: ").split()
print(checkFive(listWords))


