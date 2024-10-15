# Initialize an empty dictionary to store song data
songs_database = {}

# Display the developer menu
def display_menu():
    print("\nDeveloper Menu:")
    print("1. Load Song Data")
    print("2. View Songs Database")
    print("3. Delete a Song")
    print("4. Modify a Song")
    print("5. Exit")

# Load song data from a file
def load_song_data(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line by commas to get the song details
                song_details = [item.strip().strip('"') for item in line.split(',')]
                if len(song_details) == 5:  # Ensure there are 5 elements (Title, Artist, Album, Genre, Duration)
                    title, artist, album, genre, duration = song_details

                    # Add the song to the database, grouped by artist
                    if artist not in songs_database:
                        songs_database[artist] = []
                    songs_database[artist].append({
                        'title': title,
                        'album': album,
                        'genre': genre,
                        'duration': duration
                    })
        print(f"Songs loaded from {filename}.")
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An error occurred while loading the song data: {e}")

# View the songs database
def view_songs_database():
    if not songs_database:
        print("The song database is empty. Please load the data first.")
        return
    
    print("\nSongs Database:")
    print("{:<30} {:<20} {:<15}".format("Title", "Artist", "Genre"))
    print("=" * 65)
    
    for artist, songs in songs_database.items():
        for song in songs:
            print("{:<30} {:<20} {:<15}".format(song['title'], artist, song['genre']))

# Delete a song by title and artist
def delete_song():
    artist = input("Enter the artist of the song: ").strip().lower()
    title = input("Enter the title of the song: ").strip().lower()

    # Loop through the songs database and compare both artist and title in a case-insensitive manner
    found = False
    for stored_artist, songs in songs_database.items():
        if stored_artist.strip().lower() == artist:  # Compare artist name
            for song in songs:
                if song['title'].strip().lower() == title:  # Compare song title
                    songs_database[stored_artist].remove(song)
                    print(f"Song '{title}' by {artist} deleted successfully.")
                    found = True
                    break
            if found:
                break

    if not found:
        print(f"Song '{title}' by '{artist}' not found in the database.")


def modify_song():
    artist_input = input("Enter the artist of the song: ").strip().lower()
    title_input = input("Enter the title of the song: ").strip().lower()

    # Find the artist in a case-insensitive way
    found_artist = None
    for stored_artist in songs_database:
        if stored_artist.strip().lower() == artist_input:
            found_artist = stored_artist
            break

    if found_artist:
        # Find the song in a case-insensitive way
        for song in songs_database[found_artist]:
            if song['title'].strip().lower() == title_input:
                print("Which detail do you want to modify? (Album, Genre, Duration)")
                field_to_modify = input("Enter the detail to modify: ").strip().lower()

                # Check if the field exists in the song dictionary
                if field_to_modify in song:
                    new_value = input(f"Enter new {field_to_modify.capitalize()}: ")
                    song[field_to_modify] = new_value
                    print(f"{field_to_modify.capitalize()} updated successfully.")
                    return
                else:
                    print(f"{field_to_modify.capitalize()} is not a valid field.")
                return

        print(f"Song '{title_input}' not found for artist '{found_artist}'.")
    else:
        print(f"Artist '{artist_input}' not found in the database.")


# Main loop
def main():
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            filename = input("Enter the file name to load songs: ")
            load_song_data(filename)
        elif choice == "2":
            view_songs_database()
        elif choice == "3":
            delete_song()
        elif choice == "4":
            modify_song()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
