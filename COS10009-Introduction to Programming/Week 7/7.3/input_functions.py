# Display the prompt and return the user input
def read_string(prompt):
    return input(prompt).strip()

# Display the prompt and return the user input as a float
def read_float(prompt):
    return float(read_string(prompt).strip())

# Display the prompt and return the user input as an integer
def read_int(prompt):
    return int(read_string(prompt).strip())

# Read an int between a min and max value (not inclusive)
def read_int_in_range(prompt, min, max):
    value = read_int(prompt)
    while value <= min or value >= max:
        print(f"Please enter a value between {min} and {max}.")
        value = read_int(prompt)
    return value

def read_boolean(prompt):
    value = read_string(prompt).lower()
    return value in ['y', 'yes']