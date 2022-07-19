# Write a program that simulates rolling dice.

# When the program runs, it will:

# 1. Ask the user how many times they would like to roll the dice

# 2. Randomly choose a number between 1 and 6, for the number of dice that the user has indicated.  
# The number rolled will be printed.

# 3. Ask the user if they’d like to roll again.  If yes, go to step one.  Otherwise, exit.

import random

def main():
    num_times = int(input("How many times do you want to roll the dice? "))
    print(f"Rolling the dice {num_times} times...the values are:")
    roll_dice(num_times)    # Call the roll_dice function using the num_times as a 
    roll_again = input("Do you want to roll the dice again? (y/n) ")
    if roll_again != 'y':    # Exit function (stop everything) if answer is not "y"
        print("Thank you for playing!")
        exit
    else:                    # If answer is "y", invoke the main function to roll the dice again.
        main()
            
def roll_dice(num_times):
    rolls = 0     # Start the counter
    for i in range(num_times):     # Loop through how many times the user wants you to roll the dice
        rolls += 1       # Increase the number by 1 with every loop
        random_number = random.randint(1, 6)    # Create a variable to store a random number for each loop
        print(f'Roll #{rolls}: {random_number}')
    
main()        # Call the main function again