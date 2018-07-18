Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    intentos = 8
    wordguessed = False
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')
    while intentos > 0 and intentos<= 8 and wordguessed is False:
        if secretWord == getGuessedWord(secretWord,lettersGuessed):
            wordguessed = True
            break
        print ('You have ' + str(intentos) + ' guesses left.')
        print ('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                intentos -= 1
                print ('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
    if wordguessed == True:
        return 'Congratulations, you won!'
    elif intentos == 0:
        print ('Sorry, you ran out of guesses. The word was ' + secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

