import string
import keyboard
import os
import json
from random import randint


alphabet = list(string.ascii_lowercase)
saved = []
col = 0
row = 0
words = json.load(open('words.json'))
correctWord = words[randint(0, len(words)-1)]
gameStatus = True


def printBanner():
    os.system('cls||clear')
    print("---------------------")
    for colI in range(5):
        print("|", end=" ")
        for rowI in range(5):
            try:
                if saved[colI][rowI] == correctWord[rowI] and len(saved[colI]) == 5:
                    print("\x1b[6;30;42m" + saved[colI][rowI] + "\x1b[0m", end= " | ")
                elif saved[colI][rowI] != correctWord[rowI] and saved[colI][rowI] in correctWord and len(saved[colI]) == 5:
                    print("\33[43m" + saved[colI][rowI] + "\x1b[0m", end= " | ")
                else:
                    print(saved[colI][rowI], end= " | ")
            except:
                print("-", end= " | ")
        print()
    print("---------------------")

def removeLastWord():
    global row
    global col
    del saved[col:]
    row = -1
    col = col - 1

printBanner()
while gameStatus:
    try: 
        if keyboard.read_key().lower() in alphabet: 
            if len(saved) == col + 1:
                saved[col].append(keyboard.read_key().upper())
            else: 
                saved.append([keyboard.read_key().upper()])
            if row == 4:
                word = saved[col][0]+saved[col][1]+saved[col][2]+saved[col][3]+saved[col][4]
                if word not in words:
                    removeLastWord()
                elif word == correctWord:
                    gameStatus = False
                col += 1
                row = -1
            row += 1
            printBanner()
            if not gameStatus:
                print("nice work u win")
            elif col == 5:
                print("nice try, good luck next time")
    except:
        break
