# Hangman
A basic hangman game written from scratch in Python 3, with ASCII art.
Note: You must run this program using Python 3, for example in terminal type “python3.x Hangman.py” to run the program correctly (where x is the version of Python 3 you have installed).

Patch Notes:

v2.0

-The game will now ask the user if they would like to play again after the game is over.

-Clears screen after each letter guess and when a new game is started, on both Windows and Linux (Not supported in Python Shell)

-The program is now encapsulated in a class, to prevent globals.

-Removed some unnecessary steps when variables are first set-up.

-Fixed crash when user enters a string, before the chr was considered invalid.

v1.2

-More efficient when getting user input. (Less function calls)

-Changed ASCII Art

v1.1

-Fixed input sterilization bug caused by order of operations not short circuiting.

v1.0

-Original Program
