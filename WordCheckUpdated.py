
def checkFive(wordsList,minL):
    for word in wordsList:
        if (len(word) > 5):
            wordsFive.append(word)
    return(wordsFive)

#main
wordsFive = [] #empty list for words with 5+ letters

length = input("what is the minimum length of each word that you want?")
listWords = input("give me words to check if it is " + length + " letters or more: ").split()
print(checkFive(listWords,length))


