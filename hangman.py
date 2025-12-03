import random

def hangman():
    words = ["python", "computer", "random", "developer", "hangman", "programming"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    used = []

    print("\n--- Hangman Game ---")

    while attempts > 0:
        print("\nWord:", " ".join(guessed))
        print("Attempts left:", attempts)
        print("Used letters:", used)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input.")
            continue

        if guess in used:
            print("Already guessed.")
            continue

        used.append(guess)

        if guess in word:
            print("✔ Good guess!")
            for i, ch in enumerate(word):
                if ch == guess:
                    guessed[i] = guess
        else:
            print("❌ Wrong letter!")
            attempts -= 1

        if "_" not in guessed:
            print("\n🎉 You WON! The word was:", word)
            return

    print("\n💀 You LOST! The word was:", word)
