import random

def play_hangman():
    # Predefined word list
    words = ["python", "coding", "alpha", "github", "script"]
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("=== Welcome to Hangman Game ===")
    
    while incorrect_guesses < max_incorrect:
        # Display current status of word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word.strip()}")
        print(f"Attempts remaining: {max_incorrect - incorrect_guesses}")
        
        # Check if user won
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break

        guess = input("Guess a letter: ").lower().strip()

        # Input validations
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
        else:
            print(f"Good job! '{guess}' is in the word.")

    if incorrect_guesses == max_incorrect:
        print(f"\n❌ Game Over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()