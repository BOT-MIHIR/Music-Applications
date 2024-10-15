# Initialize an empty dictionary to store song data
songs_database = {}

# Load the song data from a file automatically on program start
def load_song_data(filename):
    global songs_database  # Modify the global songs_database variable

    # Clear the existing song database before loading new data
    songs_database = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line by commas to get the song details
                song_details = [item.strip().strip('"') for item in line.split(',')]

                if len(song_details) == 5:
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
        print("Songs loaded successfully.")
    except FileNotFoundError:
        print(f"Error: {filename} file not found.")
    except Exception as e:
        print(f"An error occurred while loading the song data: {e}")

# Search for a song by title (case-insensitive)
def search_song_by_title():
    title_input = input("Enter the song title to search: ").strip().lower()

    found = False
    for artist, songs in songs_database.items():
        for song in songs:
            if song['title'].strip().lower() == title_input:
                print(f"Song found: \nTitle: {song['title']}\nArtist: {artist}\nAlbum: {song['album']}\nGenre: {song['genre']}\nDuration: {song['duration']}")
                found = True
                break

    if not found:
        print(f"No song with the title '{title_input}' was found.")

# Search for all songs by an artist (case-insensitive)
def search_songs_by_artist():
    artist_input = input("Enter the artist's name to search: ").strip().lower()

    found_artist = None
    for stored_artist in songs_database:
        if stored_artist.strip().lower() == artist_input:
            found_artist = stored_artist
            break

    if found_artist:
        print(f"Songs by {found_artist}:")
        for song in songs_database[found_artist]:
            print(f"Title: {song['title']}, Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']}")
    else:
        print(f"No songs found for artist '{artist_input}'.")

# Main program loop with menu options for searching
def main():
    # Load songs data automatically when the program starts
    load_song_data('Song_Data.txt')

    while True:
        print("\nUser Menu:")
        print("1. Search for a Song by Title")
        print("2. Search for All Songs by an Artist")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            search_song_by_title()
        elif choice == "2":
            search_songs_by_artist()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
