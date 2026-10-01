import random

words = {
    "python": "A popular programming language",
    "computer": "An electronic machine used to process data",
    "elephant": "A large animal with a trunk",
    "rainbow": "You can see this after rain",
    "keyboard": "You use this to type on a computer"
}

word = random.choice(list(words.keys()))
hint = words[word]

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

hangman = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

print("===== HANGMAN GAME =====")
print("Hint:", hint)

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print()
    print(hangman[wrong_guesses])
    print("Word:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    if all(letter in guessed_letters for letter in word):
        print()
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(hangman[wrong_guesses])
    print("Game Over!")
    print("The word was:", word)
