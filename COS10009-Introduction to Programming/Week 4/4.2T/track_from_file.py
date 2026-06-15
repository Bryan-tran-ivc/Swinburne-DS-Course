# Track class
class Track:
    def __init__(self, name, location):
        # Store the name and location in the object
        self.name = name
        self.location = location


# reads in a single track from the given file
def read_track(a_file):
    # Read the track name from the file
    name = a_file.readline().strip()

    # Read the track location from the file
    location = a_file.readline().strip()

    # Create and return a Track object
    return Track(name, location)


# Takes a single track and prints it to the terminal
def print_track(track):
    print("Track name:", track.name)
    print("Track location:", track.location)


def main():
    # Open the file for reading
    a_file = open("track.txt", "r")

    # Read the track
    track = read_track(a_file)

    # Print the track
    print_track(track)

    # Close the file
    a_file.close()


if __name__ == "__main__":
    main()