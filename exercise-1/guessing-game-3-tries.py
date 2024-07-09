import random


def guessing_game():
    """
    Generate a random number between 0 and 100.  Ask the user to guess the number.
    Restrict the number of guesses to 3.
    Prompt the user to guess again if the guess is too low or too high.
    Exit if the user guesses correctly.
    """
    num = random.randint(0, 100)
    guesses_remaining = 3

    while True:
        if not guesses_remaining:
            print("You have run out of guesses, game over.")
            break

        try:
            guess = int(
                input(
                    f"Guess the number between 0 and 100 ({guesses_remaining} guesses remaining): "
                )
            )
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
            print(f"Your guess of {guess} is too low")
            guesses_remaining -= 1
            continue
        else:
            print(f"Your guess of {guess} is too high")
            guesses_remaining -= 1
            continue


guessing_game()
