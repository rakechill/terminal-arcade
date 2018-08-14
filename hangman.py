# clear the logic up, put some into separate functions
# give the option to use a random word or to choose a word

def get_guess():
    word = input("Word to be guessed: ")
    dashes = "-" * len(word)
    guesses_left = 10

    while guesses_left > 0 and dashes != word:
        print(dashes)
        print (guesses_left)

        guess = input("Guess a letter: ")
    
        if len(guess) != 1:
            print ("Your guess must have exactly one character!")

        elif guess in word:
            print ("That letter is in the secret word!")
            dashes = update_dashes(word, dashes, guess)

        else:
            print ("That letter is not in the secret word!")
            guesses_left -= 1

    if guesses_left == 0:
        print ("You lose. The word was: " + str(word))

    else:
        print ("Congrats! You win. The word was: " + str(word))
    

def update_dashes(word, dashes, letter):
    result = ""

    for i in range(len(word)):
        if word[i] == letter:
            result = result + letter    

        else:
            result = result + dashes[i]
    
    return result
    