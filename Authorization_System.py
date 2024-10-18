import subprocess

# File path to store user data
user_data_file = "user_data.txt"

# Load user data from a text file
def load_user_data():
    user_data = {}
    try:
        with open(user_data_file, "r") as file:
            for line in file:
                email, password, first_name, last_name, age = line.strip().split(",")
                user_data[email] = {
                    "password": password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "age": int(age)
                }
    except FileNotFoundError:
        print("User data file not found.")
    return user_data

# Save user data to a text file
def save_user_data(user_data):
    with open(user_data_file, "w") as file:
        for email, info in user_data.items():
            file.write(f"{email},{info['password']},{info['first_name']},{info['last_name']},{info['age']}\n")

# Start menu options
def start_menu():
    print("\n--- Music Application ---")
    print("1. Signup")
    print("2. Sign-in")
    print("3. Exit")

# Signup functionality
def load_user_data():
    user_data = {}
    with open('user_data.txt', 'r') as file:
        for line in file:
            email, password, first_name, last_name, age = line.strip().split(',')
            if age.isdigit():
                user_data[email] = {
                    "password": password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "age": int(age)
                }
            else:
                print(f"Invalid age for user {email}. Skipping entry.")
    return user_data

# Sign-in functionality
def signin(user_data):
    email = input("Enter Email ID: ")
    password = input("Enter Password: ")

    if email in user_data and user_data[email]["password"] == password:
        print(f"Welcome, {user_data[email]['first_name']}!")
        # After successful login, call the Developer_Settings system
        # run_Developer_Settings()
    else:
        print("Invalid email or password. Please try again.")

# Exit functionality
def exit_program():
    print("Exiting the application. Please come again!")
    exit()  # Exit the program

# Main program loop
def main():
    # Load user data from the file at the start
    user_data = load_user_data()

    while True:
        start_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            signup(user_data)
        elif choice == "2":
            signin(user_data)
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
