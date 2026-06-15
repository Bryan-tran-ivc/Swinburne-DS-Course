GENRE = {
    1 : "Pop",
    2 : "Classic",
    3 : "Jazz",
    4 : "Rock"
}

class Album():
    # NB: you will need to add tracks to the following and finish the initialiser
    
    # complete the missing code:
    def __init__(self, title, artist, genre, tracks):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.tracks = tracks

class Track():
    def __init__(self, name, location):
        self.title = name
        self.file_location = location

# Reads in and returns a single track from the given file
def read_track(music_file):
    # Fill in the missing code
    track_name = music_file.readline().strip()
    track_location = music_file.readline().strip()
    track = Track(track_name, track_location)
    return track

# Returns an array of tracks read from the given file
def read_tracks(music_file):
    count = int(music_file.readline())
    tracks = []

    # Put a while loop here which increments an index to read the tracks
    index = 0
    while index < count:
        track = read_track(music_file)
        tracks.append(track)
        index += 1
    return tracks

# Takes an array of tracks and prints them to the terminal
def print_tracks(tracks):
    # print all the tracks use: tracks[x] to access each track.
    index = 0
    while index < len(tracks):
        print(tracks[index].title)
        print(tracks[index].file_location)
        index += 1

# Reads in and returns a single album from the given file, with all its tracks
def read_album(music_file):
    # read in all the Album's fields/attributes including all the tracks
    # complete the missing code
    album_artist = music_file.readline().strip()
    album_title = music_file.readline().strip()
    album_genre = int(music_file.readline())
    tracks = read_tracks(music_file)
    album = Album(album_title, album_artist, album_genre, tracks)
    return album

# Takes a single album and prints it to the terminal along with all its tracks
def print_album(album):
    # print out all the albums fields/attributes
    # Complete the missing code.
    print(album.artist)
    print(album.title)
    print(f"Genre is {album.genre}")
    print(f"{GENRE[album.genre]}")
    # print out the tracks
    print_tracks(album.tracks)

# Takes a single track and prints it to the terminal
def print_track(track):
    print(f"Track title is: {track.title}")
    print(f"Track file location is: {track.file_location}")

# Reads in an album from a file and then print the album to the terminal
def main():
    file_name = "album.txt"
    with open(file_name, "r") as music_file:
        album = read_album(music_file)
        music_file.close()
        print_album(album)

if __name__ == "__main__":
    main()