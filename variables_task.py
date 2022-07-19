name = input("What is your first name?") # Store input inside a variable
print(name)

surname = input("Enter your last name:")
print(surname)

studentID = input("Enter your Student ID:")
print(studentID)

birth_year = int(input("Enter your year of birth:"))
print(birth_year)

current_year = int(input("Enter the current year:"))
print(current_year)


fullname = name + " " + surname
age = current_year - birth_year

print(fullname)
print(age)