
from task4_dog import Dog # put your class definition in task4_dog.py

def main():
    # put your code here
    dog = read_dog_info()
    print_dog_info(dog)

def read_dog_info():
    id = input("Enter dog's ID: ")
    breed = input("Enter dog's breed: ")
    name = input("Enter dog's name: ")
    return Dog(id, breed, name)

def print_dog_info(dog):
    print(f"id: {dog.id}")
    print(f"Breed: {dog.breed}")
    print(f"Name: {dog.name}")

if __name__ == "__main__":
    main()
 