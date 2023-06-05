import os, string, sys, time

#paths
base_d = os.path.dirname(__file__)+os.path.sep
src_f = "twl06FiveLetter.txt"

#class to store counts
class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.count = 0
        self.pos = -1
class Word:
    def __init__(self,word):
        self.word = word.rstrip()
        self.len = len(self.word)
        self.posCount = 0
        self.contDup = False
        self.valid = True
        self.checkValid()
        if self.valid:
            self.checkForDup()
    def __str__(self):
        return self.word + " " + str(self.posCount)
    def __repr__(self):
        return self.word + " " + str(self.posCount)
    def checkValid(self):
        for c in self.word:
            if c not in string.ascii_lowercase:
                self.valid = False
        if len(self.word) == 0:
            self.valid = False
    def checkForDup(self):
        for c in self.word:
            if self.word.count(c) > 1:
                self.contDup = True

#search function
def findWord(inc_list,exc_list):
    if type(inc_list) != type([]):
        raise TypeError("inc_list must be a list!")
    if type(exc_list) != type([]):
        raise TypeError("exc_list must be a list!")
    for inc in inc_list:
        if inc not in string.ascii_lowercase:
            raise ValueError("The character",inc,"in inc_list is not valid, must be an ascii lower case char.")
    for exc in exc_list:
        if exc not in string.ascii_lowercase:
            raise ValueError("The character",exc,"in exc_list is not valid, must be an ascii lower case char.")
    for w in sortedNoDupWordList:
        #check if word contains a letter in the exclude list
        cont = False
        for exc in exc_list:
            if exc in w.word:
                cont = True
        if cont:
            continue
        #check if word contains all letters in include list
        cont = False
        if len(inc_list) == 0:
            return w
        for inc in inc_list:
            if inc not in w.word:
                cont = True
        if cont:
            continue
        return w
    print("No word found matching both include list:",inc_list, "and exclude list:",exc_list)
    return -1
def findAnag(word):
    if type(word) != type('a string!'):
        raise TypeError("Must pass a string!")
    for w in sortedNoDupWordList:
        if len(w.word) != len(word):
            continue
        for c in word:
            if c not in w.word:
                continue
        print(w.word)

def bestLetterPos(word):
    posCntDict = {}    
    for c in word:
        posCntDict[c] = 0
    for i,c in enumerate(word):
        for w in wordList:
            print(w)
            if type(w) != type(''):
                continue
            if c == w.word[i]:
                posCntDict[c] += 1
    print("Count for "+word)
    print("===============")
    for c in posCntDict.keys():
        print(c,str(posCntDict[c]))
    sum=0
    for v in posCntDict.values():
        sum += v
    print("Total: "+str(sum))


#list of Letter objects
letterList = []
for char in string.ascii_lowercase:
    letterList.append(Letter(char))
def getCnt(letter):
    if len(letter) != 1:
        return -1
    if letter not in string.ascii_lowercase:
        return -1
    for ltr in letterList:
        if ltr.letter == letter:
            return ltr.pos
    return -1
#search src file and count how many words each letter appears in
#also create Word for each and mark if word contains duplicate letter or not
wordList = []
noDupWordList = []
with open(base_d+src_f,'r') as src:
    line = ' '
    while len(line) > 0:
        line = src.readline()
        for c in letterList:
            if c.letter in line:
                c.count += 1
        newWord = Word(line)
        wordList.append(newWord)
        if newWord.contDup == False:
            noDupWordList.append(newWord)
#sort letter list
sortedLetterList = sorted(letterList, key=lambda x: x.count, reverse=True)
print()
print('Letter List')
print('===========')
for i in sortedLetterList:
    i.pos = sortedLetterList.index(i)
    print(i.letter, i.count, i.pos)
print()

#get the letter count totals for each word
print('Length of wordList =',len(wordList))
print('Length of noDupWordList =',len(noDupWordList))
print()
for w in noDupWordList:
    for c in w.word:
        cnt = getCnt(c)
        if cnt == -1:
            w.posCount = -1
            break
        w.posCount += cnt

#sort noDupWordList list
print("Top Ten Worst Words")
print("===================")
sortedNoDupWordList = sorted(noDupWordList, key=lambda x: x.posCount, reverse=True)
for i in range(10):
    print(sortedNoDupWordList[i].word, sortedNoDupWordList[i].posCount)
    
print("Top Ten Best Words")
print("==================")
sortedNoDupWordList = sorted(noDupWordList, key=lambda x: x.posCount)
if sortedNoDupWordList[0].posCount == 0:
    sortedNoDupWordList.pop(0)
for i in range(10):
    print(sortedNoDupWordList[i].word, sortedNoDupWordList[i].posCount)
print()
#best word
bestWord = sortedNoDupWordList[0]
print("Best word:",bestWord)
#next best word not cotaining any of those letters
nextBestWord = findWord([],list(sortedNoDupWordList[0].word))
print("Next Best word:",nextBestWord)
#Best words with a single match
print("Best Words with a single hit from",sortedNoDupWordList[0].word,":")
svList = list(sortedNoDupWordList[0].word)
for c in svList:
    cList = svList[:]
    cList.remove(c)
    print(c,findWord([c],cList))

bestLetterPos(bestWord.word)