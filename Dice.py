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
    roll_dice(num_times)
    roll_again = input("Do you want to roll the dice again? (y/n) ")
    if roll_again != 'y':
        exit
    else:
        main()
            
def roll_dice(num_times):
    rolls = 0
    for i in range(num_times):
        rolls += 1
        random_number = random.randint(1, 6)
        print(f'Roll #{rolls}: {random_number}')
    
main()