#Jacob Hall
#Created: February 3rd, 2016
#Hangman v2.0
#https://github.com/jakeehall/Hangman
#GNU General Public License v3.0

import os
from random import randint

class Hangman():
    def setup(self):
        _=os.system('cls')
        _=os.system('clear')
        self.hangmanWord = self.words[randint(0,19)]
        self.wordWithBlanks = []
        for x in self.hangmanWord:
            self.wordWithBlanks.append("_")
        self.currentArt = 0
        self.correctLetters = 0
        print(self.art[0])
        print(''.join(self.wordWithBlanks))
        self.getLetterInput()

    def guess(self, letter):
        _=os.system('cls')
        _=os.system('clear')
        letterOccurrences = self.hangmanWord.count(letter)
        if letterOccurrences > 0:
            previousOccurrence = 0
            for occurrence in range(0, letterOccurrences):
                letterLocation = self.hangmanWord.find(letter, previousOccurrence)
                self.wordWithBlanks[letterLocation] = letter
                previousOccurrence = letterLocation + 1
            print(self.art[self.currentArt])
            print(''.join(self.wordWithBlanks))
            self.correctLetters += letterOccurrences
            if self.correctLetters == len(self.hangmanWord):
                print("\nCongradulations, You Win!")
                self.getReplayInput()
            else:
                self.getLetterInput()
        else:
            self.currentArt += 1
            if self.currentArt < 7:
                print(self.art[self.currentArt])
                if self.currentArt == 6:
                    print("\nSorry, You Lost.\nThe correct word was '" + self.hangmanWord + "'")
                    self.getReplayInput()
                else:
                    print(''.join(self.wordWithBlanks))
                    self.getLetterInput()
                
    def getLetterInput(self):
        userInput = ""
        while (len(userInput) != 1) or not (ord(userInput) >= 97 and ord(userInput) <= 122):
            userInput = input("Please guess a letter.\n").lower()
        self.guess(userInput)

    def getReplayInput(self):
        userInput = ' '
        while not (userInput == '' or userInput == 'y' or userInput == 'n'):
            userInput = input("Would you like to play again? (Y/n)\n").lower()
        if userInput != 'n':
            self.setup()

    def __init__(self):
        self.words = ["survivalism", "vegetables", "television", "bookworm", "jawbreaker", "whomever", "zombies", "walkway", "vortex", "wizard", "bowling", "flashlight", "dragon", "bagpipes", "banjo", "buffalo", "racecar", "ivy", "catwalk", "icebox"]
        self.art = ["  ————\n     |\n     |\n     |\n——————","  ————\n  O  |\n     |\n     |\n——————","  ————\n  O  |\n /   |\n     |\n——————","  ————\n  O  |\n / \ |\n     |\n——————","  ————\n  O  |\n /|\ |\n     |\n——————","  ————\n  O  |\n /|\ |\n /   |\n——————","  ————\n  0  |\n /|\ |\n / \ |\n——————"]
        self.setup()

Hangman()
