import subprocess

# Initialize the user_data dictionary
user_data = {
    "mihir.suhanda01@sarasai.org": {"password": "MIHI123", "first_name": "Mihir", "last_name": "Suhanda", "age": 23},
    "umar.farooq01@sarasai.org": {"password": "UMAR123", "first_name": "Umar", "last_name": "Farooq", "age": 18},
    "shri.harshan01@sarasai.org": {"password": "SHRI123", "first_name": "Shri", "last_name": "Harshan", "age": 20},
    "ujjwal.kalra01@sarasai.org": {"password": "UJJW123", "first_name": "Ujjwal", "last_name": "Kalra", "age": 22},
    "khushi.g@sarasai.org": {"password": "Khushi123", "first_name": "Khushi", "last_name": "Gupta", "age": 23},
    "gaurav.singh@sarasai.org": {"password": "Gaurav123", "first_name": "Gaurav", "last_name": "Singh", "age": 42},
    "anshuman@sarasai.org": {"password": "Anshuman123", "first_name": "Anshuman", "last_name": "Singh", "age": 38},
    "vishnu@sarasai.org": {"password": "Vishnu123", "first_name": "Vishnu", "last_name": "Tiwari", "age": 28},
    "shailesh@sarasai.org": {"password": "Shailesh123", "first_name": "Shailesh", "last_name": "Kumar", "age": 40},
    "sakshi.g@sarasai.org": {"password": "Sakshi123", "first_name": "Sakshi", "last_name": "Garg", "age": 28},
}

# Start menu options
def start_menu():
    print("\n--- Music Application ---")
    print("1. Signup")
    print("2. Sign-in")
    print("3. Exit")

# Signup functionality
def signup(user_data):
    email = input("Enter Email ID: ")
    if email in user_data:
        print("Email ID already exists. Please try with a different email.")
        return

    password = input("Enter Password: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    age = int(input("Enter Age: "))

    user_data[email] = {
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }
    print(f"User {first_name} registered successfully!")
    
    # After successful signup, call the song management system
    print(f"Welcome, {first_name}!")
    # run_Developer_Settings()

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
