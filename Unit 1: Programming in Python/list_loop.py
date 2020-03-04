import matplotlib.pyplot as plt
import random

plt.ion()


# -----------------------------------------------------------------------------------------------------------------------------


def roll_dice():
    dice = [1, 2, 3, 4, 5, 6]
    roll1 = random.choice(dice)
    roll2 = random.choice(dice)

    return roll1 + roll2


a = []

for i in range(100):
    a += [roll_dice()]

plt.hist(a)
plt.show(a)


# -----------------------------------------------------------------------------------------------------------------------------

def check_character(character=''):
    wordList = ["dog", "cat", "hamster", "tree"]
    secretWord = random.choice(wordList)

    if character in secretWord:
        return True
    else:
        return False


# -----------------------------------------------------------------------------------------------------------------------------

def check_positives(sentence=""):
    positiveList = ["happy", "nice", "cool", "jolly", "seven", "cheerful", "delightful", "friendly", "delicious"]
    numberOfPositives = 0

    sentenceList = sentence.split(" ")

    for i in range(len(sentenceList)):
        if sentenceList[i] in positiveList:
            numberOfPositives += 1

    return numberOfPositives


print(check_positives("happy jolly mean nice cool eight seven cheerful ugly fatso delightful friendly heck delicious"))


# -----------------------------------------------------------------------------------------------------------------------------

def check_negatives(sentence=""):
    negativeList = ["sad", "mad", "angry", "disgusting", "ugly", "pie", "stupid", "stinky", "grotesque"]

    numberOfNegatives = 0

    sentenceList = sentence.split(" ")

    for i in range(len(sentenceList)):
        if sentenceList[i] in negativeList:
            numberOfNegatives += 1

    return numberOfNegatives
