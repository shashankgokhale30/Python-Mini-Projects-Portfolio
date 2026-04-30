# guess the number game

import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Correct! You guessed it in", attempts, "attempts.")
            break


def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ")

        if again.lower() != "yes":
            print("Thanks for playing!")
            break


main()
