from collections import OrderedDict
from itertools import combinations

class word:
    def __init__(self, phrase):
        self.phrase = phrase
    def createList(self):
        return(list(self.phrase))
    def display(self):
        print(self.createList())
    def findCombinations(self, string, pattern):
        dict = OrderedDict.fromkeys(string) 
        ptrlen = 0
        strlen = len(string)

        for key,value in dict.items(): 
            if (key == pattern[ptrlen]): 
                ptrlen += 1
            for x in range (strlen**6):
                arr = []
                newlist = list(combinations(string, strlen))
                for item in newlist:
                    if item in arr:
                        pass
                    else:
                        arr.append(item)
                        num = len(arr)
                print(arr)
                print(num)
'''
            # if (ptrlen == (len(pattern))):
                for x in range (len(pattern)**2):
                    newlist = random.sample(string, len(string))
                    print(newlist)
                else:
                    break
'''



userChoice = input("What is the word you would like to check?: ").upper()
userPattern = input("What is the pattern you would like to check?: ").upper()
w = word(userChoice)
W = w.createList()
w.findCombinations(W, userPattern)
print(w.ptrlen)

