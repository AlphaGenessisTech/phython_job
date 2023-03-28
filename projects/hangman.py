secret = "dino"
failureCount = 6
guessedLetters = ""

while failureCount > 0:
    guess = input  ("enter a letter: ")

    if guess in secret:
        print(f"correct! There is one or more '{guess}' letter  in th secret 🎉")
    else:
        failureCount -= 1
        print(f"Incorrect!  There's no '{guess}'in the secret" )

    guessedLetters += guess
    wrongLetterCount = 0

    for letter in secret:
        if letter in guessedLetters:
            print (f"{letter}",end=" ")
        else:
            print ("__ ", end=" ")
            wrongLetterCount += 1
    print("\n")

    if wrongLetterCount == 0:
        print ("Congratulations! you won the game ! ")
        break

else:   
    print("Sorry, you ran out of guesses ! But try again..")