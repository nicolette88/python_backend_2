import unicodedata
# pprint-et használtam a kozol kiíratáshoz.
# https://www.delftstack.com/howto/python/python-pretty-print-dictionary/
import pprint


def removeEkezet(inputStr):
    normal = unicodedata.normalize('NFKD', inputStr).encode('ASCII', 'ignore')
    return (normal.decode("utf-8"))


input = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

users = []

for item in input:
    #email cim készites
    emailCim = ""
    for index in range(len(item)):
        if ((len(item) - 1) == index):
            emailCim += "."
        emailCim += removeEkezet(item[index])
    emailCim += "@company.hu"
    #jelszo generálás
    genJelszo = item[0] + "123Start"
    #tömb feltöltés a dict-el
    tmpDict = dict(name=item, email=emailCim.lower(), password=genJelszo)
    users.append(tmpDict)

print("---1. Feladat ---")
pp = pprint.PrettyPrinter(indent=2)
print("users = ")
pp.pprint(users)

# fájl kimenet előkészítése
outputArray = []
for itemInUsers in users:
    nameStr = ""
    for nameItem in itemInUsers['name']:
        nameStr += nameItem + " "
    outputArray.append(nameStr + str(itemInUsers['email']) + " " +
                       str(itemInUsers['password']))

# rendezve a nevek kiírása
outputArray = sorted(outputArray)
# print(outputArray)
with open('nevek.txt', 'w') as f:
    for arrayItem in outputArray:
        f.write(arrayItem)
        f.write("\n")

#--------------------------------------------
# Class tutorial: https://www.tutorialsteacher.com/python/python-class
# Property decorator tutorial: https://www.tutorialsteacher.com/python/property-decorator
print("------------------")
print("---2. Feladat ----")


class Counter():
    def __init__(self, value):
        self.__value = value
        self.__step = 1

    @property
    def value(self):
        return self.__value

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, step):
        self.__step = step

    def increment(self):
        self.__value += self.__step

    def decrement(self):
        self.__value -= self.__step

    def set_value(self, value):
        self.__value = value

    def set_step(self, step):
        self.__step = step

    def get_value(self):
        print(self.__value)
        return self.__value


print("---2.1 Feladat ---")
myCounter = Counter(10)
myCounter.increment()
myCounter.increment()
myCounter.get_value()
myCounter.set_step(5)
myCounter.decrement()
myCounter.get_value()
myCounter.set_value(100)
myCounter.increment()
myCounter.get_value()

print("---2.2 Feladat ---")
# inheritance: https://www.geeksforgeeks.org/inheritance-in-python/


class ScoreCounter(Counter):
    def __init__(self, value, playerName, playerAge):
        self.__playerName = playerName
        self.__playerAge = playerAge
        self.__winner = False
        Counter.__init__(self, value)

    @property
    def playerName(self):
        return self.__playerName

    @property
    def playerAge(self):
        return self.__playerAge

    @property
    def winner(self):
        if (self.value >= 12):
            self.__winner = True
        else:
            self.__winner = False
        return self.__winner


myScoreCounter = ScoreCounter(10, 'Zsolt', 34)
myScoreCounter.increment()
myScoreCounter.get_value()
myScoreCounter.increment()
myScoreCounter.get_value()
print(myScoreCounter.winner)
