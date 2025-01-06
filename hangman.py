import random

def hangman():
    # List of words to choose from
    word_list = ['python', 'hangman', 'programming', 'development', 'computer']
    word = random.choice(word_list).lower()
    guessed_word = ['_'] * len(word)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!\n")

    while attempts > 0 and '_' in guessed_word:
        print("\nWord to guess: ", ' '.join(guessed_word))
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

    if '_' not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()