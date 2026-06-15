from student import *

def test_student_id_is_integer():
    result = get_student_id(2)
    assert isinstance(result, int) # Use an assertion method

# insert a test here for the finding the correct student for id 300
def test_find_student_id_300():
    result = get_student_name_for_id(300)
    assert result == 'Jill'

# insert a test here for returning "Not Found" for student with id 800
def test_student_id_800_not_found():
    result = get_student_name_for_id(800)
    assert result == 'Not Found'

# insert a test here for finding the correct student name for array position 0
def test_get_student_name_at_index_0():
    result = get_student_name(0)
    assert result == 'Fred'