
from this import d
import time


lives = 10
stringword = "Apple"
word = list(stringword.lower())  # converts to a list of letters
winner = False
incorrectletters = []
guess = ["_"] * len(word)  

def printscore():
    print("\n\nLives: ", str(lives))
    print("Incorrect Letters: ", end="")
    for i in range(len(incorrectletters)):
        if i == len(incorrectletters) - 1:
            print(incorrectletters[i], end="")
        else:
            print(incorrectletters[i], end=",")
    print("")
    print("Guess: ", end="")
    for i in range(len(guess)):
       print(guess[i], end="")
    print("")

def askforletter():
    letter = input("Please guess a letter: ").lower()
    correct = False
    for i in range(len(word)):
        if letter == word[i]:
            guess[i] = letter
            correct = True
    if correct:
        print("You got one!")
    else:
        print("Sorry there is no '"+letter+"'.")
        incorrectletters.append(letter)
        global lives 
        lives -= 1
    time.sleep(1)
    
def checkwinner():
    if "_" not in guess:
        global winner
        winner = True

while lives > 0 and not winner:
    printscore()
    askforletter()
    checkwinner()




if lives <= 0:
    print("You lost. The word was "+ stringword +".")
else:
    print("Congrats! The word is '"+stringword+"'. You won with " + str(lives) + " lives left!" )

