class MyRecord():
    def __init__(self, name, age):
        self.name = name
        self.age = age


def compare(a, b, direction):
    if direction:
        return a > b
    else:
        return a < b


def sort(arr, direction):
    item_count = len(arr)
    i = 0
    while i < item_count - 1:
        j = 0
        while j < item_count - 1 - i:
            if compare(arr[j].age, arr[j + 1].age, direction):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1
    return arr


def is_numeric(obj):
    return obj.isnumeric()


def read(aFile):
    people = []

    count_str = aFile.readline().strip()
    print("First line: " + count_str)

    if is_numeric(count_str):
        count = int(count_str)
    else:
        count = 0
        print("Error: first line of file is not a number")

    index = 0
    while index < count:
        name    = aFile.readline().strip()
        age_str = aFile.readline().strip()

        if name and age_str and is_numeric(age_str):
            age    = int(age_str)
            record = MyRecord(name, age)
            people.append(record)
            print("Line read: " + name)
        else:
            print("Warning: invalid data at record " + str(index + 1) + ", skipping.")

        index += 1

    return people


def print_array(lst):
    print("Printing list - number of elements: " + str(len(lst)))
    i = 0
    while i < len(lst):
        print("Name: " + lst[i].name + "  \n  Age: " + str(lst[i].age))
        i += 1


def main():
    aFile  = open("data.txt", "r")
    people = read(aFile)
    aFile.close()

    sorted_people = sort(people, True)
    print_array(sorted_people)


if __name__ == "__main__":
    main()