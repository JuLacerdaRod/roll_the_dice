
    # Receive input from user
    # Check the input
    #     If input is 'A'
    #         output "You have selected A"
    #     If input is not 'A'
    #         If input is 'B'
    #             output "You have selected B"
    #         If input is not 'B'
    #             If input is 'C'
    #                 output "You have selected C"
    #             If input is not 'C'
    #                 output "Invalid option"

answer = input("Please enter A, B or C: ")

if answer == "A":
    print("You have selected A")
elif answer == "B":
        print("You have selected B")
elif answer == "C":
        print("You have selected C")
else:
    print("Invalid option")