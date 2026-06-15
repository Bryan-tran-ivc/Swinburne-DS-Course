STUDENTS = [
    [100,'Fred'],
    [200,'Sam'],
    [300,'Jill'],
    [400,'Jenny']
]

# get the student id at the array index position
def get_student_id(array_index):
    return STUDENTS[array_index][0]

# get the student name at the array index position
def get_student_name(array_index):
    return STUDENTS[array_index][1]

# get the student name for the given student id (not array position)
def get_student_name_for_id(student_id):
    num_students = len(STUDENTS)

    count = 0
    found = False
    result = 'Not Found'

    while count < num_students and not found:
        if STUDENTS[count][0] == student_id:
            found = True
            result = STUDENTS[count][1]
        else:
            count += 1

    return result

def main():
    print(get_student_id(0))
    print(get_student_name(3))
    print(get_student_name_for_id(300))

if __name__ == '__main__':
    main()
