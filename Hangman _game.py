import random

words_with_hints = {
    'apple': 'A fruit that keeps the doctor away',
    'train': 'A mode of public transport on tracks',
    'house': 'A place where people live',
    'light': 'Opposite of dark',
    'plant': 'It grows in soil and needs sunlight'
}

def play_game():
    word, hint = random.choice(list(words_with_hints.items()))
    display = ['_'] * len(word)
    guessed_letters = []

    print("Choose difficulty:")
    print("1. Easy (8 attempts)")
    print("2. Medium (6 attempts)")
    print("3. Hard (4 attempts)")
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        attempts = 8
    elif choice == '2':
        attempts = 6
    else:
        attempts = 4

    print("\n=== HANGMAN ===")
    print(f"Hint: {hint}")
    print(f"You have {attempts} incorrect attempts.\n")

    while attempts > 0 and '_' in display:
        print("Word:", ' '.join(display))
        print("Guessed letters:", ', '.join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            print("Correct guess!\n")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}\n")

    if '_' not in display:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game Over! The word was:", word)

while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != 'yes':
        print("Thanks for playing Hangman! Goodbye!")
        break