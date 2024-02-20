import random

words = """ apple banana cherry grape mango
          strawberry pear lemon coconut """

some_words = words.split()
word = random.choice(some_words)

print(f"{"-"*10}Word Guessing game{"-"*10}")
print()


if __name__ == "__main__":
    print("Guess the word!(Hint: Word is a name of fruit)\n>> ")

    for char in word:
        print("_", end=" ")
    print()

    chances = len(word) + 2
    correct = 0
    letter_guessed = ""

    try:
        while chances != 0:
            print()
            chances -= 1

            guess = str(input("Enter letter to guess: ")).lower()

            if len(guess) != 1:
                print("Enter only SINGLE letter!")
                continue
            if guess in letter_guessed:
                print(f"You have already guessed {guess}")

            letter_guessed += guess

            if guess in word:
                k = sum(1 for char in word if char == guess)
                correct += k

            if correct == len(word):
                print(word)
                print()
                print("Congrats, You won!")
                break

            for char in word:
                if char in letter_guessed:
                    print(char, end=" ")
                else:
                    print("_", end=" ")

        if chances <= 0 and correct != len(word):
            print()
            print(f"You lost! The word was {word}")

    except KeyboardInterrupt:
        print()
        print("Bye! Try again")

    
            