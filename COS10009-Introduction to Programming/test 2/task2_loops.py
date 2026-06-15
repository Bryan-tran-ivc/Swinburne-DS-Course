def main():
    total = 0
    i = 1
    while i <= 10:
        input_value = int(input(f"Enter an integer {i}: "))
        total += input_value
        i += 1
    print(f"Total is: {total}")

if __name__ == "__main__":
    main()