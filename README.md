# Registration and Login System using Python and File Handling

This is a simple registration and login system implemented in Python, which uses file handling to store user data securely. It allows users to register, login, and retrieve forgotten passwords.

## Features

1. **Registration**:
    - The user can register with an email/username and password.
    - Email/username should contain an "@" and must be followed by a "." (e.g., `sherlock@gmail.com` or `nothing@yahoo.in`).
    - Invalid email/username formats will be rejected, such as:
        - Starting with "@" (e.g., `@gmail.com`).
        - Containing "." immediately after "@" (e.g., `my@.com`).
        - Starting with numbers or special characters (e.g., `123#@gmail.com`).
    - Password must meet the following conditions:
        - Be between 6 to 15 characters long.
        - Contain at least one special character, one digit, one uppercase letter, and one lowercase letter.
    - Upon successful validation, the email/username and password are stored in the `users.txt` file.

2. **Login**:
    - The user can log in by providing their email/username and password.
    - The system checks if the credentials match the ones stored in `users.txt`.
    - If the login is unsuccessful, the user is prompted to either register or retrieve their forgotten password.

3. **Forgot Password**:
    - If a user forgets their password, they can retrieve it by providing their username.
    - The system will fetch the password from the `users.txt` file if the username exists.

## How It Works

### Registration
1. The user is prompted to enter their email/username and password.
2. The system validates the email/username and password according to the rules mentioned above.
3. If validation is successful, the credentials are saved in the `users.txt` file in the format:


### Login
1. The user is prompted to enter their email/username and password.
2. The system checks if the credentials exist in the `users.txt` file.
3. If the credentials are correct, the user is logged in successfully. Otherwise, the user is prompted to either register or retrieve their password.

### Password Retrieval
1. If a user forgets their password, they can retrieve it by providing their username.
2. The system searches for the username in the `users.txt` file and displays the associated password if found.

## How to Run the System

1. Clone this repository to your local machine.
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
|-- registration_login_system.py   # Main Python script
|-- users.txt                      # File where user credentials are stored
