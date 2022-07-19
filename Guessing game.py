
import random

n = random.randint(1, 10)
guess = int(input("Enter an integer from 1 to 10: "))

while n != "guess":
    print
    if guess < n:
        print("Guess is low, try again")
        guess = int(input("Enter an integer from 1 to 10: "))
    elif guess > n:
        print("Guess is high, try again.")
        guess = int(input("Enter an integer from 1 to 10: "))
    else:
        print("Congratulations! You guessed it!")
        break
