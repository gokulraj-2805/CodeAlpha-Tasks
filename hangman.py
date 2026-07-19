import random
def hangman():
    words = ["python","coding","laptop","bridge","planet"]
    word  = random.choice(words)
    guesssed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        display_word = "" 
        for letter in word:
            if letter in guesssed_letters:
                    display_word +=letter + " "
            else:        
                display_word +="_"
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")

        if "_" not in display_word:
           print("Congratulations! You Won!")
           break
        guess = input("Guess a letter: ").lower()

        if guess in guesssed_letters:
           print("You already guessed that.")
        elif guess in word:
           print("Good Job!")
           guesssed_letters.append(guess)
        else:
           print("Wrong guess.")
           guesssed_letters.append(guess)
           attempts -= 1

    if attempts == 0:
       print(f"\nGame Over! The word was: {word}")
hangman()


           
