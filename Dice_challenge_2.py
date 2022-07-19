'''Instructions

The Swinburne Caves & Lizards Club wishes to expand the functionality of the application requested previously.  They now wish the application to also:

    Store the dice rolls
    From the stored rolls, calculate
        Average
        Total
        List what the rolls were

The below are optional

    Write the rolls to text file, it should append the new rolls to whatever is already in the file.
    Read the rolls from a text file and display the amount of rolls, total and average.

As further requirements for each:

    Store the dice rolls - must use a list or array
    From the stored rolls, calculate - each of the below must be written within a function/method with appropriate return types and parameters.  Comment these functions explaining, outlining their purpose
        Average
        Total
        List what the rolls were

Optional

    Write the rolls to text file, it should append the new rolls to whatever is already in the file.
    Read the rolls from a text file and display the amount of rolls, total and average - must use functions created from requirement 2 above

'''

import random

def main():
    global num_times
    num_times = int(input("How many times do you want to roll the dice? "))
    print(f"Rolling the dice {num_times} times...the values are:")
    roll_dice(num_times)    # Call the roll_dice function using the num_times as a 
    roll_again = input("Do you want to roll the dice again? (y/n) ")
    if roll_again != 'y':    # Exit function (stop everything) if answer is not "y"
        exit
    else:                    # If answer is "y", invoke the main function to roll the dice again.
        main()


def calc_average(roll_list):
    average = round(sum(roll_list) / len(roll_list), 2)
    return average
    
def list_sum(roll_list):
    total = sum(roll_list)
    return total

def roll_dice(num_times):
    global roll_list
    roll_list = [random.randint(1,6) for i in range(num_times)]
    print(roll_list)
    rolls = 0
    for n in roll_list:      
        rolls += 1 
        print(f'Roll #{rolls}: {n}')
    print("Average of the list =", calc_average(roll_list))
    print("Sum of all elements in given list: ", list_sum(roll_list))
    list_sum(roll_list)


main()        # Call the main function


