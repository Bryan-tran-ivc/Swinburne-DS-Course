def read_string(prompt):
    return input(prompt).strip()

def read_int(prompt):
    value = read_string(prompt)
    try:
        return int(value)
    except ValueError:
        return -1

def read_int_in_range(prompt, min_val, max_val):
    value = read_int(prompt)
    while value < min_val or value > max_val:
        print(f"Please enter a value between {min_val} and {max_val}.")
        value = read_int(prompt)
    return value