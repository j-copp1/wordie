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
        for letter in word :
            if letter != '\n' :
                totalWordValue = totalWordValue + letterFreq[letter]
        wordRankings.append([totalWordValue, word[0:len(word) - 1 ]])
    return sorted(wordRankings, key=lambda x: x[0], reverse=True)

# def letterCheck(wordRankings, responseLetter, responseLetterStatus) :

#     newWordRankings = []

#     # for word in wordRankings

#     for word in wordRankings : 
#         for i, letter in enumerate(word[1]) :
#             #skip if letter contains any grey letters 
#             #add if has any green letter

#     # return newWordRankings

def letterCheck(wordRankings, slot, currResponseLetter) :

    
    # newerWordRankings = []

    for index, word in enumerate(wordRankings) :
        #check letter


        # print(word)
        # print(word[1][slot], currResponseLetter[0])

        # 0 - green
        # 1 - yellow
        # 2 - grey
        
        # word
        # [8747, 'muzzy']

        # slot 
        # currResponseLetter
        # 4
        # ['u', '2']

        #grey
        if int(currResponseLetter[1]) == 2 and word[1][slot] == currResponseLetter[0]:
            print(index, word)
            wordRankings.remove(index)
            # if int(currResponseLetter[1]) == 0 :
            #     newWordRankings.append(word)



        # if currResponseLetter[1] == 2 and word[1][slot] == currResponseLetter[0] :
        #     print(word)

        # if currResponseLetter[1] == 2 and word[1][slot] != currResponseLetter[0] :
        #     #
        


        # #check green
        # if int(currResponseLetter[1]) == 0 and word[1][slot] == currResponseLetter[0] : 
        #     newWordRankings.append(word)
        # #check grey
        # elif int(currResponseLetter[1]) == 2 and word[1][slot] != currResponseLetter[0] :
        #     newWordRankings.append(word)
        # #check yellow 
        # elif int(currResponseLetter[1]) == 1 and currResponseLetter[0] in word[1] and word[1][slot] != currResponseLetter[0]:
        #     newWordRankings.append(word)
        # print('fuck')
    
    # if int(currResponseLetter[1]) == 1 :
    #     newerWordRankings = []
    #     for word in newWordRankings :
    #         if(currResponseLetter[0] in word[1]) :
    #             newerWordRankings.append(word)
    #     return newerWordRankings


    # for word in newWordRankings :
    #     if int(currResponseLetter[1]) == 1 : 
    #         newerWordRankings.append(word)


    return wordRankings

def findBestWord(currResponse, wordRankings) :

    word = ''

    #green slots, currResponse[x][1] == 0

    newWordRankings = []

    # for word in wordRankings :
    #     for index, letter in enumerate(word[1]): 
    #         print(letter, currResponse[index][1],currResponse[index][1] == 0, currResponse[index][0], currResponse[index][0] == letter)
    #         if currResponse[index][1] == 0 :
    #             if currResponse[index][0] == letter :
    #                 print(word)

    newWordRankings = wordRankings

    for slot, currResponseLetter in enumerate(currResponse) :
        # print("->", len(newWordRankings))
        newWordRankings = letterCheck(newWordRankings, slot, currResponseLetter)
        # print("<-", len(newWordRankings))
    
    # print(newWordRankings)


    #eliminate words
        #green slots
        #yellow slots
        #not there
        #not in specific slots

    #return best word lol

    return word, newWordRankings

def main():

    # #life cycle 
    # userInput = ''
    # while (userInput != 'x') :
    #     userInput = input()
    #     if userInput == 'x':
    #         print("closing")
    #     else :
    #         print("fuck")

    #all possible wordle words
    wordList = loadList()
    #frequency rankings of letters
    letterFreq = getLetterFreq(wordList)
    #ranking of words to choose from highest combined letter freq
    wordRankings = getWordRankings(wordList, letterFreq)



    #find best word

    ## 0 = correct letter -> green
    ## 1 = misplaced -> yellow
    ## 2 = wrong / excluded -> grey

    #response structure
    currResponse = [
        ['p', '0'],
        ['i', '0'],
        ['n', '0'],
        ['t', '2'],
        ['e', '1'],
    ]

    # currResponse = [
    #     ['b', '0'],
    #     ['o', '0'],
    #     ['o', '0'],
    #     ['s', '2'],
    #     ['t', '2'],
    # ]

    userInput = ''
    while (userInput != 'x') :
        userInput = input()
        if userInput == 'x':
            print("closing")
        else :
            print('hello')
            currResponse = [
                [userInput[0], userInput[5]],
                [userInput[1], userInput[6]],
                [userInput[2], userInput[7]],
                [userInput[3], userInput[8]],
                [userInput[4], userInput[9]]
            ]
            print(len(wordRankings))
            word, wordRankings = findBestWord(currResponse, wordRankings)
            print(wordRankings[0:5])
            print(len(wordRankings))

    # print(len(wordRankings))

    # word, newWordRankings = findBestWord(currResponse, wordRankings)

    # print(len(newWordRankings))

    # print(letterFreq)

if __name__ == "__main__":
    main()
