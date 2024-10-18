# BeatBuddies Music Applications

This project is designed to manage and play songs using a database-driven approach via cmd prompt. It includes features for authorization, developer settings, and song management.

## Installation

1. Install the latest version of python.
2. Check Python has correctly installed on your system or not by typing the below command.
      ```bash
   pip install py -0 
   ``` 
4. Download the repository.
5. Run the scripts as needed.

## Guide

## Authorization_Systems.py Key Functions

### 1. load_user_data()
Loads user data from a user_data.txt file into a dictionary. Each user's information includes their email, password, first name, last name, and age.

![Fauntion1](https://github.com/user-attachments/assets/44425f56-2c2b-4fee-810a-f9f048b1e5f9)


### 2. signin(user_data)
Handles user sign-in by checking the entered email and password against stored data. If successful, it welcomes the user; otherwise, it prompts for re-entry.

![Fauntion3](https://github.com/user-attachments/assets/0b833997-18fa-4a99-8225-41b2f5f90ab1)

### 3. exit_program()
Exits the application with a farewell message.

![Fauntion4](https://github.com/user-attachments/assets/d2de8312-8c3f-40a4-ba80-a80960bca458)


## Developer_Settings.py Key Functions

## Song Database Management

### 1. load_song_data(filename)
Loads song details from a specified file into the songs_database. Each line in the file should contain song details separated by commas (Title, Artist, Album, Genre, Duration). 

![WhatsApp Image 2024-10-18 at 20 52 54_24456f53](https://github.com/user-attachments/assets/900f35f3-af21-4520-85c8-a9e55daa427c)


### 2. view_songs_database()
Displays the current song database in a tabular format, showing the title, artist, and genre of each song.

![Faunction2](https://github.com/user-attachments/assets/be40a741-73a8-49ae-98d7-e1bf0111a973)

### 3. delete_song()
Allows users to delete a song from the database by providing the song's title and artist. The search is case-insensitive.

![Faunction3](https://github.com/user-attachments/assets/c0b2aa41-bcbb-4840-a046-0d453244f2b6)

### 4. modify_song()
Enables users to modify specific details (Album, Genre, Duration) of a song by providing the song's title and artist. Users are prompted to specify which detail to change.

![Faunction4](https://github.com/user-attachments/assets/780b17ab-5725-4b70-a8f6-c31a9c44fac4)

## Song Database Application Key Functions

### load_song_data(filename)
- Loads song data from a specified text file into a dictionary (songs_database), structured by artist.
- Each song entry includes its title, album, genre, and duration.
- Handles file not found errors and other exceptions gracefully.

### search_song_by_title()
- Prompts the user to enter a song title and searches for it in the database.
- Displays details of the song if found, or informs the user if not.

### search_songs_by_artist()
- Prompts the user to enter an artist's name and searches for all songs by that artist.
- Displays the list of songs if found, or notifies the user if none are found.

### main()
- Serves as the main program loop, loading the song data and presenting a user menu for searching options.


## Requirements
- Python 3.x

# Usage

- Use `Authorization_System.py` for managing user access.
- `Songs_db.py` handles song storage and database operations.
- Modify `Developer_Settings.py` for developer-specific configurations.

1. Run the application.
2. Choose an option from the menu: 
   - Sign up 
   - Sign in 
   - Exit
3. Follow the prompts to manage your user account.


## Additional Information

Ensure the `Song_Data.txt` file is populated with the correct data format for the system to function as expected.

## Contributors

- Mihir Suhanda
- Umar Farooq Kazi
