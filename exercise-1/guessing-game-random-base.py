import random


def guessing_game():
    """
    Generate a random number between 0 and 100.
    Generate a random base between 2 and 16.
    Ask the user to guess the number using the generated base.
    Prompt the user to guess again if the guess is too low or too high.
    Exit if the user guesses correctly.
    """
    num = random.randint(0, 100)
    base = random.randint(2, 16)

    while True:
        try:
            guess = input(f"Guess the number between 0 and 100 in base {base}: ")
        except ValueError:
            print("Please enter a valid number")
            continue
        except EOFError:
            print("Exiting...")
            break

        guess_in_base = int(guess, base)

        if guess_in_base == num:
            print(f"You guessed it! The answer was {num}")
            break

        if guess_in_base < num:
            print(
                f"Your guess in base {base} is {guess_in_base} and is too low, guess again"
            )
            continue
        else:
            print(
                f"Your guess in base {base} is {guess_in_base} and is too high, guess again"
            )
            continue


guessing_game()
