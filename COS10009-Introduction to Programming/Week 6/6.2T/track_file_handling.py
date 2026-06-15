class Track:
    def __init__(self, name, location):
        self.name = name
        self.location = location

def read_tracks(music_file):
    count = int(music_file.readline().strip())
    tracks = []

    # A while loop which increments an index to read the tracks
    index = 0
    while index < count:
        track = read_track(music_file)
        tracks.append(track)
        index += 1

    return tracks

def read_track(music_file):
    # Read the track name and location, then create and return a Track object
    name = music_file.readline().strip()
    location = music_file.readline().strip()
    return Track(name, location)

def print_tracks(tracks):
    # Use a while loop with a control variable index to print each track. 
    # (Note: In Python, we use len(tracks) instead of tracks.length)
    index = 0
    while index < len(tracks):
        print_track(tracks[index])
        index += 1

def print_track(track):
    # Adjusted to match the sample output exactly (without "Track Name:" labels)
    print(track.name)
    print(track.location)

def main():
    music_file = open("input.txt", "r") # Open for reading
    
    # You must call read_tracks first to populate the tracks array
    tracks = read_tracks(music_file)
    
    # Print all the tracks
    print_tracks(tracks)
    
    music_file.close()

# Ensures the script runs the main function when executed
if __name__ == "__main__":
    main()