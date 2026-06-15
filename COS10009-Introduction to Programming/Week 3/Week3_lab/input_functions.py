def read_string(prompt):
    return input(prompt)


def read_float(prompt):
    return float(read_string(prompt))


def read_integer(prompt):
    return int(read_string(prompt))


def read_integer_in_range(prompt, min_value, max_value):
    value = read_integer(prompt)
    while value < min_value or value > max_value:
        print(f"Please enter a value between {min_value} and {max_value}.")
        value = read_integer(prompt)
    return value


def read_boolean(prompt):
    value = read_string(prompt).lower()
    return value in ['y', 'yes']


def print_float(value, decimal_places):
    print(round(value, decimal_places))
