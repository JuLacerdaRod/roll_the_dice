import random

def main():
    times = int(input("How many times do you want to roll the dice ? "))
    print("You have rolled the dice", times, "times")
    roll(times)
    roll_again= "y"
    roll_again = input("Would you like to roll it again ? y/n ").lower()
    if roll_again != "y":
        exit
    else:
        main()

def roll(times):
    while times != 0:
        times -= 1
        dice_value = random.randint(1, 6)
        print(dice_value)


main()