import os  # we use os to check the file existence

# Function to validate email/username
def validate_email(username):
    # Validation logic for email/username
    if "@" in username and "." in username:
        at_index = username.index("@")
        dot_index = username.rindex(".")
        
        if (
            at_index > 0 and                    #checking not to start this with @
            dot_index > at_index + 1 and            #and it check char b/w @ and .
            username[at_index + 1] != "." and        #checking for immediate char is @ is not dot
            username[0].isalnum()                       #ensure the chart is alphanumeric 
        ):
            return True
    return False

# Function to validate password
def validate_password(password):
    # Validation logic for password
    if 5 < len(password) < 16:
        has_digit = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_special = any(not char.isalnum() for char in password)
        
        if has_digit and has_upper and has_lower and has_special:
            return True
    return False

# Function to register a new user
def register():
    print("---- Registration ----")
    username = input("Enter email/username: ")
    
    while not validate_email(username):
        print("Invalid email/username. Please try again.")
        username = input("Enter email/username: ")
    
    password = input("Enter password: ")
    
    while not validate_password(password):
        print("Invalid password. Please try again.")
        password = input("Enter password: ")
    
    # File Handling: Append the new user credentials to 'users.txt'
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    
    print("Registration successful!")

# Function to login a user
def login():
    print("---- Login ----")
    
    # Prompt for the email and validate it
    username = input("Enter email/username: ")
    
    while not validate_email(username):
        print("Invalid email/username. Please try again.")
        username = input("Enter email/username: ")

    password = input("Enter password: ")
    
    # File Handling: Check if the 'users.txt' file exists
    if os.path.exists("users.txt"):
        # File Handling: Read the file and check credentials
        with open("users.txt", "r") as file:
            users = file.readlines()
        
        for user in users:
            saved_username, saved_password = user.strip().split(",")
            
            if username == saved_username and password == saved_password:
                print("Login successful!")
                return
            
        print("Invalid credentials. Do you want to register or retrieve your password?")
        choice = input("Enter 1 for registration or 2 to retrieve your password: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            retrieve_password(username)
        else:
            print("Invalid choice.")
    else:
        print("No users found. Please register first.")
        register()

# Function to retrieve a password
def retrieve_password(username):
    # File Handling: Check if the 'users.txt' file exists
    if os.path.exists("users.txt"):
        # File Handling: Read the file and search for the username
        with open("users.txt", "r") as file:
            users = file.readlines()
        
        for user in users:
            saved_username, saved_password = user.strip().split(",")
            
            if username == saved_username:
                print(f"Your password is: {saved_password}")
                return
            
        print("Username not found. Do you want to register?")
        choice = input("Enter 1 for registration: ")
        
        if choice == "1":
            register()
        else:
            print("Invalid choice.")
    else:
        print("No users found. Please register first.")
        register()

def main():
    while True:
        print("\n---- Welcome ----")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
