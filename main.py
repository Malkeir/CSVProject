# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

NEWLIST = []

def getLine(lineNum):
    return NEWLIST[lineNum]

def getVarLine(lineNum,value):
    val = None
    for x in NEWLIST[lineNum]:
        if value == x:
            val = x

    return val

def FindVar(value):
    val = None
    for x in NEWLIST:
        for y in x:
            if value == y:
                val = y
                break

    return (val)

def allCountsOFVar(value):
    val = []
    for x in NEWLIST:
        for y in x:
            if value == y:
                val.append(y)

    return (val , len(val))

def ParsCSV(file):
    allowence = False
    listOfchar = []
    listOfWords = []
    listOfSentences = []
    numcount = -1
    for stringOfWords in file.readlines():
        stringOfWords = stringOfWords.replace("\n",",")
        for x in stringOfWords:
            numcount +=1
            if x == "," and allowence == False:
                word = ''.join(listOfchar)
                listOfWords.append(word)
                listOfchar = []
            elif x == "'" or x == '"':
                allowence = not (allowence)
                listOfchar.append(x)
            else:
                listOfchar.append(x)
        numcount = -1
        listOfSentences.append(listOfWords)
        listOfWords = []


    return listOfSentences

def main():
    DIR = "C:/Users/dorrb/CSVProject/SampleCSVFile_556kb.csv"

    file = open(DIR)
    NEWLIST = ParsCSV(file)
    print (NEWLIST)


main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
