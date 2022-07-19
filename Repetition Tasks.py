# 1. A program that counts from 1 to 10.

count = 1
while count <= 100:
    print(count)
    count += 1



# 2. A program that counts from 0 to 20, counting by two's.

count = 0
while count <= 20:
    print(count)
    count += 2



# 3. A program that asks the user to guess a number. The magic number is 5. 
# If they get it wrong, the program asks for the number again.

magic_number = "5"

number = input("Please enter a number: ")

while number != magic_number:
    number = input("Please enter a number: ")



# 4. A program that asks the user to enter a number. 
# The program then counts from 0 to that number.

number = int(input("Please enter a number: "))

count = 0
while count <= number:
    print(count)
    count += 1



# 5. A program that asks the user "What happens when you throw a yellow rock in the red sea?". 
# The user must guess the correct answer, "It gets wet". 
# If the correct answer isn't entered the program asks again.

answer = input("What happens when you throw a yellow rock in the red sea? ")

if answer != "It gets wet":
    answer = input("Try again. What happens when you throw a yellow rock in the red sea?")
else: 
    print("That's right. Congratulations!")


# Set a secret number to 653.  
# Then program will then loop, 
# where each loop will ask the user to enter what they think a secret integer is. 
# If they get it right, print "Correct", otherwise print "Wrong, counter value is ".  
# Give the user 10 chances to guess.   
# Hint: You will need an if statement inside the loop.  
# Bonus: Make the secret number randomly generate between 1 and 1000 
# each time the program is run.  

secret_number = 653

guess = input("Please guess the secret number: ")

if guess == secret_number:
    print("Correct!")
else: 
    print("Wrong, counter value is ")




