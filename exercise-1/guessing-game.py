import random


def guessing_game():
    """
    Generate a random number between 0 and 100.  Ask the user to guess the number.
    Prompt the user to guess again if the guess is too low or too high.
    Exit if the user guesses correctly.
    """
    num = random.randint(0, 100)

    while True:
        try:
            guess = int(input("Guess the number between 0 and 100: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        except EOFError:
            print("Exiting...")
            break

        if guess == num:
            print(f"You guessed it! The answer was {num}")
            break

        if guess < num:
            print(f"Your guess of {guess} is too low, guess again")
            continue
        else:
            print(f"Your guess of {guess} is too high, guess again")
            continue


guessing_game()
