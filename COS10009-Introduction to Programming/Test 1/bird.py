import input_functions

# Complete the code below
# Use input_functions to read the data from the user

# Create a Python class that can be used to create records for the bird
# A bird has: an id (integer), a location caught (string), a species (string), and a cage number (integer)
class Bird:
    def __init__(self, id, location, species, cage_number):
         self.id = id
         self.location = location
         self.species = species
         self.cage_number = cage_number
         

# A function that reads from the terminal values for each of the fields in a bird record and returns the completed record
def read_a_bird():
    id = input_functions.read_integer("Enter bird id:\n" )
    location = input_functions.read_string("Enter bird location:\n")
    species = input_functions.read_string("Enter bird species:\n")
    cage_number = input_functions.read_integer("Enter bird cage number:\n")
    bird = Bird(id, location, species, cage_number)
    return bird
  


# A function that calls your read_a_bird() and returns an array of birds
def read_birds():
    birds = []
    count = input_functions.read_integer("How many birds are you entering:\n")      
    for i in range(count):
         bird = read_a_bird()
         birds.append(bird)
    return birds
    


# A procedure that takes a bird record and writes each of the fields to the terminal
def print_a_bird(bird):
    print("Id", bird.id)
    print("Location", bird.location)
    print("Species", bird.species)
    print("Cage Number", bird.cage_number)
    


# A procedure that calls your print_a_bird(bird) procedure for each bird in the array
def print_birds(birds):
    for bird in birds:
         print_a_bird(bird)
    


def main():
	birds = read_birds()
	print_birds(birds)

main()