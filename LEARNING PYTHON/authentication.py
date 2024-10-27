#Login confirmation
# Write a Python program that prompts the user to enter a password. The program should compare the entered password with a predefined password stored in the system. If the passwords match, the program should display "Access Granted." If they don't match, it should display "Access Denied."
# Requirements:
# Predefine a password within the code (e.g., "securePassword123").
# Use an if statement to check if the user's input matches the predefined password.
# Display the appropriate message based on whether the passwords match.
password = "Limo123"

password_input = input('Enter password: ')

if password_input !=password:
    print("Access denied")
else:
    print("Access granted!")