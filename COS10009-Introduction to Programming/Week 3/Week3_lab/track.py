import input_functions as input_functions

class Track:
    def __init__(self, name="", location=""):
        self.name = name
        self.location = location

def read_track():
    # Read track name
    track_name = input_functions.read_string("Enter track name: ")
    # Read track location
    track_location = input_functions.read_string("Enter track location: ")
    # Create and return Track object
    track = Track(track_name, track_location)
    return track

def print_track(track):
    print(f"Track name: {track.name}")
    print(f"Track location: {track.location}")

def main():
    track = read_track()
    print_track(track)

if __name__ == "__main__":
    main()