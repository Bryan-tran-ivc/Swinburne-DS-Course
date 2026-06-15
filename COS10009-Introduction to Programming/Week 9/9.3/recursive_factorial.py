import sys

# Complete the following
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Add to the following code to prevent errors for:
# 1. No command line argument provided
# 2. Argument value less than 1
def main():
    if len(sys.argv) != 2 or int(sys.argv[1]) < 0:
        puts("Incorrect argument - need a single argument with a value of 0 or more.\n")
    else:
        print(factorial(int(sys.argv[1])))

def puts(s):
    sys.stdout.write(s)

if __name__ == "__main__":
    main()