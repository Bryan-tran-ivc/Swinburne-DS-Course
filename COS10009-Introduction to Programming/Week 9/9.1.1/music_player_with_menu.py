import time
import input_functions

GENRE = {1: "Pop", 2: "Classic", 3: "Jazz", 4: "Rock"}


class Track:
    def __init__(self, name, location):
        self.title = name
        self.file_location = location


class Album:
    def __init__(self, artist, title, year, genre, tracks):
        self.artist = artist
        self.title = title
        self.year = year
        self.genre = genre
        self.tracks = tracks


def read_tracks(music_file):
    count = int(music_file.readline().strip())
    tracks = []
    i = 0
    while i < count:
        title    = music_file.readline().strip()
        location = music_file.readline().strip()
        tracks.append(Track(title, location))
        i += 1
    return tracks


def load_albums_from_file(file_name):
    try:
        music_file = open(file_name, "r")
        count  = int(music_file.readline().strip())
        albums = []
        i = 0
        while i < count:
            artist = music_file.readline().strip()
            title  = music_file.readline().strip()
            year   = music_file.readline().strip()
            genre  = int(music_file.readline().strip())
            tracks = read_tracks(music_file)
            albums.append(Album(artist, title, year, genre, tracks))
            i += 1
        music_file.close()
        return albums
    except FileNotFoundError:
        print("Error: File '" + file_name + "' not found.")
        return None
    except Exception as e:
        print("An error occurred: " + str(e))
        return None


def display_albums(albums):
    print("\n1. Display all albums")
    print("2. Display by genre")
    sub_choice = input_functions.read_int_in_range("Choice: ", 1, 2)

    genre_filter = None
    if sub_choice == 2:
        print("\nAvailable genres:")
        g = 1
        while g <= len(GENRE):
            print("  " + str(g) + ": " + GENRE[g])
            g += 1
        genre_filter = input_functions.read_int_in_range("Enter Genre ID: ", 1, len(GENRE))

    print("\n--- ALBUM LIST ---")
    i = 0
    while i < len(albums):
        album      = albums[i]
        album_id   = str(i + 1)
        genre_name = GENRE.get(album.genre, "Unknown")

        if genre_filter is None or album.genre == genre_filter:
            print("Album ID " + album_id + ": " + album.artist + " - " + album.title +
                  " (" + album.year + ") [" + genre_name + "]")
        i += 1


def play_from_album(albums):
    album_id = input_functions.read_int_in_range("Enter Album ID: ", 1, len(albums))
    album    = albums[album_id - 1]

    print("\nTracks for '" + album.title + "':")
    i = 0
    while i < len(album.tracks):
        print("  " + str(i + 1) + ". " + album.tracks[i].title)
        i += 1

    track_num = input_functions.read_int_in_range("Enter track number: ", 1, len(album.tracks))
    track     = album.tracks[track_num - 1]

    print("\n>>> Playing track '" + track.title + "' from album '" + album.title + "'")
    time.sleep(3)


def main():
    albums   = []
    finished = False

    while not finished:
        print("\n=== MAIN MENU ===")
        print("1. Read in Albums")
        print("2. Display Albums")
        print("3. Select an Album to play")
        print("5. Exit")

        choice = input_functions.read_int("Enter choice: ")

        if choice == 1:
            file_name = input_functions.read_string("Enter filename: ")
            result    = load_albums_from_file(file_name)
            if result is not None:
                albums = result
                print("Successfully loaded " + str(len(albums)) + " albums.")

        elif choice == 2:
            if not albums:
                print("No albums loaded. Please use Option 1 first.")
            else:
                display_albums(albums)

        elif choice == 3:
            if not albums:
                print("No albums loaded. Please use Option 1 first.")
            else:
                play_from_album(albums)

        elif choice == 5:
            print("Goodbye!")
            finished = True

        else:
            print("Invalid selection, please try again.")


if __name__ == "__main__":
    main()