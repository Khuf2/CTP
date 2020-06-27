# Theo Novak - 6/24/2020
# CTP Function to calculate "irresistability score", or chill-to-pull ratio

# automatic save callback from menu()?
# boolean in an options file that can remember the user

from Entry import *
from User import *
import json

def readPrep(data):
    entryData = []
    for x in data:
        entryData.append(Entry(x["Name"], x["Gender"], x["Age"], x["Scores"], x["Author"]))
    return entryData

def writePrep(data):
    dictData = []
    for x in data:
        dictData.append({
            "Name": x.getName(),
            "Gender": x.getGender(),
            "Age": x.getAge(),
            "Scores": x.getAllScores(),
            "Author": x.getAuthor()
        })
    return dictData

def main():

    name = ""
    while(len(name) is 0):
        name = input("What's your name: ") 
    # check for length
    
    
    # open file for reading, load it to the data var
    with open('data.json', 'r') as f:
        data = readPrep(json.load(f))

    # ignore the pylint hate
    user = User(name, data)

    user.menu()

    # save file after any edits made
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(writePrep(data), f, ensure_ascii=False, indent=4)


main()

