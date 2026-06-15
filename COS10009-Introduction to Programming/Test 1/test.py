import input_functions

# Complete the code below
# Use input_functions to read the data from the user

# Create a Python class that can be used to create records for the bird
# A bird has: an id (integer), a location caught (string), a species (string), and a cage number (integer)
class Bird:
    def __init__(self, id, location_caught, species, cage_number):
        self.id = id
        self.location_caught = location_caught
        self.species = species
        self.cage_number = cage_number

# A function that reads from the terminal values for each of the fields in a bird record and returns the completed record
def read_a_bird():
    bird_id = input_functions.read_integer("Enter the bird's id:\n")
    location_caught = input_functions.read_string("Enter the location where the bird was caught:\n")
    species = input_functions.read_string("Enter the bird's species:\n")
    cage_number = input_functions.read_integer("Enter the bird's cage number:\n")
    return Bird(bird_id, location_caught, species, cage_number)


# A function that calls your read_a_bird() and returns an array of birds
def read_birds():
    count = input_functions.read_integer("How many birds do you want to enter?\n")
    birds_array = []
    for index in range(count):
        bird = read_a_bird()
        birds_array.append(bird)
    return birds_array


# A procedure that takes a bird record and writes each of the fields to the terminal
def print_a_bird(bird):
    print(f"ID {bird.id}")
    print(f"Location {bird.location_caught}")
    print(f"Species {bird.species}")
    print(f"Cage Number {bird.cage_number}")


# A procedure that calls your print_a_bird(bird) procedure for each bird in the array
def print_birds(birds):
    for bird in birds:
        print_a_bird(bird)

def main():
	birds = read_birds()
	print_birds(birds)

main()