import subprocess

# Initialize the user_data dictionary
user_data = {
    "aditya.chaudhary01@sarasai.org": {"password": "ADI123", "first_name": "Aditya", "last_name": "Chaudhary", "age": 18},
    "abhishek.singh01@sarasai.org": {"password": "ABHI4533", "first_name": "Abhishek", "last_name": "Singh", "age": 20},
    "swapnil.baranwal01@sarasai.org": {"password": "Swapnil001", "first_name": "Swapnil", "last_name": "Baranwal", "age": 24},
    "anumolu.chidrup01@sarasai.org": {"password": "Chidrup109", "first_name": "Anumolu", "last_name": "Chidrup", "age": 22},
    "gaurav.singh@sarasai.org": {"password": "Gaurav1234", "first_name": "Gaurav", "last_name": "Singh", "age": 33},
    "anshuman@sarasai.org": {"password": "Anshuman0303", "first_name": "Anshuman", "last_name": "Singh", "age": 32},
    "vishnu@sarasai.org": {"password": "Vishnu0234", "first_name": "Vishnu", "last_name": "Tiwari", "age": 28},
    "shailesh@sarasai.org": {"password": "Shailesh0707", "first_name": "Shailesh", "last_name": "Kumar", "age": 34},
    "poonam.m@sarasai.org": {"password": "Madaan9870", "first_name": "Poonam", "last_name": "Madaan", "age": 32},
    "Khushi.g@sarasai.org": {"password": "Khushi7654", "first_name": "Khushi", "last_name": "Gupta", "age": 27}
}

# Display menu options
def display_menu():
    print("\n--- Music Management Application ---")
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
    # run_song_management()

# Sign-in functionality
def signin(user_data):
    email = input("Enter Email ID: ")
    password = input("Enter Password: ")

    if email in user_data and user_data[email]["password"] == password:
        print(f"Welcome, {user_data[email]['first_name']}!")
        # After successful login, call the song management system
        # run_song_management()
    else:
        print("Invalid email or password. Please try again.")

# Run the song management system by calling song_management.py
# def run_song_management():
#     try:
#         subprocess.run(['python3', '/Users/swapnilbaranwal/Desktop/Python_project/song_management.py'])
#   # Assuming song_management.py is in the same folder
#     except FileNotFoundError:
#         print("Error: The song_management.py file was not found.")
#     except Exception as e:
#         print(f"An error occurred while running the song management system: {e}")

# Exit functionality
def exit_program():
    print("Exiting the application. Goodbye!")
    exit()  # Exit the program

# Main program loop
def main():
    while True:
        display_menu()
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
