import random
from pathlib import Path


def guessing_game():
    """
    Generate list of english words with 5 characters or less.
    Ask the user to guess the word.
    Prompt user if word is earlier or later alphabetically.
    """
    word_list = []
    with open(Path("exercise-1") / "short_words.txt", "r") as file:
        word_list = file.read().splitlines()

    word = random.choice(word_list).lower()

    while True:
        try:
            guess = input("Guess the word (5 characters or less): ")
        except ValueError:
            print("Please enter a valid word")
            continue
        except EOFError:
            print("Exiting...")
            break

        if guess == word:
            print(f"You guessed it! The answer was {word}")
            break

        if guess < word:
            print(f"Your guess of {guess} is earlier in the alphabet, guess again")
            continue
        else:
            print(f"Your guess of {guess} is later in the alphabet, guess again")
            continue


guessing_game()
