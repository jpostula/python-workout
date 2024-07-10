from pathlib import Path

import nltk
from nltk.corpus import words


def main():
    nltk.download("words")
    word_list = words.words()

    short_words = [word for word in word_list if len(word) <= 5]

    with open(Path("exercise-1") / "short_words.txt", "w") as file:
        for word in short_words:
            file.write(word + "\n")


if __name__ == "__main__":
    main()
