def read_string(prompt):
    return input(prompt).strip()

def read_float(prompt):
    return float(read_string(prompt))

def read_int(prompt):
    return int(read_string(prompt))

def read_int_in_range(prompt, min_val, max_val):
    value = read_int(prompt)
    while value < min_val or value > max_val:
        print("Please enter a value between " + str(min_val) + " and " + str(max_val) + ".")
        value = read_int(prompt)
    return value

def read_boolean(prompt):
    value = read_string(prompt).lower()
    return value in ['y', 'yes']