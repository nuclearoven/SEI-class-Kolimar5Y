import random
import string
import datetime
import os
from os import path
from datetime import date
#Strings - random letters____________________________________________________

#1-1
def RandomString(length1):
    """this function creates a new string with the length: length1 which is set in the second function
    it then generates random letters and joins them into the string"""
    str = ''.join(random.choices(string.ascii_letters, k=length1))
    return str
#1-2
def RandomList(length2):
    """this function generates a list lst with the length: length2
    It assigns random words to it with a specified length."""
    lst = []
    for i in range(length2):
        lst.append(RandomString(5))
    return lst
print(RandomList(10))

#2 i dont understand the assignment

#3 this code prints how many letters does each of the strings in the list have
for i in RandomList(10):
    print(len(i))


#Strings - random words____________________________________________________

#1-1
def RandomWord(length1):
    """this function generates a random string of the length: length1
    it returns the string str"""
    str = ''.join(random.choices(string.ascii_letters, k=length1))
    return str
def WordList():
    """this function generates a random list consisting of strings from the first function with the length: length
    it returns the list lst"""
    lst = []
    for i in range(30):
        lst.append(RandomWord(random.randint(3, 7)))
    return lst
#1-2 loops through the wordlist and if a word has the specified amount of letters it adds one to its respective int
wordlist = WordList()
threeLetter = 0
fourLetter = 0
fiveLetter = 0
sixLetter = 0
sevenLetter = 0

for i in range(30):
    if len(wordlist[i]) == 3:
        threeLetter += 1
    if len(wordlist[i]) == 4:
        fourLetter += 1
    if len(wordlist[i]) == 5:
        fiveLetter += 1
    if len(wordlist[i]) == 6:
        sixLetter += 1
    if len(wordlist[i]) == 7:
        sevenLetter += 1
print("3 letters:" + str(threeLetter))
print("4 letters:" + str(fourLetter))
print("5 letters:" + str(fiveLetter))
print("6 letters:" + str(sixLetter))
print("7 letters:" + str(sevenLetter))
#2
def sortAlphabetically(lst):
    """this function sorts the list lst alphabetically"""
    lst.sort()
    return lst
print("sorted alphabetically: " + str(sortAlphabetically(wordlist)))
#3
def sortLength(lst):
    """this function sorts the list lst by word length in ascending order"""
    lst.sort(key=len)
    return lst
print("sorted by length: " + str(sortLength(wordlist)))

#________________________________________________________________________________________________________
#paths
#________________________________________________________________________________________________________

import os
from datetime import datetime, timedelta
import random

#1 checks if the data and dates folders exist, if not it creates them
data_folder = "data"
dates_folder = os.path.join(data_folder, "dates")

if os.path.exists(data_folder):
    print("data folder exists:")
else:
    os.makedirs(data_folder)
if os.path.exists(dates_folder):
    print("dates folder exists:")
else:
    os.makedirs(dates_folder)

#2 dice roll
def rollDice():
    """this function picks a random number between 1 and 6"""
    return random.randint(1, 6)

#3 Create 10 files starting from today's date
today = datetime.now()
def fileCreate(extraDay):
    """this function creates a new file in the dates folder with its name corresponding to a date some time from today
    parameters:
    -extraDay: the amount of days from today
    -day: today’s date with the added extra days
    -filename: the day parameter as a string
    -filepath: the path to the dates folder
    -file: the new file
    -rolls: list of ten dice rolls from the previous function
    The function writes the result of a dice-roll into each file
    returns nothing"""
    day = today + timedelta(days=extraDay)
    filename_date = day.strftime("%Y-%m-%d")
    filename = f"{filename_date}.txt"
    filepath = os.path.join(dates_folder, filename)
    rolls = [str(rollDice()) for _ in range(10)]
    file = open(filepath, "w")
    file.write("\n".join(rolls))
    return

#repeats the fileCreate function the specified amount of times
for i in range(10):
    fileCreate(i)

#4 Creates a file with the current time and saves it in the dates folder
timePath = os.path.join(data_folder, "time.txt")

with open(timePath, "w") as f:
    time = datetime.now().strftime("%H:%M:%S")
    f.write(time)
