import random

number = random.randint(1, 100)
guess = None
attempts = 0

print("Welcome to the Guessing Game!")

while guess != number:
    guess = int(input("Enter your guess (between 1 and 100): "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right in", attempts, "attempts!")
