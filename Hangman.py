#Jacob Hall
#February 3rd, 2016
#Hangman v1.2
#GNU General Public License v3.0

from random import randint

words = ["survivalism", "vegetables", "television", "bookworm", "jawbreaker", "whomever", "zombies", "walkway", "vortex", "wizard", "bowling", "flashlight", "dragon", "bagpipes", "banjo", "buffalo", "racecar", "ivy", "catwalk", "icebox"]
hangmanWord = words[randint(0,19)]
wordWithBlanks = []
for x in hangmanWord:
    wordWithBlanks.append("_")

art = ["  ————\n     |\n     |\n     |\n——————","  ————\n  O  |\n     |\n     |\n——————","  ————\n  O  |\n /   |\n     |\n——————","  ————\n  O  |\n / \ |\n     |\n——————","  ————\n  O  |\n /|\ |\n     |\n——————","  ————\n  O  |\n /|\ |\n /   |\n——————","  ————\n  0  |\n /|\ |\n / \ |\n——————"]
currentArt = 0

correctLetters = 0

def guess(letter):
    letter = letter.lower()
    letterOccurrences = hangmanWord.count(letter)
    global currentArt
    if letterOccurrences > 0:
        previousOccurrence = 0
        for occurrence in range(0, letterOccurrences):
            letterLocation = hangmanWord.find(letter, previousOccurrence)
            wordWithBlanks[letterLocation] = letter
            previousOccurrence = letterLocation + 1
        print(art[currentArt])
        print(''.join(wordWithBlanks))
        global correctLetters
        correctLetters += letterOccurrences
        if correctLetters == len(hangmanWord):
            print("Congradulations, You Win!\nRestart Program To Play Again.")
        else:
            getInput()
    else:
        currentArt += 1
        if currentArt < 7:
            print(art[currentArt])
            if currentArt == 6:
                print("Sorry, You Lost.\nThe correct word was '" + hangmanWord + "'\nRestart Program To Play Again.")
            else:
                print(''.join(wordWithBlanks))
                getInput()
            
def getInput():
    userInput = input("Please guess a letter.\n")
    chrValue = ord(userInput)
    while not (len(userInput) == 1) or not ((chrValue >= 65 and chrValue <= 90) or (chrValue >= 97 and chrValue <= 122)):
        userInput = input("Please guess a valid letter.\n")
        chrValue = ord(userInput)
    guess(userInput)

print(art[currentArt])
print(''.join(wordWithBlanks))
getInput()
