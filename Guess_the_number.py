import random

def guess(x):
    random_variable = random.randint(1,x)
    guess = 0
    while guess != random_variable:
        guess = int(input(f"Guess the number 1 to {x}: "))
        if guess > random_variable:
            print("Sorry, you guess too high")

        elif guess < random_variable:
            print("Sorry, you guess too low")

    print("Hurray you guess right")

guess(100)