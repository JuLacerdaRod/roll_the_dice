# Exercise 1

# Create flowcharts, pseudocode and/or code for the following:

# A program receives a person's age as input from the user. 
# If the input is greater than 17, output "Legally adult age", otherwise output "Legally not adult age".

age = int(input("Enter your age: "))
if age > 17:
    print("Legally adult age")
else:
    print("Legally not adult age")

# A program receives the gender of a person (male or female) and also their age. 
# The program should output accordingly, "M/F is an adult/not an adult"

gender = input("Type your gender: ")
age = int(input("Enter your age: "))

if age > 17:
    print(f"{gender} is an adult")
else:
    print(f"{gender} is not an adult")

# A program receives two numbers. 
# If the numbers add up to greater than 10, output "Sum of numbers is greater than 10". 
# If the numbers add up to less than 10, output "Sum of numbers is less than 10". 
# What happens if the numbers add up to 10?

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))
sum = number1 + number2

if sum > 10:
    print ("Sum of numbers is greater than 10")
elif sum < 10:
    print ("Sum of numbers is less than 10")
else:
    print("Sum of numbers is 10")
