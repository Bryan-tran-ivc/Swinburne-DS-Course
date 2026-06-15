import input_functions as input_functions

GENRE_NAMES = {
    1: "Pop",
    2: "Classic",
    3: "Jazz",
    4: "Rock"
}
class Album:
    # Optional: you may add an __init__ method
    def __init__(self, name="", artist="", genre=0):
        self.name = name
        self.artist = artist
        self.genre = genre
def read_album():
    print("Enter Album")
    # Read the album name
    album_name = input_functions.read_string("Enter album name: ")
    # Read the artist name
    artist_name = input_functions.read_string("Enter artist name: ")
    # Read the genre number (1 - 4)
    genre_number = input_functions.read_integer_in_range(
        "Enter Genre between 1 - 4: ", 1, 4
    )
    # Create Album object
    album = Album(album_name, artist_name, genre_number)
    return album
def print_album(album):
    print("Album information is:")
    # Print album details
    print(album.name)
    print(album.artist)
    print(f"Genre is {album.genre}")
    print(GENRE_NAMES[album.genre])

def main():
    album = read_album()
    print_album(album)

if __name__ == "__main__":
    main()