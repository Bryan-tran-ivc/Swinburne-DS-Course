# Display the prompt and return the read string
def read_string(prompt):
    value = input(prompt)
    return value


# Display the prompt and return the read float
def read_float(prompt):
    value = read_string(prompt)
    return float(value)


# Display the prompt and return the read integer
def read_integer(prompt):
    value = read_string(prompt)
    return int(value)


# Read an integer between min and max, prompting with the string provided
def read_integer_in_range(prompt, min_val, max_val):
    value = read_integer(prompt)
    while value < min_val or value > max_val:
        print(f"Please enter a value between {min_val} and {max_val}: ")
        value = read_integer(prompt)
    return value


# Display the prompt and return the read Boolean
def read_boolean(prompt):
    value = read_string(prompt)
    match value:
        case "y" | "yes" | "Yes" | "YES":
            return True
        case _:
            return False


# ===============================
# Test the functions above
# ===============================
def main():
    print("String entered is:", read_string("Enter a String: "))
    print("Boolean is:", read_boolean("Enter yes or no: "))
    print("Float is:", read_float("Enter a floating point number: "))
    print(
        "Integer is:",
        read_integer_in_range(
            "Enter an integer between 3 and 6: ", 3, 6
        )
    )


if __name__ == "__main__":
    main()
