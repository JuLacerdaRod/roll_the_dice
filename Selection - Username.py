username = input("What is your username? ").upper()

if username == "JULIANA":
    print("User exists")
    password = input("What is your password? ")
    if password == "dog":
        print("Login successful")
    else:
        print("Incorrect password. Login unsuccessful")
else:
    print("User doesn't exist")

