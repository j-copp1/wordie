def loadList():
    # opening the file in read mode 
    my_file = open("wordle-nyt-words-14855.txt", "r") 

    data = my_file.readlines()

    my_file.close() 

    return(data)

def getLetterFreq(wordList) :

    letterFreq = {}

    for word in wordList :
        for letter in word :
            #ignore end of line letter
            if (letter != '\n') :
                #check if letter added 
                if letter in letterFreq.keys() :
                    letterFreq[letter] = letterFreq[letter] + 1
                else : 
                    letterFreq.update({letter : 1})
    return letterFreq

def getWordRankings(wordList, letterFreq) :

    wordRankings = []

    for word in wordList :
        totalWordValue = 0
        uniqueLetters = []
        for letter in word :
            if letter != '\n' and letter not in uniqueLetters:
                totalWordValue = totalWordValue + letterFreq[letter]
                uniqueLetters.append(letter)
        wordRankings.append([totalWordValue, word[0:len(word) - 1 ]])
    return sorted(wordRankings, key=lambda x: x[0], reverse=True)

def getBestWord(currResponse, wordRankings, greens, yellows, greys) :

    newWordRankings = []

    for slot, letter in enumerate(currResponse) :
        
        if int(letter[1]) == 0 :
            greens.append([slot, letter[0]])
            if letter[0] in yellows.keys() :
                yellows.pop(letter[0])
        elif int(letter[1]) == 1 :
            if letter[0] not in yellows :
                yellows.update({letter[0] : [slot]})
            else :
                yellows[letter[0]].append(slot)
            pass
        else :
            greys.append(letter[0])

    print('greens => ', greens)
    print('yellows =>', yellows)
    print('greys =>', greys)

    # for word in [[0,'riser'],[3, 'inter']] :
    for word in wordRankings :
        addCheck = True

        #grey check
        for grey in greys :
            if grey in word[1] :
                addCheck = False

        #green check
        for green in greens : 
            if green[1] != word[1][green[0]] :
                addCheck = False

        #yellow check slot

        for yellow in yellows :
            for slot in yellows[yellow] :
                if word[1][slot] == yellow :
                    addCheck = False

        #yellow check full
        for yellow in yellows :
            temp = []
            for index, letter in enumerate(word[1]) :
                addToTemp = True
                if index in yellows[yellow] :
                    addToTemp = False
                else :
                    for green in greens : 
                        if index == green[0] :
                            addToTemp = False
                if addToTemp :
                    temp.append(letter)

            if yellow not in temp :
                addCheck = False

        if addCheck : 
            newWordRankings.append(word)

    return newWordRankings, greens, yellows, greys

def wordieRun(wordRankings) :

    #greens [slot, letter]
    greens = []
    #yellows {letter : [0, 1, ...]}
    yellows = {}
    #greys [letter]
    greys = []

    userInput = ''
    while (userInput != 'x') :
        userInput = input()
        if userInput == 'x':
            print("closing")
        else :
            currResponse = [
                [userInput[0], userInput[5]],
                [userInput[1], userInput[6]],
                [userInput[2], userInput[7]],
                [userInput[3], userInput[8]],
                [userInput[4], userInput[9]]
            ]
            wordRankings, greens, yellows, greys = getBestWord(currResponse, wordRankings, greens, yellows, greys)
            print(len(wordRankings), " ------------------ ", wordRankings[0:5])

def main():

    #all possible wordle words
    wordList = loadList()
    #frequency rankings of letters
    letterFreq = getLetterFreq(wordList)
    #ranking of words to choose from highest combined letter freq
    wordRankings = getWordRankings(wordList, letterFreq)

    #run program
    wordieRun(wordRankings)

if __name__ == "__main__":
    main()
